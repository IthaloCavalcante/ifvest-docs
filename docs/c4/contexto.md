# C4 — Nível 1: Contexto

Mostra o IFVest como uma caixa única, os perfis de usuário que interagem com ele e os sistemas externos com os quais se comunica. Não há detalhes técnicos internos neste nível.

**Público-alvo:** qualquer pessoa — técnica ou não.

---


```plantuml
@startuml C4_Contexto_IFVest
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title Diagrama de Contexto — IFVest (C4 Nível 1)

LAYOUT_LEFT_RIGHT()

Person(aluno, "Aluno", "Estudante que se prepara\npara vestibulares e ENEM")
Person(professor, "Professor", "Docente responsável pela criação\ne curadoria de conteúdo educacional")
Person(admin, "Administrador", "Responsável técnico pela\nadministração e moderação da plataforma")

System(ifvest, "IFVest", "Plataforma gratuita de preparação\npara vestibulares do IFSP Campus Jacareí")

System_Ext(enem_api, "enem.dev", "API pública com questões\nreais do ENEM (2009–2023)")
System_Ext(fuvest_api, "API FUVEST", "Provedor de questões da FUVEST\npara vestibulares")
System_Ext(unicamp_api, "API UNICAMP", "Provedor de questões da UNICAMP\npara vestibulares")

Rel_R(aluno, ifvest, "Realiza simulados, revisão,\nquizzes e flashcards")
Rel_R(professor, ifvest, "Cria questões, simulados,\nmateriais e flashcards")
Rel_R(admin, ifvest, "Gerencia usuários e\nconteúdo da plataforma")

Rel_R(ifvest, enem_api, "Carrega questões do ENEM\npara o módulo IFQuiz", "REST/HTTPS")
Rel_R(ifvest, fuvest_api, "Carregará questões\nda FUVEST", "REST/HTTPS")
Rel_R(ifvest, unicamp_api, "Carregará questões\nda UNICAMP", "REST/HTTPS")

SHOW_LEGEND()
@enduml
```
