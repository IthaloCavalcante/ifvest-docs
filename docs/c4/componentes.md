# Nível 3 — Componentes

O diagrama de componentes abre o contêiner **Aplicação Web (Node.js + Express)** e mostra seus módulos internos: como as responsabilidades estão distribuídas, como os domínios se organizam e como se comunicam com a camada de dados e os sistemas externos.

!!! info "Público-alvo"
    Desenvolvedores que trabalham ou vão trabalhar diretamente no código do IFVest. É o nível mais técnico dos três diagramas.

---

## Visão Completa

Visão unificada de todos os componentes e suas conexões. Use como referência geral; para leitura detalhada, consulte as seções abaixo.

```plantuml
@startuml C4_Componentes_IFVest_Completo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — Aplicação Web IFVest (C4 Nível 3 · Visão Completa)

LAYOUT_TOP_DOWN()

Person(aluno, "Aluno", "Estudante que se prepara\npara vestibulares e ENEM")
Person(professor, "Professor", "Docente responsável pela criação\ne curadoria de conteúdo educacional")
Person(admin, "Administrador", "Responsável técnico pela\nadministração e moderação da plataforma")

Container_Ext(editor, "Editor Markdown", "React + Vite (SPA)", "Editor de conteúdo interativo.\nExecuta no navegador do usuário")
ContainerDb_Ext(database, "Banco de Dados", "MySQL", "Armazena todos os dados da plataforma")

System_Ext(enem_api, "enem.dev", "API pública com questões\nreais do ENEM (2009–2023)")
System_Ext(fuvest_api, "API FUVEST", "Provedor de questões da FUVEST\npara vestibulares")
System_Ext(unicamp_api, "API UNICAMP", "Provedor de questões da UNICAMP\npara vestibulares")

Container_Boundary(webapp, "Aplicação Web — Node.js 22.5 + Express 5.1") {
    Component(router, "Router", "routes/", "Ponto de entrada — recebe todas as requisições HTTP e distribui aos domínios")
    Component(middleware, "Middleware de Segurança", "middleware/ · Helmet · CORS · express-session · rate-limit", "Autenticação e proteção HTTP — toda requisição passa por aqui antes de chegar aos domínios")
    Component(dom_simulados, "Domínio Simulados", "domains/simulados/", "Gerencia questões e simulados. Editor Quill.js com texto rico, imagens e equações LaTeX via MathJax")
    Component(dom_revisao, "Domínio Revisão", "domains/revisao/", "Gerencia materiais de revisão por área e tópico")
    Component(dom_flashcards, "Domínio Flashcards", "domains/flashcards/", "Flashcards com lógica de repetição espaçada baseada no campo visto_por_ultimo")
    Component(dom_ifquiz, "Domínio IFQuiz", "domains/IFQuiz/", "Quiz gamificado — gerencia sessões, pontuação e placar de líderes")
    Component(dom_shared, "Domínio Compartilhado", "domains/shared/", "Componentes e utilitários reutilizados entre os domínios")
    Component(data_layer, "Camada de Dados", "models/ + validations/", "Modelos Sequelize e schemas Zod que abstraem o banco e validam os dados antes da persistência")
    Component(pdf_gen, "Gerador de PDF", "Puppeteer · modules/ ou utils/", "Exportação de simulados e gabaritos em PDF via headless Chrome server-side")
}

Rel_D(aluno, router, "Requisições HTTP", "HTTPS")
Rel_D(professor, router, "Requisições HTTP", "HTTPS")
Rel_D(admin, router, "Requisições HTTP", "HTTPS")
Rel_D(router, middleware, "Todas as requisições\npassam pelo middleware", "Express pipeline")
Rel_D(middleware, dom_simulados, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_revisao, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_flashcards, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_ifquiz, "Requisições autenticadas", "Express pipeline")
Rel_D(dom_simulados, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_revisao, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_flashcards, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_ifquiz, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_simulados, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_revisao, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_flashcards, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_ifquiz, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(data_layer, database, "Persiste e recupera dados", "SQL")
Rel_D(dom_simulados, pdf_gen, "Solicita geração de PDF\nde simulados e gabaritos", "")
Rel_R(dom_ifquiz, enem_api, "Carrega questões do ENEM\npara o módulo IFQuiz", "REST/HTTPS")
Rel_D(dom_simulados, fuvest_api, "Carregará questões\nda FUVEST", "REST/HTTPS")
Rel_D(dom_simulados, unicamp_api, "Carregará questões\nda UNICAMP", "REST/HTTPS")
Rel_R(dom_revisao, editor, "Serve o bundle\nJavaScript compilado", "HTTPS")
Rel_L(editor, dom_revisao, "Requisições de carregamento\ne salvamento de conteúdo", "REST/HTTPS, Axios")

SHOW_LEGEND()
@enduml
```

---

## Fluxo de Requisição

Mostra o caminho interno de uma requisição: da entrada pelo Router, passando pelo Middleware de Segurança, chegando aos domínios e descendo até a Camada de Dados e o Banco.

