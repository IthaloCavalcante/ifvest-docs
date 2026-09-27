# C4 — Nível 3: Componentes

Abre os contêineres **API** e **Aplicação Web** e mostra seus módulos internos: como as responsabilidades estão distribuídas, como os domínios se organizam e como se comunicam com a camada de dados e os serviços externos.

!!! info "Público-alvo"
    Desenvolvedores que trabalham ou vão trabalhar diretamente no código do IFVest. É o nível mais técnico dos três diagramas.

---

## API — Visão Completa

Visão unificada dos componentes da API. Use como referência geral; para leitura detalhada, consulte as seções abaixo.

```plantuml
@startuml C4_Componentes_API_Completo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — API IFVest (C4 Nível 3 · Visão Completa)

LAYOUT_TOP_DOWN()

Container(web, "Aplicação Web", "React + Vite", "Consome a API")

Container_Boundary(api, "API — FastAPI") {
    Component(rotas, "Camada de Rotas", "FastAPI Routers", "auth · users · quiz · mocktests\nessays · features")
    Component(seguranca, "Segurança", "security.py · firebase.py", "Extrai e verifica o token,\nidentifica o usuário")
    Component(permissoes, "Permissões", "permissions.py", "Atribui as permissões iniciais e\nautoriza cada ação")
    Component(flags, "Feature Flags", "feature_flags_service.py", "Liga e desliga módulos\ne funcionalidades")
    Component(servicos, "Serviços de Domínio", "quiz · mocktests · essays\nseed · unicamp_seed", "Regras de negócio de cada módulo")
    Component(esquemas, "Esquemas", "Pydantic", "Valida entradas e formata\nas respostas da API")
    Component(modelos, "Modelos", "SQLAlchemy 2.0", "Mapeamento das 22 tabelas\ndo banco de dados")
}

ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Persistência")
System_Ext(firebase, "Firebase Authentication", "Verificação de tokens")

Rel_D(web, rotas, "Requisições REST\ncom token", "HTTPS")

Rel_D(rotas, seguranca, "Identifica o usuário")
Rel_D(rotas, permissoes, "Verifica a permissão exigida")
Rel_D(rotas, flags, "Verifica se o módulo\nestá ativo")
Rel_D(rotas, esquemas, "Valida e serializa")
Rel_D(rotas, servicos, "Delega a regra de negócio")

Rel_R(seguranca, firebase, "Verifica a assinatura\ndo token", "SDK Admin")
Rel_D(seguranca, modelos, "Carrega o usuário")
Rel_D(permissoes, modelos, "Lê as permissões\ndo usuário")
Rel_D(flags, modelos, "Lê o estado das flags")
Rel_D(servicos, modelos, "Lê e escreve dados")
Rel_D(modelos, db, "Consultas assíncronas", "asyncpg / SQL")

SHOW_LEGEND()
@enduml
```

---

## API — Rotas e Serviços

Cada módulo da plataforma tem sua rota e seu serviço correspondente. **As rotas não acessam o banco diretamente**: recebem e validam a requisição, e delegam a regra de negócio ao serviço.

```plantuml
@startuml C4_Componentes_API_Dominios
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — API IFVest (C4 L3 · Rotas e Serviços)

LAYOUT_LEFT_RIGHT()

Container_Boundary(api, "API — FastAPI") {
    Component(r_quiz, "Rotas de Quiz", "quiz.py · 17 rotas", "Partidas, pergunta do dia,\nranking, loja e histórico")
    Component(r_mock, "Rotas de Simulados", "mocktests.py · 14 rotas", "Questões, simulados\ne tentativas")
    Component(r_essays, "Rotas de Redação", "essays.py · 11 rotas", "Propostas, redações\ne correções")
    Component(r_users, "Rotas de Usuário", "users.py · 4 rotas", "Perfil do usuário")
    Component(r_feat, "Rotas de Flags", "features.py · 3 rotas", "Consulta e alteração\ndas feature flags")
    Component(r_auth, "Rotas de Sessão", "auth.py · 2 rotas", "Sessão do usuário")

    Component(s_quiz, "Serviço de Quiz", "quiz_service.py", "Pontuação, ofensiva diária\ne gamificação")
    Component(s_mock, "Serviço de Simulados", "mocktests_service.py", "Montagem e correção\ndos simulados")
    Component(s_essays, "Serviço de Redação", "essays_service.py", "Propostas e correção por\ncompetências do ENEM")
    Component(s_seed, "Serviços de Carga", "seed_service.py\nunicamp_seed_service.py", "Carga inicial de dados\ne de questões")
}

ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Persistência")

Rel_R(r_quiz, s_quiz, "Delega")
Rel_R(r_mock, s_mock, "Delega")
Rel_R(r_essays, s_essays, "Delega")

Rel_D(s_quiz, db, "Lê e escreve", "SQL")
Rel_D(s_mock, db, "Lê e escreve", "SQL")
Rel_D(s_essays, db, "Lê e escreve", "SQL")
Rel_D(s_seed, db, "Popula", "SQL")
Rel_D(r_users, db, "Lê e escreve", "SQL")
Rel_D(r_feat, db, "Lê e escreve", "SQL")

SHOW_LEGEND()
@enduml
```

---

## API — Componentes Transversais

Segurança, permissões e feature flags atuam **antes** de qualquer regra de negócio: toda requisição a uma rota protegida passa pelos três.

