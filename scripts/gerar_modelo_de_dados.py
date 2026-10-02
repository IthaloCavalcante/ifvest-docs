"""Gera os diagramas de docs/modelo-de-dados.md a partir dos modelos do backend do IFVest.

Os diagramas saem dos metadados do SQLAlchemy, as mesmas definições que o Alembic
compara com o banco, e não de um desenho feito à mão. O script substitui só o trecho
entre os marcadores INÍCIO e FIM da página; o restante dela é escrito à mão.

Uso, na raiz deste repositório (Windows: troque python3 por py):

    python3 -m pip install -r <monorepo>/ifvest-backend/requirements.txt
    python3 scripts/gerar_modelo_de_dados.py <monorepo>/ifvest-backend

Se o backend ganhar uma tabela que ainda não está em DOMINIOS, ela vai para a seção
"Sem domínio definido" e o script avisa: inclua-a no domínio certo e rode de novo.
"""

import argparse
import importlib
import pkgutil
import re
import sys
from pathlib import Path

PAGINA = Path(__file__).resolve().parent.parent / "docs" / "modelo-de-dados.md"
INICIO = "<!-- INÍCIO do trecho gerado por scripts/gerar_modelo_de_dados.py: não edite à mão -->"
FIM = "<!-- FIM do trecho gerado -->"

# Cada domínio lista suas tabelas e as de outros domínios que mostram a ligação entre eles.
DOMINIOS: dict[str, list[str]] = {
    "Usuários e permissões": ["permissions", "user_permissions", "users"],
    "Taxonomia": ["disciplines", "subjects", "topics"],
    "Banco de questões": ["alternatives", "multiple_choice_questions", "question_topics", "topics"],
    "Simulados": [
        "fixed_mocktests", "multiple_choice_questions", "questions_mocktests", "user_mocktests", "users",
    ],
    "Quiz e gamificação": [
        "items", "multiple_choice_questions", "question_history", "quiz_history", "transactions", "users",
    ],
    "Redação": ["essay_annotations", "essays", "gradings", "proposals", "support_texts", "users"],
    "Moderação e auditoria": ["audit_logs", "multiple_choice_questions", "question_reports", "users"],
    "Plataforma": ["feature_flags"],
}

# Nome do tipo no PostgreSQL -> forma curta usada nos diagramas
TIPOS_CURTOS = {
    "integer": "int",
    "boolean": "bool",
    "character varying": "varchar",
    "timestamp without time zone": "timestamp",
    "timestamp with time zone": "timestamptz",
}


def carregar_metadados(pasta_backend: Path):
    """Importa todos os módulos de src/models e devolve Base.metadata."""
    if not (pasta_backend / "src" / "models" / "base.py").is_file():
        sys.exit(
            f"Não encontrei src/models/base.py em '{pasta_backend}'. "
            "Informe a pasta ifvest-backend do monorepo, por exemplo: ../ifvest-monorepo/ifvest-backend"
        )
    sys.path.insert(0, str(pasta_backend))
    try:
        import src.models as pacote_modelos
        from src.models.base import Base
    except ModuleNotFoundError as erro:
        sys.exit(
            f"Falta a dependência '{erro.name}'. Instale as do backend com: "
            f"python3 -m pip install -r {pasta_backend / 'requirements.txt'}"
        )
    for modulo in pkgutil.iter_modules(pacote_modelos.__path__):
        importlib.import_module(f"src.models.{modulo.name}")
    return Base.metadata


def tipo_curto(coluna) -> str:
    from sqlalchemy.dialects import postgresql

    nome = coluna.type.compile(dialect=postgresql.dialect()).lower()
    nome = re.sub(r"\(.*\)", "", nome).strip()
    return TIPOS_CURTOS.get(nome, nome)


def coluna_unica(coluna) -> bool:
    if coluna.unique:
        return True
    return any(
        type(regra).__name__ == "UniqueConstraint" and [c.name for c in regra.columns] == [coluna.name]
        for regra in coluna.table.constraints
    )


def chaves_da_coluna(coluna) -> str:
    chaves = []
    if coluna.primary_key:
        chaves.append("PK")
    if coluna.foreign_keys:
        chaves.append("FK")
    if not coluna.primary_key and coluna_unica(coluna):
        chaves.append("UK")
    return " " + ", ".join(chaves) if chaves else ""


def bloco_tabela(tabela) -> list[str]:
    linhas = [f"    {tabela.name} {{"]
    for coluna in tabela.columns:
        linhas.append(f"        {tipo_curto(coluna)} {coluna.name}{chaves_da_coluna(coluna)}")
    linhas.append("    }")
    return linhas