```plantuml
@startuml C4_Componentes_IFVest_Fluxo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — Fluxo de Requisição (C4 Nível 3)

LAYOUT_TOP_DOWN()

Person(aluno, "Aluno", "Estudante que se prepara\npara vestibulares e ENEM")
Person(professor, "Professor", "Docente responsável pela criação\ne curadoria de conteúdo educacional")
Person(admin, "Administrador", "Responsável técnico pela\nadministração e moderação da plataforma")

ContainerDb_Ext(database, "Banco de Dados", "MySQL", "Armazena todos os dados da plataforma")

Container_Boundary(webapp, "Aplicação Web — Node.js 22.5 + Express 5.1") {
    Component(router, "Router", "routes/", "Ponto de entrada — recebe todas as requisições HTTP e as distribui aos domínios")
    Component(middleware, "Middleware de Segurança", "middleware/ · Helmet · CORS · express-session · rate-limit", "Autenticação e proteção HTTP — toda requisição passa por aqui antes de chegar aos domínios")
    Component(dom_simulados, "Domínio Simulados", "domains/simulados/", "Gerencia questões e simulados. Editor Quill.js com texto rico, imagens e equações LaTeX via MathJax")
    Component(dom_revisao, "Domínio Revisão", "domains/revisao/", "Gerencia materiais de revisão por área e tópico")
    Component(dom_flashcards, "Domínio Flashcards", "domains/flashcards/", "Flashcards com lógica de repetição espaçada baseada no campo visto_por_ultimo")
    Component(dom_ifquiz, "Domínio IFQuiz", "domains/IFQuiz/", "Quiz gamificado — gerencia sessões, pontuação e placar de líderes")
    Component(dom_shared, "Domínio Compartilhado", "domains/shared/", "Componentes e utilitários reutilizados entre os domínios")
    Component(data_layer, "Camada de Dados", "models/ + validations/", "Modelos Sequelize e schemas Zod que abstraem o banco e validam os dados antes da persistência")
}

Rel_D(aluno, router, "Requisições HTTP", "HTTPS")
Rel_D(professor, router, "Requisições HTTP", "HTTPS")
Rel_D(admin, router, "Requisições HTTP", "HTTPS")
Rel_D(router, middleware, "Todas as requisições\npassam pelo middleware", "Express pipeline")
Rel_D(middleware, dom_simulados, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_revisao, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_flashcards, "Requisições autenticadas", "Express pipeline")
Rel_D(middleware, dom_ifquiz, "Requisições autenticadas", "Express pipeline")
Rel_D(dom_simulados, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_revisao, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_flashcards, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_ifquiz, dom_shared, "Utiliza componentes compartilhados", "")
Rel_D(dom_simulados, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_revisao, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_flashcards, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(dom_ifquiz, data_layer, "Lê e escreve dados", "Sequelize / Zod")
Rel_D(data_layer, database, "Persiste e recupera dados", "SQL")

SHOW_LEGEND()
@enduml
```

---

## Integrações e Saídas

Mostra como os domínios se comunicam com sistemas externos, o Editor Markdown e o Gerador de PDF.

```plantuml
@startuml C4_Componentes_IFVest_Integracoes
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Component.puml

title Componentes — Integrações e Saídas (C4 Nível 3)

LAYOUT_LEFT_RIGHT()

System_Ext(enem_api, "enem.dev", "API pública com questões\nreais do ENEM (2009–2023)")
System_Ext(fuvest_api, "API FUVEST", "Provedor de questões da FUVEST\npara vestibulares")
System_Ext(unicamp_api, "API UNICAMP", "Provedor de questões da UNICAMP\npara vestibulares")
Container_Ext(editor, "Editor Markdown", "React + Vite (SPA)", "Editor de conteúdo interativo.\nExecuta no navegador do usuário")

Container_Boundary(webapp, "Aplicação Web — Node.js 22.5 + Express 5.1") {
    Component(dom_simulados, "Domínio Simulados", "domains/simulados/", "Gerencia questões e simulados")
    Component(dom_revisao, "Domínio Revisão", "domains/revisao/", "Gerencia materiais de revisão por área e tópico")
    Component(dom_ifquiz, "Domínio IFQuiz", "domains/IFQuiz/", "Quiz gamificado com questões do ENEM")
    Component(pdf_gen, "Gerador de PDF", "Puppeteer · modules/ ou utils/", "Exportação de simulados e gabaritos em PDF via headless Chrome server-side")
}

Rel_R(dom_ifquiz, enem_api, "Carrega questões do ENEM\npara o módulo IFQuiz", "REST/HTTPS")
Rel_R(dom_simulados, fuvest_api, "Carregará questões\nda FUVEST", "REST/HTTPS")
Rel_R(dom_simulados, unicamp_api, "Carregará questões\nda UNICAMP", "REST/HTTPS")
Rel_R(dom_revisao, editor, "Serve o bundle\nJavaScript compilado", "HTTPS")
Rel_L(editor, dom_revisao, "Requisições de carregamento\ne salvamento de conteúdo", "REST/HTTPS, Axios")
Rel_D(dom_simulados, pdf_gen, "Solicita geração de PDF\nde simulados e gabaritos", "")

SHOW_LEGEND()
@enduml
```
