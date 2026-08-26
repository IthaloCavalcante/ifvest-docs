# Acesso e Conta

Esta página reúne as tarefas de acesso à plataforma: criar sua conta, entrar, recuperar o acesso e sair. Ela vale para **todos os perfis** — aluno e professor —; onde há diferença entre eles, ela está sinalizada no texto.

As áreas internas do IFVest são protegidas: **os módulos de estudo — Revisão, Simulados, Flashcards e IFQuiz — e a área de perfil exigem sessão ativa**. Sem ela, a plataforma leva você de volta à página inicial, de onde é possível entrar ou se cadastrar.

*Comportamento conforme o código-fonte da plataforma anterior ao redesign.*

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração pelo subprojeto de frontend e **podem mudar até a entrega**. Veja [como ler as tarefas](../index.md#como-ler-as-tarefas).

---

## Tarefa 1 — Criar uma conta

**Status:** ✅ Atual

**Objetivo:** registrar-se na plataforma para ter acesso aos módulos de estudo e ao seu histórico.

**Pré-requisitos:** um endereço de e-mail válido.

**Como fazer:**

1. Acesse a página de **cadastro** (`/cadastro`).
2. Preencha os campos obrigatórios:

    | Campo | Regra |
    |---|---|
    | **Nome completo** | mínimo de 2 caracteres |
    | **Nome de usuário** | de 3 a 30 caracteres; aceita letras, números, `_`, `.` e `-`; **deve ser único** na plataforma |
    | **E-mail** | endereço de e-mail válido |
    | **Senha** | mínimo de 8 caracteres, contendo ao menos **uma letra e um número** |
    | **Perfil** | **Usuário (aluno)** ou **Professor** — ver aviso abaixo |

3. Envie o formulário. Se algum campo não atender às regras, a plataforma indica o erro e o cadastro não é concluído.

    !!! warning "O campo Perfil define o que você poderá fazer"
        A escolha feita no cadastro determina seu acesso: **Usuário (aluno)** dá acesso aos módulos de estudo; **Professor** dá acesso aos mesmos módulos **mais** as áreas de criação e gestão de conteúdo descritas no [Guia do Professor](../professor/index.md). Um professor cadastrado como aluno não encontrará essas áreas.

        A escolha é livre no formulário: o sistema aceita qualquer uma das duas opções, sem etapa de aprovação. *(Conforme o código-fonte da plataforma anterior ao redesign.)*
4. Com o cadastro concluído, você é levado à tela de login para entrar pela primeira vez (ver [Tarefa 2](#tarefa-2-entrar-na-sua-conta)).

!!! abstract "Na versão refatorada"
    A tela de cadastro ganha o botão **"Cadastrar com Google"**, permitindo criar a conta a partir de uma conta Google, sem preencher o formulário.

    *Fonte: Relatório 1 — Maria Luiza (frontend), item 2 e fig. 3.1. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente (aguardando estabilização da interface).

**Observações:**

- Seu **nome de usuário** é o que você usará para entrar — anote-o. O e-mail não substitui o nome de usuário no login atual.

---

## Tarefa 2 — Entrar na sua conta

**Status:** ✅ Atual

**Objetivo:** iniciar uma sessão para acessar os módulos de estudo e seu histórico.

**Pré-requisitos:** ter uma conta ([Tarefa 1](#tarefa-1-criar-uma-conta)).

**Como fazer:**

1. Acesse a página de **login** (`/login`).
2. Informe seu **nome de usuário** e sua **senha**.
3. Envie o formulário. Com as credenciais corretas, você é levado à página inicial da sua conta e passa a ter acesso às áreas de estudo.
4. Se as credenciais estiverem incorretas, uma mensagem é exibida na própria tela de login e você pode tentar novamente — respeitando o limite de tentativas (ver *Observações*).

!!! abstract "Na versão refatorada"
    A tela de login ganha o botão **"Entrar com Google"**, permitindo acessar a plataforma com uma conta Google em vez de nome de usuário e senha.

    *Fonte: Relatório 1 — Maria Luiza (frontend), item 2 e fig. 3.1. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente.

**Observações:**

- **Limite de tentativas:** são permitidas **até 5 tentativas de login a cada 15 minutos** por conexão. Ao exceder esse limite, o acesso fica bloqueado temporariamente e uma mensagem informa o bloqueio — basta aguardar e tentar de novo. É uma proteção contra tentativas automatizadas de adivinhar senhas, não uma punição ao seu usuário.

---

## Tarefa 3 — Recuperar sua senha

**Status:** 🟡 Refatorado (em design)

**Objetivo:** voltar a acessar sua conta quando você não lembra a senha.

!!! warning "Disponível apenas a partir da versão refatorada"
    A plataforma atual **não possui** recuperação de senha pelo próprio aluno. Se você perdeu o acesso hoje, procure a coordenação do projeto — não há como redefinir a senha sozinho pela plataforma.

**Como funcionará (conforme o design):**

A funcionalidade **"Esqueci minha senha"** terá três etapas:

1. Informar o **e-mail vinculado à conta**;
2. Validar o **código** recebido;
3. Definir a **nova senha**.

*Fonte: Relatório 1 — Maria Luiza (frontend), item 3 e fig. 3.2. Design em andamento, sujeito a alteração.*

⬜ *A confirmar: o design do subprojeto de frontend descreve a etapa como "e-mail institucional" — resta confirmar se a recuperação aceita igualmente contas cadastradas com e-mail pessoal, que é o entendimento atual.* ⬜ Captura de tela pendente.

---

## Tarefa 4 — Sair da sua conta

**Status:** ✅ Atual

**Objetivo:** encerrar sua sessão, especialmente em computadores compartilhados.

**Pré-requisitos:** estar logado.

**Como fazer:**

1. Acione a opção de **sair** disponível para usuários autenticados.
2. A plataforma encerra sua sessão — no servidor e no navegador — e leva você de volta à tela de login.
3. A partir daí, o acesso às áreas de estudo exige entrar novamente.

**Observações:**

- Encerrar a sessão é o procedimento recomendado ao usar um computador compartilhado (laboratório, biblioteca): fechar apenas a aba do navegador não encerra a sessão no servidor.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| "Fui levado de volta à página inicial sem querer" | As áreas de estudo exigem sessão ativa. Sua sessão pode ter sido encerrada — basta entrar novamente |
| Bloqueio após várias tentativas | Você atingiu o limite de 5 tentativas em 15 minutos. Aguarde o período e tente de novo, conferindo o nome de usuário |
| Nome de usuário recusado no cadastro | O nome de usuário deve ser único na plataforma — escolha outro |
| Senha recusada no cadastro | A senha precisa ter no mínimo 8 caracteres, com letras e números |
| Esqueci minha senha | Não há recuperação pela plataforma na versão atual (ver [Tarefa 3](#tarefa-3-recuperar-sua-senha)) |
| ⬜ Mensagens de erro específicas | As mensagens exatas exibidas pela plataforma serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1, 2 e 4) e regras de validação | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Autenticação e Acesso, derivada do código-fonte (rotas `/cadastro`, `/login`, controle de sessão) | jun/2026 |
| Interface futura (Tarefas 1–2) e recuperação de senha (Tarefa 3) | Relatório 1 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |

!!! note "Sobre a mudança do sistema de autenticação"
    A adequação da plataforma à LGPD prevê a migração da autenticação para um serviço externo de identidade. Para o aluno, essa mudança é **invisível no uso**: o que muda na tela é o acréscimo do acesso via Google e da recuperação de senha. Os detalhes técnicos da migração pertencem à [Descrição da Arquitetura](../../arquitetura.md), não a este guia.
