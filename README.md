# Documentação do IFVest

Documentação técnica oficial da plataforma **IFVest**, projeto acadêmico voltado à preparação gratuita de estudantes para o ENEM e vestibulares.

**➜ [Ler a documentação](https://IthaloCavalcante.github.io/ifvest-docs/)**

---

## Sobre este repositório

Este repositório contém os **arquivos-fonte da documentação**, não o código da plataforma. É mantido pela frente de **Testes e Documentação**, que atua transversalmente aos módulos do projeto.

A documentação responde, para quem chega de fora:

- **O que é** o sistema e qual problema ele resolve
- **Como está construído** — arquitetura e diagramas C4
- **O que ele deve fazer** — requisitos funcionais e não-funcionais
- **O que ele faz** — descrição das funcionalidades por módulo
- **Como se usa** — guias de uso por tarefa
- **O que mudou** — registro de versões
- **O que está sendo construído** — frentes de trabalho e projetos paralelos

O plano de produção, as normas adotadas e os critérios aplicados estão em [Planejamento da Documentação](https://IthaloCavalcante.github.io/ifvest-docs/planejamento/).

---

## Estado atual: transição para o IFVest V3

O IFVest está sendo substituído por uma **plataforma nova**, desenvolvida do zero e referida internamente como **IFVest V3**, com stack, modelo de dados e organização de perfis diferentes da versão anterior.

A documentação está sendo **redirecionada para descrever a plataforma nova**. Enquanto essa transição ocorre:

- O conteúdo da versão anterior permanece recuperável pela etiqueta **`legado-v2`** no histórico deste repositório.
- Páginas ainda não revisadas podem descrever a versão anterior — o [Planejamento](https://IthaloCavalcante.github.io/ifvest-docs/planejamento/) indica o estado de cada item.
- A trajetória entre as versões fica registrada no Registro de Versões.

```bash
# Consultar a documentação da versão anterior
git checkout legado-v2
```

---

## Executar localmente

Necessário ter **Python 3.8+** instalado.

```bash
# 1. Instalar as dependências (uma vez por máquina)
py -m pip install --user -r requirements.txt

# 2. Iniciar o servidor local, na pasta que contém o mkdocs.yml
py -m mkdocs serve
```

A documentação fica disponível em `http://127.0.0.1:8000`, com recarregamento automático a cada arquivo salvo.

> **Windows:** use sempre `py -m mkdocs`, e não `mkdocs` direto. A pasta de scripts do Python costuma não estar no PATH, especialmente em computadores de laboratório. Em Linux ou macOS, troque `py` por `python3`.

O arquivo [`tutorial.html`](tutorial.html) traz o passo a passo completo, com verificação a cada etapa e solução dos erros mais comuns.

---

## Estrutura

```
ifvest-docs/
├── mkdocs.yml              # configuração do site e menu de navegação
├── requirements.txt        # dependências
├── tutorial.html           # guia de instalação e execução
└── docs/
    ├── index.md
    ├── planejamento.md     # plano, normas e critérios de produção
    ├── descricao-do-sistema.md
    ├── arquitetura.md
    ├── c4/                 # diagramas C4 (contexto, contêineres, componentes)
    ├── requisitos/
    ├── funcionalidades.md
    ├── versoes.md
    ├── subprojetos/        # frentes de trabalho e projetos paralelos
    ├── guias/              # documentação de usuário
    ├── diagrams/src/       # fontes PlantUML dos diagramas
    └── stylesheets/        # estilos personalizados
```

---

## Editar e publicar

A documentação é escrita em **Markdown** e mantida em formato *docs-as-code*: o conteúdo é versionado como código, revisado por commits e publicado a partir do repositório.

```bash
# 1. Editar os arquivos em docs/ e conferir localmente
py -m mkdocs serve

# 2. Versionar a alteração
git add .
git commit -m "docs: descrição da alteração"
git push

# 3. Publicar no site
py -m mkdocs gh-deploy
```

O `git push` envia os arquivos-fonte; o `gh-deploy` reconstrói e atualiza o site publicado. **São passos distintos** — commitar não atualiza a URL.

Cada página do site tem um ícone de edição que leva diretamente ao arquivo correspondente neste repositório.

### Contribuindo

Correções e complementos são bem-vindos, especialmente de quem desenvolve os módulos. Seguindo as convenções do projeto:

- **Branches:** `docs/nome-da-alteracao`
- **Commits:** padrão Conventional Commits, com prefixo `docs:`
- **Pull Requests:** sempre, para revisão antes do merge

Se algo nesta documentação não corresponder ao que foi implementado, **abra uma issue** — divergências entre documentação e código são registradas explicitamente, não corrigidas em silêncio.

---

## Normas adotadas

A documentação segue normas internacionais de documentação de software, adaptadas ao contexto de um projeto acadêmico:

| Norma | Papel |
|---|---|
| **ISO/IEC/IEEE 15289:2019** | Norma principal — define o conteúdo dos itens de documentação |
| **ISO/IEC/IEEE 12207:2017** | Estabelece a documentação como parte do ciclo de vida do software |
| **ISO/IEC/IEEE 26514:2022** | Orienta a estrutura e o conteúdo da documentação de usuário |

Um critério atravessa toda a documentação: **nada é registrado sem fonte confirmada**. Cada informação tem origem rastreável no código-fonte, em documentos de projeto, no material de design ou em registros de reunião — e, quando algo não pode ser confirmado, registra-se uma pendência explícita em vez de uma suposição.

---

## Créditos

Documentação produzida por **Ithalo Cavalcante Gomes**, estudante de Tecnologia em Análise e Desenvolvimento de Sistemas, como subprojeto do projeto IFVest — **IFSP Campus Jacareí**.
