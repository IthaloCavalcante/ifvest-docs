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
    Component(rotas, "Camada de Rotas", "FastAPI Routers", "auth · users · features · question_bank\nmocktests · essays · quiz · admin")
    Component(seguranca, "Segurança", "security.py · firebase.py", "Extrai e verifica o token,\nidentifica o usuário")
    Component(permissoes, "Permissões", "permission_catalog.py\npermissions.py", "Catálogo das permissões, atribuição\ninicial e autorização de cada ação")
    Component(flags, "Feature Flags", "feature_guard.py\nfeature_flags_service.py", "Liga e desliga módulos\ne funcionalidades")
    Component(servicos, "Serviços de Domínio", "quiz · mocktests · essays · admin\nquestion_editing · seed", "Regras de negócio de cada módulo")
    Component(esquemas, "Esquemas", "Pydantic", "Valida entradas e formata\nas respostas da API")
    Component(modelos, "Modelos", "SQLAlchemy 2.0", "Mapeamento das 24 tabelas\ndo banco de dados")
}

ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Persistência")
System_Ext(firebase, "Firebase Authentication", "Verificação de tokens")

Rel_D(web, rotas, "Requisições REST\ncom token", "HTTPS")

Rel_D(rotas, flags, "Verifica se o módulo\nestá ativo")
Rel_D(rotas, seguranca, "Identifica o usuário")
Rel_D(rotas, permissoes, "Verifica a permissão exigida")
Rel_D(rotas, esquemas, "Valida e serializa")
Rel_D(rotas, servicos, "Delega a regra de negócio")

Rel_R(seguranca, firebase, "Verifica a assinatura\ndo token", "SDK Admin")
Rel_D(seguranca, modelos, "Carrega o usuário\ne suas permissões")
Rel_D(flags, modelos, "Lê o estado das flags")
Rel_D(servicos, modelos, "Lê e escreve dados")
Rel_D(modelos, db, "Consultas assíncronas", "asyncpg / SQL")

SHOW_LEGEND()
@enduml
```

---

## API — Rotas e Serviços

Cada módulo da plataforma tem suas rotas e seus serviços. As rotas recebem e validam a requisição e **delegam a regra de negócio aos serviços**; as de sessão e de usuários, mais simples, e alguns trechos das rotas do quiz consultam o banco diretamente.

```plantuml
@startuml C4_Componentes_API_Dominios
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — API IFVest (C4 L3 · Rotas e Serviços)

LAYOUT_LEFT_RIGHT()

Container_Boundary(api, "API — FastAPI") {
    Component(r_quiz, "Rotas de Quiz", "quiz.py · 18 rotas", "Partidas, pergunta do dia,\nfiltros, ranking, loja e histórico")
    Component(r_mock, "Rotas de Simulados", "mocktests.py · 12 rotas", "Montagem, resolução\ne correção de simulados")
    Component(r_bank, "Rotas do Banco de Questões", "question_bank.py · 5 rotas", "Busca, cadastro, edição\ne denúncia de questões")
    Component(r_essays, "Rotas de Redação", "essays.py · 11 rotas", "Propostas, redações\ne correções")
    Component(r_admin, "Rotas de Administração", "admin.py · 3 rotas", "Painel de indicadores\ne moderação das denúncias")
    Component(r_feat, "Rotas de Flags", "features.py · 3 rotas", "Consulta e alteração\ndas feature flags")
    Component(r_users, "Rotas de Usuário", "users.py · 6 rotas", "Perfil, lista de usuários\ne permissões")
    Component(r_auth, "Rotas de Sessão", "auth.py · 2 rotas", "Login e dados\ndo usuário atual")

    Component(s_quiz, "Serviços do Quiz", "quiz_service.py e módulos quiz_*\nstore_catalog.py · daily_streak.py", "Partidas, pontuação, ranking,\nloja e sequência diária")
    Component(s_mock, "Serviço de Simulados", "mocktests_service.py", "Montagem e correção dos\nsimulados; busca e cadastro de questões")
    Component(s_edit, "Edição de Questões", "question_editing.py", "Leitura com gabarito\ne edição de questões")
    Component(s_essays, "Serviço de Redação", "essays_service.py", "Propostas e correção por\ncompetências do ENEM")
    Component(s_admin, "Serviço de Administração", "admin_service.py", "Indicadores, denúncias\ne registro de auditoria")
    Component(s_flags, "Serviço de Flags", "feature_flags_service.py", "Estado e hierarquia\ndas flags")
    Component(s_seed, "Serviços de Carga", "seed_service.py\nunicamp_seed_service.py", "Dados de teste e\ncarga das provas")
}

ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Persistência")

