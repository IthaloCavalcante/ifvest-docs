# C4 — Nível 1: Contexto

Mostra o IFVest como uma caixa única, os perfis de usuário que interagem com ele e os sistemas externos com os quais se comunica. Não há detalhes técnicos internos neste nível.

**Público-alvo:** qualquer pessoa — técnica ou não.

!!! note "Sobre os perfis representados"
    O IFVest não organiza usuários em cargos fixos: a autorização é feita por [permissões granulares](../arquitetura.md#permissoes). Os perfis abaixo representam **conjuntos de permissões** típicos, e não categorias rígidas do sistema.

---

```plantuml
@startuml C4_Contexto_IFVest
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

title Diagrama de Contexto — IFVest (C4 Nível 1)

LAYOUT_LEFT_RIGHT()

Person(estudante, "Estudante", "Prepara-se para o ENEM e vestibulares\nresolvendo questões, simulados e redações")
Person(educador, "Educador", "Cadastra e cura questões, monta simulados\ne publica propostas de redação")
Person(corretor, "Corretor", "Avalia redações segundo as\ncompetências do ENEM")
Person(admin, "Administrador", "Gerencia permissões, modera as questões\ne controla os módulos ativos")

System(ifvest, "IFVest", "Plataforma gratuita de preparação para o ENEM\ne vestibulares do IFSP Campus Jacareí")

System_Ext(firebase, "Firebase Authentication", "Serviço de identidade do Google:\nautentica usuários e emite tokens")

System_Ext(leitor_pdf, "Leitor de PDFs Educacionais", "Aplicativo de leitura de materiais\nem PDF no dispositivo do estudante")
System_Ext(extrator, "Extrator de Questões por IA", "Sistema que lê provas anteriores em PDF\ne extrai as questões estruturadas")

Rel_R(estudante, ifvest, "Estuda, resolve questões\ne envia redações", "HTTPS")
Rel_R(educador, ifvest, "Cadastra questões, simulados\ne propostas de redação", "HTTPS")
Rel_R(corretor, ifvest, "Corrige redações e\nregistra devolutivas", "HTTPS")
Rel_R(admin, ifvest, "Administra permissões,\nmoderação e módulos", "HTTPS")

Rel_R(estudante, firebase, "Entra com a\nconta Google", "HTTPS")
Rel_R(ifvest, firebase, "Verifica a autenticidade\ndos tokens recebidos", "SDK Admin / HTTPS")

Rel_R(ifvest, leitor_pdf, "Exportará materiais\nem PDF", "A definir")
Rel_R(extrator, ifvest, "Alimentará o banco\nde questões", "A definir")

SHOW_LEGEND()
@enduml
```

---

## Leitura do diagrama

**Os quatro perfis** acessam a mesma aplicação web; o que muda entre eles são as permissões que cada conta possui. Um mesmo usuário pode acumular permissões de mais de um perfil.

**A autenticação acontece fora da plataforma.** O usuário entra com a conta Google diretamente no Firebase, que devolve um token; o IFVest recebe esse token e apenas verifica sua autenticidade. A plataforma nunca manipula senhas. O diagrama liga ao Firebase só o estudante, para não sobrecarregar o desenho, mas todos os perfis entram da mesma forma.

**As duas integrações previstas** — o leitor de PDFs e o extrator de questões — aparecem com relações em tempo futuro porque **ainda não existem no código**. Estão representadas por pertencerem ao ecossistema do projeto e por terem impacto direto sobre a plataforma quando forem implementadas. Hoje, as provas entram no banco por uma carga de arquivos executada pela equipe no servidor, sem vínculo registrado com o extrator (ver [Arquitetura — Carga do banco de questões](../arquitetura.md#carga-do-banco-de-questoes)).

⬜ *A atualizar quando as integrações forem implementadas, substituindo o protocolo "A definir" pelo mecanismo efetivo.*

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Perfis e permissões | `ifvest-backend/src/core/permission_catalog.py` e `permissions.py` | set/2026 |
| Autenticação e verificação de tokens | `ifvest-backend/src/core/firebase.py` e `src/core/security.py`; `ifvest-frontend/src/core/auth/` | set/2026 |
| Integrações previstas | Documento de onboarding do projeto | set/2026 |
| Carga atual das provas | `docs/atualizar-questoes-na-vps.md` do `ifvest-monorepo` | set/2026 |
