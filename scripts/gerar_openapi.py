"""Gera docs/openapi.json a partir do código do backend do IFVest.

A especificação é montada pelo próprio FastAPI, a partir das rotas e dos esquemas
Pydantic: o script só importa a aplicação e grava o resultado. Não sobe servidor,
não conecta ao banco e não precisa das credenciais do Firebase.

Uso, na raiz deste repositório (Windows: troque python3 por py):

    python3 -m pip install -r <monorepo>/ifvest-backend/requirements.txt
    python3 scripts/gerar_openapi.py <monorepo>/ifvest-backend

No fim, o script mostra quantas operações cada grupo tem. Esses números aparecem
em docs/api.md e docs/arquitetura.md, que são escritos à mão: confira se mudaram.
"""

import argparse
import collections
import json
import sys
from pathlib import Path

DESTINO = Path(__file__).resolve().parent.parent / "docs" / "openapi.json"
METODOS_HTTP = {"get", "post", "put", "patch", "delete"}


def carregar_especificacao(pasta_backend: Path) -> dict:
    """Importa src.main do backend e devolve o dicionário OpenAPI."""
    if not (pasta_backend / "src" / "main.py").is_file():
        sys.exit(
            f"Não encontrei src/main.py em '{pasta_backend}'. "
            "Informe a pasta ifvest-backend do monorepo, por exemplo: ../ifvest-monorepo/ifvest-backend"
        )
    sys.path.insert(0, str(pasta_backend))
    try:
        # Import aqui dentro: o caminho do backend só é conhecido depois de ler o argumento
        from src.main import app
    except ModuleNotFoundError as erro:
        sys.exit(
            f"Falta a dependência '{erro.name}'. Instale as do backend com: "
            f"python3 -m pip install -r {pasta_backend / 'requirements.txt'}"
        )
    return app.openapi()


def resumir(especificacao: dict) -> None:
    """Mostra operações por grupo (tag), caminhos e esquemas."""
    por_grupo: collections.Counter[str] = collections.Counter()
    for caminho, operacoes in especificacao["paths"].items():
        for metodo, operacao in operacoes.items():
            if metodo in METODOS_HTTP and caminho.startswith("/api/v1"):
                por_grupo[(operacao.get("tags") or ["(sem grupo)"])[0]] += 1

    caminhos_api = [c for c in especificacao["paths"] if c.startswith("/api/v1")]
    esquemas = especificacao.get("components", {}).get("schemas", {})
    print(f"Gravado em {DESTINO}")
    print(f"Operações sob /api/v1: {sum(por_grupo.values())}, em {len(caminhos_api)} caminhos")
    print(f"Esquemas de dados: {len(esquemas)}")
    for grupo, total in por_grupo.most_common():
        print(f"  {grupo:15s} {total}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("backend", type=Path, help="pasta ifvest-backend do monorepo")
    args = parser.parse_args()

    especificacao = carregar_especificacao(args.backend.resolve())
    DESTINO.write_text(json.dumps(especificacao, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    resumir(especificacao)


if __name__ == "__main__":
    main()