Rel_R(r_quiz, s_quiz, "Delega")
Rel_R(r_mock, s_mock, "Delega")
Rel_R(r_bank, s_mock, "Busca e cadastro")
Rel_R(r_bank, s_edit, "Edição")
Rel_R(r_bank, s_admin, "Denúncias")
Rel_R(r_essays, s_essays, "Delega")
Rel_R(r_admin, s_admin, "Delega")
Rel_R(r_feat, s_flags, "Delega")

Rel_D(s_quiz, db, "Lê e escreve", "SQL")
Rel_D(s_mock, db, "Lê e escreve", "SQL")
Rel_D(s_edit, db, "Lê e escreve", "SQL")
Rel_D(s_essays, db, "Lê e escreve", "SQL")
Rel_D(s_admin, db, "Lê e escreve", "SQL")
Rel_D(s_flags, db, "Lê e escreve", "SQL")
Rel_D(s_seed, db, "Popula", "SQL")
Rel_D(r_users, db, "Lê e escreve", "SQL")
Rel_D(r_auth, db, "Busca e cria usuários", "SQL")

SHOW_LEGEND()
@enduml
```

O **Serviço de Administração** também guarda o registro de auditoria: as rotas que cadastram e editam questões, mexem em propostas de redação, concedem ou revogam permissões e alteram módulos registram ali o que foi feito. Os **Serviços de Carga** não são chamados por rotas: rodam por scripts, para popular o ambiente de desenvolvimento ou carregar provas no banco de produção.

---

## API — Componentes Transversais

A guarda dos módulos, a segurança e as permissões atuam **antes** de qualquer regra de negócio. Nas rotas de um módulo, a requisição passa pelos três, nesta ordem:

```plantuml
@startuml C4_Componentes_API_Transversais
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — API IFVest (C4 L3 · Componentes Transversais)

LAYOUT_LEFT_RIGHT()

Container(web, "Aplicação Web", "React", "Envia o token\nem cada requisição")

Container_Boundary(api, "API — FastAPI") {
    Component(guarda, "Guarda dos Módulos", "feature_guard.py\nfeature_flags_service.py", "Recusa com 503 as chamadas\na módulos desligados,\nrespeitando a hierarquia")
    Component(seguranca, "Segurança", "security.py", "Extrai o token do cabeçalho\ne resolve o usuário atual")
    Component(fb, "Integração Firebase", "firebase.py", "Verifica a assinatura\ndo token de identidade")
    Component(permissoes, "Permissões", "permission_catalog.py\npermissions.py", "Confere a permissão\nexigida pela rota")
    Component(rotas, "Camada de Rotas", "FastAPI Routers", "Executa a ação solicitada")
}

System_Ext(firebase, "Firebase Authentication", "Serviço de identidade")
ContainerDb(db, "Banco de Dados", "PostgreSQL 16", "Usuários, permissões\ne estado das flags")

Rel_R(web, guarda, "1. Requisição com token", "HTTPS")
Rel_R(guarda, seguranca, "2. Módulo ativo")
Rel_D(seguranca, fb, "Solicita a verificação")
Rel_D(fb, firebase, "Valida o token", "SDK Admin")
Rel_R(seguranca, permissoes, "3. Usuário identificado")
Rel_R(permissoes, rotas, "4. Permissão confirmada")
Rel_D(guarda, db, "Lê o estado das flags", "SQL")
Rel_D(seguranca, db, "Carrega o usuário\ne suas permissões", "SQL")