def relacoes(metadados, tabelas: set[str]) -> list[str]:
    """Uma linha por chave estrangeira cujas duas pontas estão em `tabelas`."""
    linhas = []
    for tabela in sorted(metadados.tables.values(), key=lambda t: t.name):
        for coluna in tabela.columns:
            for fk in sorted(coluna.foreign_keys, key=lambda f: f.target_fullname):
                pai = fk.column.table.name
                if tabela.name in tabelas and pai in tabelas:
                    ponta_pai = "|o" if coluna.nullable else "||"
                    ponta_filho = "o|" if coluna_unica(coluna) else "o{"
                    linhas.append(f'    {pai} {ponta_pai}--{ponta_filho} {tabela.name} : ""')
    return linhas


def diagrama(linhas: list[str]) -> list[str]:
    return ["```mermaid", "erDiagram", *linhas, "```"]


def lista_de_nomes(nomes: list[str]) -> str:
    nomes = [f"`{n}`" for n in nomes]
    return nomes[0] if len(nomes) == 1 else ", ".join(nomes[:-1]) + " e " + nomes[-1]


def gerar_trecho(metadados) -> tuple[str, list[str]]:
    todas = set(metadados.tables)
    total_fks = sum(len(t.foreign_keys) for t in metadados.tables.values())
    ligadas = {fk.column.table.name for t in metadados.tables.values() for fk in t.foreign_keys}
    ligadas |= {t.name for t in metadados.tables.values() if t.foreign_keys}
    isoladas = sorted(todas - ligadas)

    frase_isoladas = ""
    if isoladas:
        verbo = "não aparece" if len(isoladas) == 1 else "não aparecem"
        artigo = "A tabela" if len(isoladas) == 1 else "As tabelas"
        frase_isoladas = (
            f" {artigo} {lista_de_nomes(isoladas)} {verbo} por não ter relacionamento com as demais."
        )

    saida = [
        "## Visão geral dos relacionamentos",
        "",
        f"O esquema tem **{len(todas)} tabelas** e **{total_fks} chaves estrangeiras**. "
        "O diagrama abaixo mostra apenas as tabelas e como se relacionam, sem as colunas."
        + frase_isoladas,
        "",
        *diagrama(relacoes(metadados, todas)),
        "",
        "**Como ler o diagrama:** cada linha liga duas tabelas por uma chave estrangeira. "
        "Na ponta da tabela que guarda a referência, o círculo com o pé de galinha indica que "
        "vários registros dela podem apontar para um mesmo registro do outro lado, e o círculo "
        "com uma barra, que há no máximo um. Na ponta da tabela referenciada, as duas barras "
        "indicam que a referência é obrigatória, e o círculo com uma barra, que ela pode ficar vazia.",
        "",
        "---",
        "",
        "## Tabelas por domínio",
        "",
        "Nas colunas, **PK** indica chave primária, **FK**, chave estrangeira, e **UK**, valor que "
        "não se repete na tabela. Tabelas que aparecem em mais de um domínio estão repetidas para "
        "mostrar a ligação entre eles.",
    ]

    avisos = []
    desconhecidas = [n for tabelas in DOMINIOS.values() for n in tabelas if n not in todas]
    if desconhecidas:
        sys.exit(f"Tabelas listadas em DOMINIOS que não existem nos modelos: {sorted(set(desconhecidas))}")

    sem_dominio = sorted(todas - {n for tabelas in DOMINIOS.values() for n in tabelas})
    dominios = dict(DOMINIOS)
    if sem_dominio:
        dominios["Sem domínio definido"] = sem_dominio
        avisos.append(f"Tabelas sem domínio em DOMINIOS: {', '.join(sem_dominio)}")

    for nome, tabelas in dominios.items():
        corpo = []
        for tabela in sorted(tabelas):
            corpo += bloco_tabela(metadados.tables[tabela])
        corpo += relacoes(metadados, set(tabelas))
        saida += ["", f"### {nome}", "", *diagrama(corpo)]

    return "\n".join(saida), avisos


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("backend", type=Path, help="pasta ifvest-backend do monorepo")
    args = parser.parse_args()

    metadados = carregar_metadados(args.backend.resolve())
    trecho, avisos = gerar_trecho(metadados)

    texto = PAGINA.read_text(encoding="utf-8")
    if INICIO not in texto or FIM not in texto:
        sys.exit(f"Os marcadores do trecho gerado não estão em {PAGINA}:\n  {INICIO}\n  {FIM}")
    antes, resto = texto.split(INICIO, 1)
    _, depois = resto.split(FIM, 1)
    PAGINA.write_text(f"{antes}{INICIO}\n\n{trecho}\n\n{FIM}{depois}", encoding="utf-8")

    total_fks = sum(len(t.foreign_keys) for t in metadados.tables.values())
    print(f"Atualizado: {PAGINA}")
    print(f"{len(metadados.tables)} tabelas, {total_fks} chaves estrangeiras")
    for aviso in avisos:
        print(f"ATENÇÃO: {aviso}")


if __name__ == "__main__":
    main()
