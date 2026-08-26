# Flashcards

O módulo de **Flashcards** (`/flashcards`) oferece cartões de estudo no formato pergunta-e-resposta: a frente do cartão traz a pergunta e o verso, a resposta. A plataforma controla **quando** cada cartão volta a aparecer para você ([repetição espaçada](../glossario.md#termos)), priorizando o que está há mais tempo sem revisão. Hoje, os cartões são criados pelos professores; a versão refatorada prevê também a criação de cartões próprios pelo aluno.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração pelo subprojeto de frontend e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Estudar com flashcards

**Status:** ✅ Atual

**Objetivo:** revisar um conjunto de cartões de pergunta e resposta sobre o conteúdo que você está estudando.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta) (o histórico de revisão é registrado por usuário).

**Como fazer:**

1. Acesse o módulo **Flashcards** (`/flashcards`).
2. Se quiser, aplique os filtros opcionais de **Área**, **Tópico** e **Dificuldade** (Fácil, Médio ou Difícil) para delimitar o que revisar.
3. A plataforma exibe **até 10 cartões por vez**, escolhidos conforme os filtros e o seu histórico de revisão (ver nota abaixo).
4. Leia a pergunta na frente do cartão e tente responder mentalmente.
5. **Vire o cartão** para conferir a resposta.

!!! note "Como a plataforma escolhe os cartões (repetição espaçada)"
    Cada vez que você visualiza um cartão, a plataforma registra a data. Na seleção seguinte, os cartões são agrupados por urgência de revisão — há quanto tempo você não os vê (1, 3, 7, 15 ou mais de 15 dias) — e os **não vistos ou vistos há mais tempo têm prioridade**. Você não precisa configurar nada: basta estudar, e o sistema traz de volta o que está para ser esquecido.

!!! abstract "Na versão refatorada"
    A área de Flashcards passa a ser dividida em **duas abas**: *Meus Flashcards*, com os cartões pré-definidos pelos professores/administradores, e *Criar Flashcards*, para os seus próprios cartões (ver [Tarefa 4](#tarefa-4-criar-seus-proprios-flashcards)).

    O caminho até os cartões também muda: em *Meus Flashcards*, você seleciona a **disciplina**, abre **"Ver todos os assuntos de flashcards"**, escolhe o **subassunto** em um menu expansível e é levado aos cartões. Em cada cartão, o botão **"Ver resposta"** vira o componente e exibe a resposta.

    *Fonte: Relatório 4 — Isabella Pereira (frontend), figs. 2.0 a 2.1.6. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente (aguardando estabilização da interface).

---

## Tarefa 2 — Revisar cartões por tempo (grupos)

**Status:** ✅ Atual

**Objetivo:** ver os cartões organizados pelo tempo desde a sua última revisão, para decidir por onde recomeçar.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta).

**Como fazer:**

1. Acesse **`/flashcards/grupos`**.
2. Os cartões aparecem agrupados por intervalo de tempo desde a última visualização (os mesmos grupos da repetição espaçada).
3. Escolha um grupo e revise os cartões correspondentes.

**Observações:**

- O subprojeto de frontend registrou que, na interface atual, essa revisão por grupos **não fica intuitiva** para o aluno. ⬜ O tratamento dessa visão no redesign ainda não foi detalhado nos relatórios — a documentar quando definido.

---

## Tarefa 3 — Continuar de onde parou

**Status:** 🟡 Refatorado (em design)

**Objetivo:** retomar o estudo de uma lista de flashcards do ponto em que você a interrompeu.

!!! warning "Disponível apenas a partir da versão refatorada"
    A plataforma atual não possui esse recurso. Esta tarefa descreve uma capacidade nova, prevista no redesign.

**Como funcionará (conforme o design):**

- Ao terminar uma lista de flashcards, ela é marcada como **concluída**.
- A partir daí, a opção **"Continuar de onde parei"** fica disponível, permitindo retomar o estudo sem recomeçar a lista do zero.

*Fonte: Relatório 4 — Isabella Pereira (frontend), fig. 2.1.6 e texto subsequente. Design em andamento, sujeito a alteração.*

⬜ O comportamento exato da retomada (o que é salvo e por quanto tempo) ainda não está especificado — a documentar quando definido.

---

## Tarefa 4 — Criar seus próprios flashcards

**Status:** 🔵 Em deliberação

**Objetivo:** montar cartões de estudo personalizados, com as suas próprias perguntas e respostas.

!!! warning "Esta funcionalidade ainda não foi decidida"
    Hoje, **apenas professores criam flashcards** — o aluno estuda com os cartões do acervo da plataforma. O subprojeto de frontend desenhou a criação pelo próprio aluno, mas **ainda avalia se ela será implementada**.

    O funcionamento abaixo está documentado porque o design existe — não porque a funcionalidade esteja confirmada. ⬜ *A atualizar quando a decisão for tomada.*

**Como funcionará (conforme o design):**

- A aba **"Criar Flashcards"** permitirá que você monte seus próprios cartões.
- Os cartões criados por você serão **visíveis somente na sua conta** — eles não são adicionados às disciplinas originais da plataforma.

O que define a visibilidade de um flashcard é **o perfil de quem o criou**: os cartões de professores e administradores compõem o acervo da plataforma e ficam disponíveis a todos os alunos; os criados por um aluno permanecem restritos à conta dele.

*Fonte: Relatório 4 — Isabella Pereira (frontend), fig. 2.2 e texto introdutório. Design em andamento, sujeito a alteração.*

⬜ Os campos do formulário de criação (e se haverá área/dificuldade como nos cartões dos professores) ainda não estão detalhados — a documentar quando definido.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| Nenhum cartão aparece para os filtros escolhidos | O acervo pode ainda não ter cartões daquela combinação (os cartões são cadastrados pelos professores). Amplie ou remova os filtros |
| Os mesmos cartões se repetem com frequência | É o comportamento esperado da repetição espaçada: cartões não vistos ou vistos há mais tempo voltam primeiro |
| ⬜ Mensagens de erro específicas | As mensagens exatas exibidas pela plataforma serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–2) | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Flashcards, derivada do código-fonte (rotas `/flashcards/*`, repositório IFVEST-main) | jun/2026 |
| Interface futura (Tarefa 1) e novas capacidades (Tarefas 3–4) | Relatório 4 — Isabella Pereira, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |
| Observação sobre a revisão por grupos (Tarefa 2) | Relatório 4 — Isabella Pereira, observações sobre o estado atual | abr/2026 |

Os Relatórios 2 e 3 de Isabella tratam do módulo Simulados, e os relatórios de Maria Luiza cobrem Revisão, autenticação e perfil — nenhum deles afeta as tarefas desta página.