```plantuml
@startuml C4_Componentes_API_Transversais
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — API IFVest (C4 L3 · Componentes Transversais)

LAYOUT_LEFT_RIGHT()

Container(web, "Aplicação Web", "React", "Envia o token\nem cada requisição")

Container_Boundary(api, "API — FastAPI") {
    Component(seguranca, "Segurança", "security.py", "Extrai o token do cabeçalho\ne resolve o usuário atual")
    Component(fb, "Integração Firebase", "firebase.py", "Verifica a assinatura\ndo token de identidade")
    Component(permissoes, "Permissões", "permissions.py", "Atribui permissões iniciais\npor domínio de e-mail e\nautoriza cada ação")
    Component(flags, "Feature Flags", "feature_flags_service.py", "Recusa chamadas a módulos\ndesligados, respeitando a\nhierarquia entre eles")
    Component(rotas, "Camada de Rotas", "FastAPI Routers", "Executa a ação solicitada")
}

System_Ext(firebase, "Firebase Authentication", "Serviço de identidade")
ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Usuários, permissões\ne estado das flags")

Rel_R(web, seguranca, "Requisição com token", "HTTPS")
Rel_R(seguranca, fb, "Solicita a verificação")
Rel_D(fb, firebase, "Valida o token", "SDK Admin")
Rel_R(seguranca, permissoes, "Usuário identificado")
Rel_R(permissoes, flags, "Permissão confirmada")
Rel_R(flags, rotas, "Módulo ativo")
Rel_D(permissoes, db, "Lê permissões", "SQL")
Rel_D(flags, db, "Lê o estado das flags", "SQL")

SHOW_LEGEND()
@enduml
```

---

## Aplicação Web — Componentes

O frontend separa a **infraestrutura compartilhada**, em `core/`, dos **módulos da plataforma**, em `features/`. Cada módulo tem suas próprias telas, componentes e testes.

```plantuml
@startuml C4_Componentes_Frontend
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — Aplicação Web IFVest (C4 Nível 3)

LAYOUT_TOP_DOWN()

Person(usuario, "Usuário", "Qualquer perfil")

Container_Boundary(web, "Aplicação Web — React + Vite") {
    Component(router, "Roteador", "React Router 7", "Define as rotas e protege\nas telas que exigem sessão")
    Component(layout, "Layout", "core/layout", "Estrutura visual comum\na todas as telas")

    Component(f_home, "Início", "features/home", "Página inicial e navegação\nentre os módulos")
    Component(f_quiz, "Quiz", "features/quiz", "Partidas, pergunta do dia,\nranking e loja")
    Component(f_mock, "Simulados", "features/mocktests", "Criação e resolução\nde simulados")
    Component(f_essays, "Redação", "features/essays", "Envio de redações\ne consulta às correções")
    Component(f_admin, "Administração", "features/admin", "Permissões, conteúdo\ne feature flags")
    Component(f_auth, "Autenticação", "features/auth", "Cadastro e entrada")
    Component(f_dev, "Em Desenvolvimento", "features/underDevelopment", "Tela exibida no lugar dos\nmódulos desligados")

    Component(c_api, "Cliente HTTP", "core/api", "Chamadas à API com o token,\npor caminhos relativos")
    Component(c_auth, "Sessão", "core/auth", "Integração com o Firebase\ne estado da sessão")
    Component(c_feat, "Feature Flags", "core/features", "Consulta as flags e oculta\nos módulos desligados")
}

Container(api, "API", "FastAPI", "Regras de negócio")
System_Ext(firebase, "Firebase Authentication", "Serviço de identidade")

Rel_D(usuario, router, "Navega", "HTTPS")
Rel_D(router, layout, "Renderiza dentro de")
Rel_D(router, c_feat, "Consulta antes\nde exibir o módulo")
Rel_D(c_feat, f_dev, "Módulo desligado")

Rel_D(layout, f_home, "Exibe")
Rel_D(layout, f_quiz, "Exibe")
Rel_D(layout, f_mock, "Exibe")
Rel_D(layout, f_essays, "Exibe")
Rel_D(layout, f_admin, "Exibe")
Rel_D(layout, f_auth, "Exibe")

Rel_D(f_quiz, c_api, "Usa")
Rel_D(f_mock, c_api, "Usa")
Rel_D(f_essays, c_api, "Usa")
Rel_D(f_admin, c_api, "Usa")
Rel_D(f_auth, c_auth, "Usa")

Rel_R(c_auth, firebase, "Autentica", "SDK / HTTPS")
Rel_D(c_api, api, "Requisições REST\ncom token", "HTTPS")

SHOW_LEGEND()
@enduml
```

---

## Leitura dos diagramas

**A ordem das verificações importa.** Uma requisição a uma rota protegida passa por identificação do usuário, verificação da permissão exigida e verificação do módulo ativo — nessa ordem — antes de chegar à regra de negócio. Uma permissão válida não basta se o módulo estiver desligado.

**O controle de módulos acontece nas duas pontas.** O frontend oculta as telas dos módulos desligados, exibindo a página de "em desenvolvimento"; o backend recusa as chamadas correspondentes. A verificação no navegador é conveniência, não segurança: quem chamar a API diretamente continua sendo barrado.

**Os módulos do frontend espelham os domínios da API.** Quiz, simulados, redação e administração existem dos dois lados, o que mantém a correspondência entre as telas e os endpoints que as alimentam.

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Componentes da API e contagem de rotas | `ifvest-backend/src/` e especificação OpenAPI gerada do código | set/2026 |
| Componentes transversais | `src/core/security.py`, `firebase.py`, `permissions.py` e `src/services/feature_flags_service.py` | set/2026 |
| Componentes do frontend | `ifvest-frontend/src/core/` e `src/features/` | set/2026 |
