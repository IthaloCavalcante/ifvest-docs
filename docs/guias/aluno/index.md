# Guia do Aluno

Este guia ensina, tarefa por tarefa, como usar a plataforma IFVest no perfil de **aluno**: acessar sua conta, estudar pelos módulos de Revisão, IFQuiz, Flashcards e Simulados, e gerenciar seu perfil.

!!! warning "Qual versão da plataforma este guia documenta"
    O IFVest está em processo de **refatoração do frontend** (migração para React, com redesign completo da interface). Por orientação do projeto, este guia é escrito tendo a **plataforma refatorada como referência**, para evitar documentar telas transitórias que serão substituídas.

    Na prática, cada tarefa distingue duas camadas:

    - O **fluxo da tarefa** (objetivo, pré-requisitos, sequência de passos) — válido hoje e após a refatoração, verificado no sistema em produção.
    - A **interface** (telas, botões, navegação) — descrita nos blocos *"Na versão refatorada"*, com base nos relatórios do subprojeto de frontend. Esse design **ainda está em elaboração e pode mudar** até a entrega.

    Capturas de tela e instruções visuais definitivas serão adicionadas quando a interface React estabilizar.

---

## Para quem é este guia

Estudantes que usam o IFVest para se preparar para o ENEM e vestibulares. Nenhum conhecimento técnico é necessário — basta um navegador de internet e acesso à plataforma em `ifvest.jcr.ifsp.edu.br`.

**O que este guia não cobre:** as funções de criação e gestão de conteúdo (questões, simulados, materiais, flashcards), que pertencem aos perfis de professor e administrador. Elas são tratadas no [Guia do Professor](../professor/index.md), em produção — parte dessas tarefas pode ainda ser redistribuída entre os perfis de professor e administrador na plataforma refatorada.

---

## Mapa da plataforma

Visão rápida do que o aluno encontra no IFVest:

| Módulo | O que você faz nele |
|---|---|
| **Revisão** | Ler materiais de estudo teóricos, organizados por assunto |
| **IFQuiz** | Jogar quizzes com questões do ENEM e acompanhar o placar |
| **Flashcards** | Estudar com cartões de pergunta e resposta e repetição espaçada |
| **Simulados** | Realizar provas de prática e conferir o gabarito |

Os termos usados na plataforma — área, tópico, assunto, repetição espaçada, gabarito, eficiência — estão explicados no [Glossário](../glossario.md).

---

## Acessibilidade

Os módulos de Simulados, Flashcards e IFQuiz passaram por avaliação e ajustes de acessibilidade — navegação apenas por teclado e uso com leitor de tela. Os detalhes estão em [Acessibilidade da plataforma](../index.md#acessibilidade-da-plataforma).

---

## Como ler as tarefas deste guia

Cada tarefa segue a mesma estrutura, baseada na **ISO/IEC/IEEE 26514:2022** — *Design and development of information for users*:

| Campo | O que informa |
|---|---|
| **Status** | Ver legenda abaixo |
| **Objetivo** | O que você realiza ao completar a tarefa |
| **Pré-requisitos** | O que precisa estar pronto antes (ex.: estar logado) |
| **Como fazer** | A sequência de passos, do início ao resultado |
| **Na versão refatorada** | Como a tela/fluxo ficará no novo design, com a fonte citada |
| **Observações** | Limites, validações e situações comuns |

**Legenda de status das tarefas:**

- ✅ **Atual** — a tarefa funciona hoje na plataforma em produção. A interface será redesenhada, mas o fluxo permanece.
- 🟡 **Refatorado (em design)** — a tarefa **ainda não existe** na plataforma atual. Ela está prevista no design da versão refatorada e será disponibilizada com a nova interface.
- ⬜ **Pendência** — marca itens aguardando confirmação ou material (ex.: captura de tela, verificação na plataforma).

Toda informação da camada *"Na versão refatorada"* cita sua fonte (relatório e figura do subprojeto de frontend), seguindo o critério desta documentação: **nada é documentado sem evidência confirmada**.

---

## Estrutura do guia

Antes de começar, as tarefas de conta são comuns a todos os perfis: [Acesso e Conta](../conta/acesso.md) e [Perfil e Seus Dados](../conta/perfil.md).

As páginas de estudo abaixo estão na ordem sugerida de leitura — da teoria à prática.

| Página | Conteúdo | Status |
|---|---|---|
| [Revisão de Conteúdo](revisao.md) | Navegar, buscar e ler materiais de estudo; progresso | ✅ Disponível |
| [Flashcards](flashcards.md) | Estudar cartões; criar os próprios (versão refatorada) | ✅ Disponível |
| [Simulados](simulados.md) | Ver, fazer e conferir simulados; criar o próprio (versão refatorada) | ✅ Disponível |
| [IFQuiz](ifquiz.md) | Jogar quiz, ver resultado e placar | ✅ Disponível — camada refatorada pendente |
| [Glossário](../glossario.md) | Termos da plataforma e organização dos conteúdos | ✅ Disponível |

---

## Conformidade com as normas

Este guia é o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto (ver [Planejamento da Documentação](../../planejamento.md)): a 15289 exige que o item exista e define seu papel — *explicar como usar, não o que existe*; a estrutura e o conteúdo seguem a **ISO/IEC/IEEE 26514:2022** — *Design and development of information for users* (edição vigente, que substituiu a ISO/IEC 26514:2008 e renomeou o escopo de "documentação de usuário" para "informação para usuários").

Ambas as normas permitem **adaptação ao contexto do projeto** (*tailoring*), desde que a seleção de elementos aplicados e adiados seja registrada. Este é o registro:

| Elemento da 26514 | Onde está | Situação |
|---|---|---|
| Análise de público-alvo e tarefas | Seção "Para quem é" + inventário de tarefas por módulo | ✅ Aplicado |
| Informação instrucional (tarefas passo a passo) | Corpo das páginas de módulo | ✅ 6 de 6 páginas redigidas |
| Informação conceitual (o que cada módulo é) | "Mapa da plataforma" + introdução de cada página | ✅ Aplicado |
| Solução de problemas | Seção "Erros e situações comuns" de cada página | ✅ Aplicado (mensagens exatas pendentes) |
| Mensagens de erro (textos exatos) | Depende da interface React estabilizada | ⬜ Adiado, com justificativa |
| Informação de referência | Coberta fora do guia pela [Descrição das Funcionalidades](../../funcionalidades.md) | ✅ Coberto pela Fase 3 |
| Glossário | Página [Glossário](../glossario.md) | ✅ Aplicado |
| Informação de acessibilidade da plataforma | [Seção comum aos guias](../index.md#acessibilidade-da-plataforma) | ✅ Aplicado, com normas de referência identificadas (WCAG 2.2 e ABNT NBR 17225:2025) |
| Acessibilidade da documentação | [Convenções comuns aos guias](../index.md#convencoes-de-acessibilidade-destes-guias) | 🟡 Convenções definidas; textos alternativos pendentes com as capturas |
| Tarefas de conta e perfil | [Seção Conta](../conta/acesso.md), comum a todos os perfis | ✅ Aplicado |
| Validação com usuários | Prevista conforme a **ISO/IEC/IEEE 26513** (testes e revisão de documentação), após a entrega da interface React | ⬜ Adiado, com justificativa |
