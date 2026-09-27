# C4 — Nível 2: Contêineres

Detalha os contêineres que compõem o IFVest, as escolhas tecnológicas de cada um e como se comunicam entre si. É o primeiro nível técnico do modelo C4.

**Público-alvo:** desenvolvedores, arquitetos de software e equipes de operações.

!!! note "O que é um contêiner neste contexto"
    Um contêiner é qualquer unidade separadamente executável ou implantável — a aplicação que roda no navegador, a API, o banco de dados, o proxy reverso. No IFVest, cada um corresponde a um container Docker em produção.

---

## Visão Completa

Visão unificada de todos os contêineres e suas conexões. Use como referência geral; para leitura detalhada, consulte as seções abaixo.

```plantuml
@startuml C4_Container_IFVest_Completo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 Nível 2 · Visão Completa)

LAYOUT_TOP_DOWN()

Person(estudante, "Estudante", "Resolve questões, simulados\ne envia redações")
Person(educador, "Educador", "Cria questões, simulados\ne propostas de redação")
Person(admin, "Administrador", "Gerencia permissões,\nconteúdo e módulos")

System_Boundary(ifvest, "IFVest — VPS única") {
    Container(caddy, "Proxy Reverso", "Caddy 2", "Único ponto de entrada. Termina o TLS,\nemite o certificado e roteia por caminho")
    Container(web, "Aplicação Web", "React 19 + TypeScript + Vite\nservida por nginx", "Interface do usuário, executada no navegador.\nArquivos estáticos, sem renderização no servidor")
    Container(api, "API", "Python 3.12 + FastAPI", "Regras de negócio, autorização por permissões\ne controle dos módulos ativos")
    ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Usuários, permissões, taxonomia, questões,\nsimulados, redações e gamificação")
    Container(arquivos, "Armazenamento de Arquivos", "Volume Docker", "Imagens das questões, servidas pela API")
}

System_Ext(firebase, "Firebase Authentication", "Autentica usuários\ne emite tokens")

Rel_D(estudante, caddy, "Usa a plataforma", "HTTPS")
Rel_D(educador, caddy, "Cria e gerencia conteúdo", "HTTPS")
Rel_D(admin, caddy, "Administra a plataforma", "HTTPS")

Rel_D(caddy, web, "Encaminha os demais caminhos", "HTTP interno")
Rel_D(caddy, api, "Encaminha /api, /static,\n/imgs e /health", "HTTP interno")

Rel_R(web, firebase, "Autentica o usuário", "SDK / HTTPS")
Rel_D(web, caddy, "Requisições à API,\nmesma origem", "REST / HTTPS")

Rel_D(api, db, "Lê e escreve dados", "SQL assíncrono\n(SQLAlchemy / asyncpg)")
Rel_R(api, arquivos, "Lê e grava imagens\ndas questões", "Sistema de arquivos")
Rel_R(api, firebase, "Verifica a assinatura\ndos tokens", "SDK Admin / HTTPS")

SHOW_LEGEND()
@enduml
```

---

## Visão Interna — Roteamento por Caminho

Como frontend e API compartilham o mesmo domínio, o proxy reverso decide o destino de cada requisição pelo início do caminho. Essa escolha elimina a necessidade de CORS no navegador.

```plantuml
@startuml C4_Container_IFVest_Roteamento
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 L2 · Roteamento por Caminho)

LAYOUT_LEFT_RIGHT()

Person(usuario, "Usuário", "Qualquer perfil da plataforma")

System_Boundary(ifvest, "IFVest — VPS única") {
    Container(caddy, "Proxy Reverso", "Caddy 2", "Única porta publicada:\n80 e 443")
    Container(web, "Aplicação Web", "nginx + build do Vite", "Assume o roteamento das telas\nno próprio navegador")
    Container(api, "API", "FastAPI", "Endpoints, arquivos estáticos\ne verificação de disponibilidade")
    ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Sem porta exposta:\nexiste apenas na rede interna")
}

Rel_R(usuario, caddy, "ifvest.com.br", "HTTPS")
Rel_R(caddy, api, "/api/* · /static/* · /imgs/* · /health", "HTTP interno")
Rel_D(caddy, web, "qualquer outro caminho", "HTTP interno")
Rel_D(api, db, "Conexão interna", "SQL")

SHOW_LEGEND()
@enduml
```

---

## Autenticação entre Contêineres

A identidade do usuário é responsabilidade do Firebase; a autorização é responsabilidade da API. Os dois papéis não se misturam.

```plantuml
@startuml C4_Container_IFVest_Auth
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 L2 · Autenticação)

LAYOUT_LEFT_RIGHT()

Person(usuario, "Usuário", "Qualquer perfil da plataforma")

System_Boundary(ifvest, "IFVest") {
    Container(web, "Aplicação Web", "React + Firebase SDK", "Obtém o token e o envia\nem cada requisição")
    Container(api, "API", "FastAPI + firebase-admin", "Verifica o token e carrega\nas permissões do usuário")
    ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Guarda os usuários\ne suas permissões")
}

System_Ext(firebase, "Firebase Authentication", "E-mail e senha\nou conta Google")

Rel_R(usuario, web, "Informa credenciais", "HTTPS")
Rel_R(web, firebase, "Solicita autenticação", "SDK / HTTPS")
Rel_L(firebase, web, "Devolve o token\nde identidade", "HTTPS")
Rel_D(web, api, "Requisição com o token\nno cabeçalho Authorization", "REST / HTTPS")
Rel_R(api, firebase, "Verifica a assinatura\ndo token", "SDK Admin / HTTPS")
Rel_D(api, db, "Busca o usuário\ne suas permissões", "SQL")

SHOW_LEGEND()
@enduml
```

---

## Implantação

Os quatro contêineres são orquestrados por Docker Compose em uma VPS única. **Apenas o proxy reverso publica portas** — API e banco existem somente na rede interna.

| Contêiner | Imagem | Portas publicadas |
|---|---|---|
| Proxy reverso | Caddy 2 | **80 e 443** |
| Aplicação web | nginx | nenhuma |
| API | Python 3.12 | nenhuma |
| Banco de dados | PostgreSQL 16 | nenhuma |

Detalhes de implantação, backup e segurança em [Arquitetura do Sistema](../arquitetura.md#topologia-de-producao).

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Contêineres, imagens e rede | `deploy/docker-compose.prod.yml` | set/2026 |
| Roteamento por caminho e TLS | `deploy/Caddyfile` | set/2026 |
| Tecnologias de cada contêiner | `requirements.txt`, `package.json` e Dockerfiles | set/2026 |
| Fluxo de autenticação | `ifvest-backend/src/core/` e `ifvest-frontend/src/core/auth/` | set/2026 |
