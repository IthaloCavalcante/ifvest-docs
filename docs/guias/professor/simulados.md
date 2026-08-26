# Simulados

O módulo de **Simulados** (`/simulados`) é onde você monta as provas de prática que os alunos realizam. Um simulado é um **conjunto de questões vindas do banco** ([Banco de Questões](banco-de-questoes.md)): você cria as questões uma vez e as reaproveita em quantos simulados quiser.

Além de disponibilizá-lo na plataforma, é possível **imprimir** o simulado para aplicação em papel.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Criar um simulado

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** montar uma prova de prática a partir das questões do banco.

**Pré-requisitos:** estar logado com perfil de professor; ter **ao menos uma questão cadastrada** (ver [Banco de Questões](banco-de-questoes.md#tarefa-2-criar-uma-questao)) — não é possível criar um simulado vazio.

**Como fazer:**

1. Acesse **Criar simulado** (`/simulados/criar-simulado`).
2. Preencha os campos:

    | Campo | Regra |
    |---|---|
    | **Título** | identifica o simulado nas listagens |
    | **Descrição** | **obrigatória**, com no mínimo 10 caracteres |
    | **Tipo** | Objetivo, Dissertativo ou Aleatório |

3. **Selecione as questões** que comporão o simulado. É necessário vincular pelo menos uma.
4. Finalize a criação. Você é levado à área **Meus Simulados**, onde o novo simulado aparece (ver [Tarefa 2](#tarefa-2-ver-e-gerenciar-seus-simulados)).

!!! warning "Limitações conhecidas da versão atual"
    Três comportamentos foram observados no sistema em produção e devem ser considerados ao montar um simulado:

    - **O campo Tipo não altera o comportamento do sistema.** Escolher Objetivo, Dissertativo ou Aleatório não muda a exibição nem filtra as questões oferecidas para seleção.
    - **A seleção de questões não tem filtro por disciplina.** Todas as suas questões aparecem juntas, sem separação por área ou assunto — em bancos grandes, localizar as questões desejadas fica trabalhoso.
    - **O tipo "Aleatório" não gera questões automaticamente.** A seleção manual continua obrigatória, o que remove a imprevisibilidade esperada desse tipo.

    *Fonte: Relatório 2 — Isabella Pereira (frontend), observações sobre o estado atual, figs. 1.1 e 1.1.2.*

!!! abstract "Na versão refatorada"
    A criação é reorganizada em duas etapas. Primeiro você define o **título**, uma **descrição opcional** e a **quantidade de questões**. Em seguida, faz as escolhas comuns aos dois modos de criação:

    | Escolha | Opções |
    |---|---|
    | **Tipo de simulado** | Por disciplina, Por assunto, Enem, Unicamp |
    | **Disciplina** | disciplinas do ensino médio no contexto pré-vestibular |
    | **Assunto** | assuntos da disciplina escolhida (opcional no modo aleatório) |
    | **Tipo de questão** | objetiva, dissertativa, ou ambas |

    A partir daí, há **dois caminhos**:

    - **Gerar com questões aleatórias** — o sistema monta o simulado conforme suas escolhas, sem seleção manual, preservando a imprevisibilidade.
    - **Gerar com questões selecionadas** — você escolhe questão por questão: os títulos aparecem em lista, clicar no ID seleciona a questão (as escolhidas ficam visíveis em um balão lateral) e a seta à direita expande enunciado e alternativas. O botão **"Escolher outros assuntos"** permite voltar mantendo as seleções já feitas.

    Em ambos os caminhos, o simulado é salvo em **Meus Simulados**.

    *Fontes: Relatório 2 — Isabella Pereira (fluxo geral de criação, fig. 2.2.0); Relatório 3 — Isabella Pereira (filtros e seleção manual, figs. 1.0 a 3.0); Fluxograma sugerido (anexo ao Relatório 2). Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente. ⬜ *A confirmar: os relatórios descrevem esse fluxo para "o usuário", sem distinguir professor de aluno — resta esclarecer se a criação de simulados passará a estar disponível também ao aluno (ver [Guia do Aluno](../aluno/simulados.md#tarefa-4-criar-seu-proprio-simulado)).*

---

## Tarefa 2 — Ver e gerenciar seus simulados

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** consultar os simulados que você criou e acessar as ações de manutenção.

**Pré-requisitos:** estar logado com perfil de professor.

**Como fazer:**

1. Acesse **Meus simulados** (`/simulados/meus-simulados`).
2. A lista exibe os simulados criados por você, com as opções de **editar**, **excluir** e **gerenciar as questões** de cada um.

!!! abstract "Na versão refatorada"
    A área Meus Simulados é redesenhada e passa a concentrar todas as ações sobre um simulado: **realizar, editar, remover, visualizar e exportar em PDF**. O fluxograma do redesign prevê ainda um **atalho rápido** para o simulado recém-criado.

    *Fontes: Relatório 2 — Isabella Pereira, fig. 2.1; Relatório 3 — Isabella Pereira, fig. 2.3; Fluxograma sugerido. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente.

---

## Tarefa 3 — Editar um simulado

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** corrigir ou atualizar os dados de um simulado já criado.

**Pré-requisitos:** ter o simulado criado por você.

**Como fazer:**

1. Em **Meus simulados**, localize o simulado e acione a edição (`/simulados/:id/editar`).
2. Altere **título**, **descrição** ou **tipo**.
3. Salve as alterações.

**Observações:**

- A edição altera apenas os dados do simulado. Para mudar **quais questões** ele contém, use a [Tarefa 4](#tarefa-4-adicionar-ou-remover-questoes-de-um-simulado).
- A regra de mínimo de 10 caracteres da descrição continua valendo na edição.

---

## Tarefa 4 — Adicionar ou remover questões de um simulado

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** ajustar o conjunto de questões de um simulado já criado, sem precisar refazê-lo.

**Pré-requisitos:** ter o simulado criado por você; para adicionar, ter as questões cadastradas no banco.

**Como fazer:**

- Para **incluir** questões, acesse **Adicionar questões** (`/simulados/:simuladoId/adicionar-questoes`) e selecione as questões a vincular.
- Para **retirar** questões, acesse **Remover questões** (`/simulados/:simuladoId/remover-questoes`) e desvincule as questões desejadas.

**Observações:**

- Remover uma questão do simulado **não a exclui do banco** — ela continua disponível para outros simulados. Para apagá-la definitivamente, use [Excluir uma questão](banco-de-questoes.md#tarefa-5-excluir-uma-questao).
- Retirar uma questão do simulado desfaz o vínculo entre os dois; as respostas já registradas pelos alunos para aquela questão continuam associadas a ela no banco. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Tarefa 5 — Imprimir um simulado

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** gerar uma versão formatada do simulado para aplicação em papel.

**Pré-requisitos:** ter o simulado criado, com as questões já vinculadas.

**Como fazer:**

1. Em **Meus simulados**, acione a opção de impressão (`/simulados/:simuladoId/imprimir`).
2. A plataforma gera uma versão do simulado com formatação própria para impressão.
3. Use a função de imprimir do navegador para enviar à impressora ou salvar como PDF.

**Observações:**

- **A versão impressa das questões dissertativas inclui o gabarito.** Cada questão dissertativa traz um bloco identificado como "Gabarito / Resposta Esperada", seguido das linhas para a resposta do aluno. Nas objetivas, as alternativas saem sem marcação visível da correta. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

!!! abstract "Na versão refatorada"
    A exportação em **PDF** passa a ser uma das ações disponíveis diretamente na área Meus Simulados.

    *Fonte: Relatório 2 — Isabella Pereira, descrição do novo fluxo. Design em andamento, sujeito a alteração.*

---

## Tarefa 6 — Excluir um simulado

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** remover um simulado que não será mais utilizado.

**Pré-requisitos:** ter o simulado criado por você.

**Como fazer:**

1. Em **Meus simulados**, localize o simulado e acione a exclusão.
2. O simulado deixa de estar disponível na plataforma.

**Observações:**

- Excluir o simulado **não exclui as questões** que o compunham — elas permanecem no banco.
- A exclusão do simulado remove também os **vínculos com as questões** e as **respostas registradas pelos alunos** naquele simulado. As questões em si permanecem no banco. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| Não consigo finalizar a criação do simulado | É obrigatório vincular ao menos uma questão. Confira também se a descrição tem no mínimo 10 caracteres |
| Não encontro minhas questões na hora de selecionar | A seleção atual não separa as questões por disciplina — todas aparecem juntas. Use o título da questão para localizá-las |
| Escolhi o tipo "Aleatório" e o sistema pediu para eu selecionar as questões | É a limitação conhecida da versão atual: o tipo não altera o comportamento do sistema ([Tarefa 1](#tarefa-1-criar-um-simulado)) |
| Removi uma questão do simulado e ela sumiu da lista | Ela foi apenas desvinculada do simulado; continua no seu banco de questões |
| ⬜ Mensagens de erro específicas | As mensagens exatas serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–6): criação, gestão, edição, questões, impressão e exclusão | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Simulados, seção "Para o Professor", derivada do código-fonte (rotas `/simulados/criar-simulado`, `meus-simulados`, `:id/editar`, `adicionar-questoes`, `remover-questoes`, `:id/imprimir`) | jun/2026 |
| Comportamento observado na criação e regra da descrição (Tarefa 1) | Relatório 2 — Isabella Pereira, descrição do fluxo atual e problemas identificados | mar/2026 |
| Interface futura (Tarefas 1, 2 e 5) | Relatórios 2 e 3 — Isabella Pereira + Fluxograma sugerido (anexo ao Relatório 2), subprojeto *Refatoração para React e Redesign do IFVest* | mar–abr/2026 |

!!! note "Relação com o Guia do Aluno"
    A página de [Simulados do Guia do Aluno](../aluno/simulados.md) documenta o outro lado do módulo — ver, realizar e conferir simulados —, incluindo a limitação atual da tela de resolução, em que as questões são exibidas sem mecanismo de resposta. Isso afeta você indiretamente: **os relatórios de desempenho dos alunos não refletem o resultado real** até que essa entrega seja concluída.
