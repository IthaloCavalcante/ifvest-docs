# Perfil e Seus Dados

Esta página reúne as tarefas de gerenciamento da sua conta: consultar e atualizar seus dados cadastrais, trocar a foto de perfil e a senha, e excluir a conta. Todas ficam na área de **perfil do usuário** (`/usuario/perfil`), disponível para quem está logado.

Ela vale para **todos os perfis** — aluno e professor. A exclusão da conta tem consequências diferentes para cada um: veja o aviso na [Tarefa 4](#tarefa-4-excluir-sua-conta).

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração pelo subprojeto de frontend e **podem mudar até a entrega**. Veja [como ler as tarefas](../index.md#como-ler-as-tarefas).

---

## Tarefa 1 — Consultar e atualizar seus dados cadastrais

**Status:** ✅ Atual

**Objetivo:** conferir e corrigir as informações que a plataforma tem sobre você.

**Pré-requisitos:** estar logado (ver [Acesso e Conta](acesso.md#tarefa-2-entrar-na-sua-conta)).

**Como fazer:**

1. Acesse a área de **perfil** (`/usuario/perfil`). Seus dados cadastrais são exibidos.
2. Edite os campos que quiser atualizar:

    | Campo | Observação |
    |---|---|
    | **Nome completo** | — |
    | **Nome de usuário** | é a credencial que você usa para entrar (ver aviso abaixo) |
    | **E-mail** | — |

3. Salve as alterações.

!!! warning "Ao trocar o nome de usuário, sua forma de entrar muda"
    O login atual é feito com **nome de usuário**, não com e-mail. Se você alterar esse campo, passe a usar o **novo** nome de usuário para entrar na plataforma. As mesmas regras do cadastro continuam valendo: de 3 a 30 caracteres, e o nome precisa ser único na plataforma.

!!! abstract "Na versão refatorada"
    A área de gerenciamento de perfil é reestruturada, mantendo as três capacidades atuais: **alteração da foto**, **atualização das informações cadastrais** e **opção de exclusão** da conta.

    *Fonte: Relatório 1 — Maria Luiza (frontend), item 4 e fig. 3.3. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente (aguardando estabilização da interface).

---

## Tarefa 2 — Trocar sua foto de perfil

**Status:** ✅ Atual

**Objetivo:** definir ou substituir a imagem que identifica sua conta.

**Pré-requisitos:** estar logado; ter o arquivo de imagem no dispositivo.

**Como fazer:**

1. Na área de perfil, escolha a opção de **foto de perfil**.
2. Faça o **upload** da imagem desejada.
3. Salve a alteração — a nova imagem passa a identificar sua conta.

**Observações:**

- Não há restrição de formato ou de tamanho definida para a imagem enviada. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Tarefa 3 — Trocar sua senha

**Status:** ✅ Atual

**Objetivo:** substituir sua senha atual por uma nova, sabendo a senha vigente.

**Pré-requisitos:** estar logado e **saber sua senha atual**. Se você não a souber, veja [Recuperar sua senha](acesso.md#tarefa-3-recuperar-sua-senha).

**Como fazer:**

1. Na área de perfil, localize a troca de senha.
2. Informe a **senha atual** e, em seguida, a **nova senha**.
3. Salve a alteração. A partir daí, use a nova senha para entrar.

**Observações:**

- Informar a senha atual é uma proteção: impede que alguém com acesso momentâneo ao seu navegador troque sua senha e tome a conta.
- A nova senha segue **as mesmas regras do cadastro**: mínimo de 8 caracteres, com ao menos uma letra e um número. *(Conforme o código-fonte da plataforma anterior ao redesign.)*
- Na versão refatorada, a área de perfil terá um **botão dedicado à troca de senha**, que leva você à tela da funcionalidade. *(Definição do subprojeto de frontend registrada em reunião, ago/2026.)*

---

## Tarefa 4 — Excluir sua conta

**Status:** ✅ Atual

**Objetivo:** encerrar definitivamente sua conta e remover seus dados da plataforma.

**Pré-requisitos:** estar logado.

!!! danger "Esta ação é irreversível"
    A exclusão remove seu registro de usuário e, **em cascata, os dados associados a ele** — as questões e as respostas vinculadas à sua conta. Não há como desfazer a exclusão nem recuperar esses dados depois. Se sua intenção é apenas parar de usar a plataforma por um período, **encerrar a sessão** ([sair](acesso.md#tarefa-4-sair-da-sua-conta)) é suficiente e preserva seus dados.

!!! danger "Se você é professor: a exclusão apaga o conteúdo que você criou"
    A remoção em cascata alcança as **questões** e os **simulados** cadastrados por você, junto com as alternativas e as respostas vinculadas a eles. Os flashcards **não** são afetados, por não guardarem autoria.

    ⚠️ **Materiais de revisão impedem a exclusão.** A vinculação entre conteúdo e autor não prevê remoção em cascata, de modo que a exclusão de uma conta com materiais publicados tende a ser recusada pelo sistema. Nesse caso, procure a coordenação do projeto — remover os materiais por conta própria significaria descartar conteúdo de estudo em uso.

    *Conforme o código-fonte da plataforma anterior ao redesign.*

**Como fazer:**

1. Na área de perfil, acione a opção de **exclusão da conta**.
2. Confirme a solicitação.
3. Sua conta e os dados associados são removidos, e você perde o acesso à plataforma.

!!! abstract "Na versão refatorada"
    A opção de exclusão é mantida na área de perfil reestruturada.

    *Fonte: Relatório 1 — Maria Luiza (frontend), item 4 e fig. 3.3. Design em andamento, sujeito a alteração.*

**Observações:**

- Para voltar a usar o IFVest depois de excluir a conta, é necessário fazer um **novo cadastro** ([Criar uma conta](acesso.md#tarefa-1-criar-uma-conta)) — e o histórico anterior não é restaurado.

---

## Seus dados na plataforma

Os dados pessoais que o IFVest coleta de você no cadastro são: **nome de usuário, nome completo, e-mail, senha e foto de perfil**. Todos podem ser consultados e atualizados na área de perfil (Tarefas 1 a 3), e a exclusão da conta (Tarefa 4) é o mecanismo pelo qual você remove esses dados da plataforma.

⬜ *A confirmar: não há, na versão atual, função na plataforma para solicitar uma **cópia** dos seus dados — resta esclarecer com o subprojeto de adequação à LGPD se existe um canal para esse tipo de pedido, para orientar o aluno aqui.*

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| "Troquei o nome de usuário e não consigo mais entrar" | Use o **novo** nome de usuário — ele é a credencial de login (ver [Tarefa 1](#tarefa-1-consultar-e-atualizar-seus-dados-cadastrais)) |
| Nome de usuário recusado ao editar | O nome precisa ser único na plataforma — escolha outro |
| Não sei minha senha atual e quero trocá-la | A troca exige a senha vigente. Sem ela, veja [Recuperar sua senha](acesso.md#tarefa-3-recuperar-sua-senha) |
| Excluí a conta por engano | A exclusão é irreversível; será necessário um novo cadastro, sem o histórico anterior |
| ⬜ Mensagens de erro específicas | As mensagens exatas exibidas pela plataforma serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–4): campos editáveis, troca de senha e exclusão em cascata | [Descrição das Funcionalidades](../../funcionalidades.md) — Perfil de Usuário, derivada do código-fonte (rota `/usuario/perfil`) | jun/2026 |
| Interface futura (Tarefas 1 e 4) | Relatório 1 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest*, item 4 e fig. 3.3 | abr/2026 |
| Relação de dados pessoais coletados no cadastro | Relatório final de extensão *Adequação do Cadastro do Portal IFVest à LGPD* — diagnóstico do cadastro | 2025/2026 |

!!! note "Sobre a adequação à LGPD"
    O subprojeto de adequação à LGPD tem escopo **técnico**: reestruturação do armazenamento dos dados do cadastro, controle de acesso por usuário e formalização das bases legais de cada dado coletado. Nenhuma dessas mudanças altera as tarefas desta página — para o aluno, o uso do perfil permanece o mesmo. As tarefas de perfil já existentes (atualizar, corrigir e excluir seus dados) continuam sendo a via pela qual você gerencia suas informações.
