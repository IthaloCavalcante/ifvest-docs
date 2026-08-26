# Simulados

O módulo de **Simulados** (`/simulados`) permite realizar provas de prática montadas a partir do banco de questões da plataforma, com questões objetivas (alternativas A–E) e dissertativas. Hoje, os simulados são criados pelos professores e realizados pelos alunos; a versão refatorada redesenha o módulo inteiro — da criação à resolução — e prevê a criação de simulados pelo próprio usuário.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração pelo subprojeto de frontend e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Ver os simulados disponíveis

**Status:** ✅ Atual

**Objetivo:** encontrar os simulados que você pode realizar.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta) — o módulo de Simulados exige sessão ativa.

**Como fazer:**

1. Acesse o módulo **Simulados** (`/simulados`).
2. Abra a listagem de simulados (**`/simulados/visualizar`**), que exibe os simulados disponíveis na plataforma.
3. Escolha um simulado para realizá-lo (ver [Tarefa 2](#tarefa-2-fazer-um-simulado)).

!!! abstract "Na versão refatorada"
    O redesign detalha a área **"Meus Simulados"**, com as criações do próprio usuário (ver [Tarefa 4](#tarefa-4-criar-seu-proprio-simulado)). ⬜ O destino da **listagem geral** de simulados disponibilizados pelos professores ainda não está descrito nos relatórios — a documentar quando definido.

---

## Tarefa 2 — Fazer um simulado

**Status:** ✅ Atual — *com limitação conhecida na interface (ver aviso abaixo)*

**Objetivo:** realizar uma prova de prática, respondendo às questões no seu ritmo.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta).

**Como fazer** (fluxo da tarefa):

1. Na listagem, abra o simulado desejado e escolha **"fazer"**.
2. As questões do simulado são exibidas. Não há limite de tempo — responda no ritmo que preferir.
3. Responda às questões: nas **objetivas**, escolhendo uma alternativa (A–E); nas **dissertativas**, escrevendo sua resposta *(ver a limitação abaixo)*.
4. Ao terminar, acione **"enviar simulado"**. A plataforma gera um relatório final com desempenho geral, quantidade de acertos e erros.

!!! warning "Limitação conhecida da interface atual"
    Na tela atual, as questões são exibidas **sem alternativas selecionáveis e sem campos de texto** — não há como registrar suas respostas. Além disso, as questões **dissertativas são automaticamente consideradas incorretas**, independentemente do conteúdo, e o relatório final é gerado mesmo assim. **As métricas exibidas não refletem seu desempenho real** — não as use como medida de estudo até a versão refatorada.

    *Fonte: Relatório 2 — Isabella Pereira (frontend), observações sobre o estado atual, figs. 1.2.1 e 1.2.2.*

!!! abstract "Na versão refatorada"
    A resolução passa a exibir as questões **uma a uma**, com alternativas selecionáveis nas objetivas e campo de escrita nas dissertativas. Ao responder cada questão — acertando ou errando — **um método de solução (explicação) é exibido** antes de seguir adiante. O fluxograma anexo ao redesign prevê ainda a opção de **salvar um simulado em andamento** para continuar depois.

    *Fontes: Relatório 2 — Isabella Pereira (frontend), figs. 3 e 3.1; Fluxograma sugerido (anexo ao Relatório 2). Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente (aguardando estabilização da interface).

---

## Tarefa 3 — Conferir o resultado e o gabarito

**Status:** ✅ Atual — *com a ressalva da [Tarefa 2](#tarefa-2-fazer-um-simulado)*

**Objetivo:** ver seu desempenho e as respostas corretas após realizar um simulado.

**Pré-requisitos:** ter enviado o simulado.

**Como fazer:**

1. Ao enviar o simulado, a plataforma exibe o **relatório final**, com desempenho geral, acertos e erros.
2. O **[gabarito](../glossario.md#termos)** (**`/simulados/:id/gabarito`**) exibe as respostas corretas das questões após a realização.

**Observações:**

- Enquanto a limitação da Tarefa 2 existir, o relatório **não reflete seu desempenho real** (as respostas não são registradas e as dissertativas contam como erradas). O gabarito continua útil para conferir as respostas corretas das questões.

!!! abstract "Na versão refatorada"
    O retorno passa a ser **imediato e questão a questão**, com explicação a cada resposta — o resultado deixa de ser apenas um relatório ao final. ⬜ O formato do relatório consolidado no redesign ainda não foi detalhado nos relatórios — a documentar quando definido.

    *Fonte: Relatório 2 — Isabella Pereira (frontend), figs. 3 e 3.1.*

---

## Tarefa 4 — Criar seu próprio simulado

**Status:** 🔵 Em deliberação

**Objetivo:** montar um simulado personalizado — escolhendo tema, dificuldade e tipo de questão — para praticar exatamente o que você precisa.

!!! warning "Esta funcionalidade ainda não foi decidida"
    Hoje, **apenas professores criam simulados**. O subprojeto de frontend desenhou um fluxo de criação descrito para "o usuário", mas **ainda avalia se ele ficará disponível ao aluno** ou permanecerá restrito a professores e administradores.

    O fluxo abaixo está documentado porque o design existe — não porque a disponibilização ao aluno esteja confirmada. ⬜ *A atualizar quando a decisão for tomada.*

**Como funcionará (conforme o design):**

Ao acessar **"Criar novo simulado"**, você define um **título** (com descrição opcional) e a **quantidade de questões**, e faz as escolhas comuns aos dois modos de criação: o **tipo de simulado** (Por disciplina, Por assunto, Enem, Unicamp), a **disciplina**, o **assunto** (opcional no modo aleatório) e o **tipo de questão** (objetiva, dissertativa ou ambas). A partir daí, há dois caminhos:

- **Gerar com questões aleatórias** — o sistema monta o simulado sozinho conforme suas escolhas, preservando a imprevisibilidade da prova.
- **Gerar com questões selecionadas** — você escolhe questão por questão: os títulos aparecem em lista, clicar no ID seleciona a questão (as escolhidas ficam visíveis em um balão lateral) e a seta à direita expande o enunciado e as alternativas. É possível voltar e **"Escolher outros assuntos"** mantendo as seleções anteriores.

Em ambos os caminhos, o simulado é salvo na área **"Meus Simulados"**, onde pode ser **realizado, editado, removido, visualizado ou exportado em PDF**.

*Fontes: Relatório 2 — Isabella Pereira (fluxo geral de criação); Relatório 3 — Isabella Pereira (filtros e seleção manual, figs. 1.0 a 3.0); Fluxograma sugerido (anexo ao Relatório 2). Design em andamento, sujeito a alteração.*

!!! note "Observação — o design ainda está em iteração"
    O Relatório 2 registrava a escolha do tipo de questão como pendente ("será implementado na próxima semana"); o Relatório 3 a incorporou aos dois modos de criação. O registro fica aqui como evidência de que a camada de interface segue em evolução.

⬜ Captura de tela pendente.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| "Enviei o simulado e o resultado veio zerado ou com erros que não cometi" | É a limitação conhecida da interface atual ([Tarefa 2](#tarefa-2-fazer-um-simulado)): as respostas não são registradas. **Não é um erro seu** |
| Questões dissertativas sempre marcadas como incorretas | Mesma limitação: a avaliação atual considera todas as dissertativas erradas automaticamente |
| ⬜ Mensagens de erro específicas | As mensagens exatas serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Rotas e fluxos atuais (Tarefas 1–3: listagem, fazer, gabarito) | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Simulados, derivada do código-fonte (rotas `/simulados/*`, repositório IFVEST-main) | jun/2026 |
| Comportamento observado da tela de fazer e do relatório (Tarefas 2–3) | Relatório 2 — Isabella Pereira, observações sobre o estado atual | mar/2026 |
| Interface futura e criação de simulados (Tarefas 2–4) | Relatórios 2 e 3 — Isabella Pereira + Fluxograma sugerido (anexo ao Relatório 2), subprojeto *Refatoração para React e Redesign do IFVest* | mar–abr/2026 |

!!! note "Registro de divergência entre fontes"
    Para a tela de fazer simulado, a Descrição das Funcionalidades (Fase 3, derivada do código) descreve a seleção de alternativas (A–E) e campo de texto livre; o Relatório 2 observou, no sistema em produção, a **ausência** desses mecanismos. Por decisão do projeto, esta página adota o **comportamento observado em produção**. ⬜ Pendência: confirmar na plataforma e ajustar a Fase 3 na etapa de revisão da documentação.
