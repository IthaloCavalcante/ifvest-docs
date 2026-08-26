# C4 — Nível 2: Contêineres

Detalha os contêineres que compõem o IFVest, as escolhas tecnológicas de cada um e como se comunicam entre si. É o primeiro nível técnico do modelo C4.

**Público-alvo:** desenvolvedores, arquitetos de software e equipes de operações.

!!! note "O que é um contêiner neste contexto"
    Um contêiner é qualquer unidade separadamente executável ou implantável — a aplicação web, o editor que roda no browser, o banco de dados.

---

## Visão Completa

Visão unificada de todos os contêineres e suas conexões. Use como referência geral; para leitura detalhada, consulte as seções abaixo.

```plantuml
@startuml C4_Container_IFVest_Completo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 Nível 2 · Visão Completa)

LAYOUT_TOP_DOWN()

Person(aluno, "Aluno", "Estudante que se prepara\npara vestibulares e ENEM")
Person(professor, "Professor", "Docente responsável pela criação\ne curadoria de conteúdo educacional")
Person(admin, "Administrador", "Responsável técnico pela\nadministração e moderação da plataforma")

System_Boundary(ifvest, "IFVest") {
    Container(webapp, "Aplicação Web", "Node.js 22.5 + Express 5.1", "Renderiza páginas EJS, processa a lógica de negócio,\nexpõe a API REST e serve os assets estáticos")
    Container(editor, "Editor Markdown", "React + Vite (SPA)", "Editor de conteúdo interativo compilado como\nSingle-Page Application. Executa no navegador do usuário")
    ContainerDb(database, "Banco de Dados", "MySQL", "Armazena usuários, questões, simulados,\nflashcards e registros de desempenho")
}

System_Ext(enem_api, "enem.dev", "API pública com questões\nreais do ENEM (2009–2023)")
System_Ext(fuvest_api, "API FUVEST", "Provedor de questões da FUVEST\npara vestibulares")
System_Ext(unicamp_api, "API UNICAMP", "Provedor de questões da UNICAMP\npara vestibulares")

Rel_D(aluno, webapp, "Acessa simulados, revisão,\nIFQuiz e flashcards", "HTTPS")
Rel_D(professor, webapp, "Cria e gerencia questões,\nsimulados e flashcards", "HTTPS")
Rel_D(admin, webapp, "Administra usuários\ne conteúdo", "HTTPS")

Rel_D(webapp, database, "Lê e escreve dados via ORM", "Sequelize / SQL")
Rel_R(webapp, editor, "Serve o bundle JavaScript compilado", "HTTPS")
Rel_L(editor, webapp, "Requisições de conteúdo e salvamento", "REST / HTTPS (Axios)")

Rel_R(webapp, enem_api, "Carrega questões do ENEM\npara o IFQuiz", "REST / HTTPS")
Rel_R(webapp, fuvest_api, "Carregará questões\nda FUVEST", "REST / HTTPS")
Rel_R(webapp, unicamp_api, "Carregará questões\nda UNICAMP", "REST / HTTPS")

SHOW_LEGEND()
@enduml
```

---

## Visão Interna — Contêineres e Usuários

Mostra como os três perfis de usuário interagem com os contêineres internos da plataforma.

```plantuml
@startuml C4_Container_IFVest_Interno
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 L2 · Visão Interna)

LAYOUT_TOP_DOWN()

Person(aluno, "Aluno", "Estudante que se prepara\npara vestibulares e ENEM")
Person(professor, "Professor", "Docente responsável pela criação\ne curadoria de conteúdo educacional")
Person(admin, "Administrador", "Responsável técnico pela\nadministração e moderação da plataforma")

System_Boundary(ifvest, "IFVest") {
    Container(webapp, "Aplicação Web", "Node.js 22.5 + Express 5.1", "Renderiza páginas EJS, processa a lógica de negócio,\nexpõe a API REST e serve os assets estáticos")
    Container(editor, "Editor Markdown", "React + Vite (SPA)", "Editor de conteúdo interativo compilado como\nSingle-Page Application. Executa no navegador do usuário")
    ContainerDb(database, "Banco de Dados", "MySQL", "Armazena usuários, questões, simulados,\nflashcards e registros de desempenho")
}

Rel_D(aluno, webapp, "Acessa simulados, revisão,\nIFQuiz e flashcards", "HTTPS")
Rel_D(professor, webapp, "Cria e gerencia questões,\nsimulados e flashcards", "HTTPS")
Rel_D(admin, webapp, "Administra usuários\ne conteúdo", "HTTPS")

Rel_D(webapp, database, "Lê e escreve dados via ORM", "Sequelize / SQL")
Rel_R(webapp, editor, "Serve o bundle JavaScript compilado", "HTTPS")
Rel_L(editor, webapp, "Requisições de conteúdo e salvamento", "REST / HTTPS (Axios)")

SHOW_LEGEND()
@enduml
```

---

## Integrações Externas

Mostra como a aplicação web se conecta às APIs externas de questões.

```plantuml
@startuml C4_Container_IFVest_Externo
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml

title Contêineres — IFVest (C4 L2 · Integrações Externas)

LAYOUT_LEFT_RIGHT()

System_Boundary(ifvest, "IFVest") {
    Container(webapp, "Aplicação Web", "Node.js 22.5 + Express 5.1", "Ponto central de integração\ncom os sistemas externos")
}

System_Ext(enem_api, "enem.dev", "API pública com questões\nreais do ENEM (2009–2023)")
System_Ext(fuvest_api, "API FUVEST", "Provedor de questões da FUVEST\npara vestibulares")
System_Ext(unicamp_api, "API UNICAMP", "Provedor de questões da UNICAMP\npara vestibulares")

Rel_R(webapp, enem_api, "Carrega questões do ENEM\npara o IFQuiz", "REST / HTTPS")
Rel_R(webapp, fuvest_api, "Carregará questões\nda FUVEST", "REST / HTTPS")
Rel_R(webapp, unicamp_api, "Carregará questões\nda UNICAMP", "REST / HTTPS")

SHOW_LEGEND()
@enduml
```