SHOW_LEGEND()
@enduml
```

Quando a rota pertence a uma funcionalidade com flag própria — o ranking do quiz ou a correção de redações, por exemplo —, essa flag é conferida por último, depois da permissão. As rotas que não pertencem a um módulo — sessão, usuários, flags, administração e banco de questões — não passam pela guarda dos módulos.

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
    Component(router, "Roteador", "React Router 7", "Define as rotas e aplica o\ncontrole de módulos a cada tela")
    Component(layout, "Layout", "core/layout", "Estrutura visual comum\na todas as telas")

    Component(f_home, "Início", "features/home", "Página inicial e navegação\nentre os módulos")
    Component(f_quiz, "Quiz", "features/quiz", "Partidas, pergunta do dia,\nranking e loja")
    Component(f_mock, "Simulados", "features/mocktests", "Criação e resolução\nde simulados")
    Component(f_essays, "Redação", "features/essays", "Envio de redações,\ncorreção e consulta")
    Component(f_prof, "Área do Professor", "features/professor", "Banco de questões, propostas\nde redação e fila de correção")
    Component(f_admin, "Painel Administrativo", "features/admin", "Indicadores, permissões,\nmoderação e módulos")
    Component(f_auth, "Autenticação e Perfil", "features/auth", "Entrada com a conta Google\ne perfil do usuário")
    Component(f_dev, "Em Desenvolvimento", "features/underDevelopment", "Tela exibida no lugar dos\nmódulos desligados")

    Component(c_api, "Cliente HTTP", "core/api", "Chamadas à API com o token,\npor caminhos relativos")
    Component(c_auth, "Sessão", "core/auth", "Integração com o Firebase,\nsessão e permissões")
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
Rel_D(layout, f_prof, "Exibe")
Rel_D(layout, f_admin, "Exibe")
Rel_D(layout, f_auth, "Exibe")

Rel_D(f_quiz, c_api, "Usa")
Rel_D(f_mock, c_api, "Usa")
Rel_D(f_essays, c_api, "Usa")
Rel_D(f_prof, c_api, "Usa")
Rel_D(f_admin, c_api, "Usa")
Rel_D(f_auth, c_auth, "Usa")

Rel_R(c_auth, firebase, "Autentica", "SDK / HTTPS")
Rel_D(c_api, api, "Requisições REST\ncom token", "HTTPS")

SHOW_LEGEND()
@enduml
```

---

## Leitura dos diagramas

**A ordem das verificações importa.** Nas rotas de um módulo, a primeira verificação é se ele está ligado: um módulo desligado responde 503 antes mesmo de identificar o usuário. Depois vêm a identificação, a permissão exigida e, quando houver, a flag da funcionalidade específica. Uma permissão válida não basta se o módulo estiver desligado.

**O controle de módulos acontece nas duas pontas.** O frontend oculta as telas dos módulos desligados, exibindo a página de "em desenvolvimento"; o backend recusa as chamadas correspondentes. A verificação no navegador é conveniência, não segurança: quem chamar a API diretamente continua sendo barrado. A exceção é o painel administrativo, cuja flag é conferida só no frontend — as rotas de administração continuam exigindo a permissão de administrador.

**O roteador não exige sessão.** Qualquer tela pode ser aberta sem login, mas os dados dependem da API, que recusa as chamadas às rotas protegidas.

**Os módulos do frontend espelham os domínios da API.** Quiz, simulados, redação e administração existem dos dois lados, e a Área do Professor reúne, numa só tela, as rotas do banco de questões e das propostas e correções de redação.

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Componentes da API e contagem de rotas | `ifvest-backend/src/` e especificação OpenAPI gerada do código | set/2026 |
| Componentes transversais e ordem das verificações | `src/core/feature_guard.py`, `security.py`, `firebase.py`, `permission_catalog.py`, `permissions.py` e `src/services/feature_flags_service.py`; ordem conferida executando a API | set/2026 |
| Componentes do frontend | `ifvest-frontend/src/core/`, `src/features/` e `src/router/` | set/2026 |
