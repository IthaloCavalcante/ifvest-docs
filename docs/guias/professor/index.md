# Guia do Professor

Este guia documenta as tarefas de **criação e gestão de conteúdo** do IFVest: montar o banco de questões, criar e gerenciar simulados, produzir flashcards e manter os materiais de revisão.

!!! info "Este guia complementa o Guia do Aluno"
    Na plataforma, o perfil de professor tem **todas as capacidades do aluno**, mais as de gestão de conteúdo. Este guia cobre apenas o que se soma a elas:

    - **Conta e perfil** — criar conta, entrar, editar seus dados e excluir a conta ficam na [seção Conta](../conta/acesso.md), comum a todos os perfis, com as diferenças do professor sinalizadas nas próprias páginas.
    - **Tarefas de estudo** — ler materiais, estudar flashcards, fazer simulados e jogar o IFQuiz funcionam para você exatamente como para o aluno, e estão no [Guia do Aluno](../aluno/index.md).

!!! warning "Qual versão da plataforma este guia documenta"
    O IFVest está em processo de **refatoração do frontend** (migração para React, com redesign completo da interface). Por orientação do projeto, este guia é escrito tendo a **plataforma refatorada como referência**, para evitar documentar telas transitórias que serão substituídas.

    Cada tarefa distingue duas camadas: o **fluxo da tarefa** (objetivo, pré-requisitos, passos), verificável hoje e estável após a refatoração; e a **interface** (telas, botões, navegação), descrita nos blocos *"Na versão refatorada"* com base nos relatórios do subprojeto de frontend — design **ainda em elaboração, sujeito a alteração**.

!!! danger "Atenção: os perfis de professor e administrador estão sendo redefinidos"
    O redesign prevê a criação de um **perfil de administrador**, que assumirá parte das tarefas hoje atribuídas ao professor. As decisões registradas até o momento incluem a saída da criação de materiais de revisão da área do professor (mantendo apenas a edição) e a substituição da tela "Meus Materiais" por um "Histórico de Edições".

    Enquanto essa redistribuição não é concluída, **cada tarefa deste guia indica a qual perfil pertence** (ver [legenda de perfil](#legenda-de-perfil)). As tarefas marcadas como *a definir* poderão migrar para um futuro **Guia do Administrador**.

    *Fonte: atas de reunião do subprojeto de frontend (abr–mai/2026).*

---

## Para quem é este guia

Professores do IFSP Campus Jacareí que produzem e mantêm o conteúdo do IFVest — questões, simulados, flashcards e materiais de estudo. Nenhum conhecimento técnico de programação é necessário.

**Pré-requisito geral:** ter uma conta com perfil **Professor**. O perfil é escolhido no [cadastro](../conta/acesso.md#tarefa-1-criar-uma-conta) e define o acesso às funções descritas aqui — uma conta criada como aluno não terá acesso a nenhuma das áreas deste guia.

---

## Mapa das áreas de gestão

| Área | O que você faz nela |
|---|---|
| **Banco de questões** | Criar, editar e excluir questões objetivas e dissertativas; conferir similaridade com questões já existentes |
| **Simulados** | Montar simulados a partir do banco de questões, gerenciá-los e imprimir |
| **Flashcards** | Criar, editar e excluir os cartões de estudo disponibilizados aos alunos |
| **Materiais de revisão** | Produzir e manter os conteúdos teóricos do módulo de Revisão |
| **Organização de conteúdos** | Manter as áreas, tópicos e assuntos que categorizam todo o conteúdo |

Os termos usados na plataforma estão explicados no [Glossário](../glossario.md).

---

## Como ler as tarefas deste guia

Cada tarefa segue a mesma estrutura das do Guia do Aluno, baseada na **ISO/IEC/IEEE 26514:2022** — *Design and development of information for users* —, acrescida do campo **Perfil**:

| Campo | O que informa |
|---|---|
| **Status** | Se a tarefa funciona hoje ou é prevista no redesign (ver legenda abaixo) |
| **Perfil** | A qual perfil a tarefa pertence após a redistribuição (ver legenda abaixo) |
| **Objetivo** | O que você realiza ao completar a tarefa |
| **Pré-requisitos** | O que precisa estar pronto antes |
| **Como fazer** | A sequência de passos, do início ao resultado |
| **Na versão refatorada** | Como a tela/fluxo ficará no novo design, com a fonte citada |
| **Observações** | Limites, validações e situações comuns |

### Legenda de status

- ✅ **Atual** — a tarefa funciona hoje na plataforma em produção. A interface será redesenhada, mas o fluxo permanece.
- 🟡 **Refatorado (em design)** — a tarefa ainda não existe na plataforma atual; está prevista no design da versão refatorada.
- 🔵 **Em deliberação** — a tarefa ainda não foi decidida: o projeto avalia se ela existirá.
- ⬜ **Pendência** — item aguardando confirmação ou material (captura de tela, verificação na plataforma, decisão do projeto).

### Legenda de perfil

- 👤 **Professor** — atribuição atual da tarefa, **não afetada** pelas decisões de redistribuição de perfis registradas até o momento.
- 🔄 **A definir** — atribuição **sob revisão**: a tarefa pode passar ao perfil de administrador. Se isso ocorrer, ela migra integralmente para o Guia do Administrador.

!!! note "Por que marcar o perfil de cada tarefa"
    A redistribuição de perfis ainda não foi concluída, e esperar por ela paralisaria a documentação. Marcando o perfil tarefa a tarefa, a definição final se resolve **movendo blocos inteiros** entre guias, sem reescrever conteúdo — o mesmo princípio aplicado às camadas estável e volátil da interface.

---

## Estrutura do guia

As páginas estão na ordem sugerida de leitura: primeiro o banco de questões, que alimenta os simulados; depois os demais tipos de conteúdo.

| Página | Conteúdo | Status |
|---|---|---|
| [Acesso e Conta](../conta/acesso.md) | Cadastro (com o campo Perfil), login, logoff | ✅ Comum a todos os perfis |
| [Perfil e Seus Dados](../conta/perfil.md) | Editar dados; excluir conta e o efeito sobre o conteúdo criado | ✅ Comum a todos os perfis |
| [Banco de Questões](banco-de-questoes.md) | Criar, editar e excluir questões; verificação de similaridade por IA | ✅ Disponível |
| [Simulados](simulados.md) | Montar, gerenciar e imprimir simulados | ✅ Disponível |
| [Flashcards](flashcards.md) | Criar, editar e excluir flashcards | ✅ Disponível |
| [Materiais de Revisão](materiais-de-revisao.md) | Produzir e manter conteúdos teóricos | ✅ Disponível — tarefas marcadas por perfil |
| Organização de Conteúdos | Áreas, tópicos e assuntos | ⬜ Pendente — provável migração para o perfil administrador |

---

## Conformidade com as normas

Este guia integra, junto com o [Guia do Aluno](../aluno/index.md) e a [seção Conta](../conta/acesso.md), o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto (ver [Planejamento da Documentação](../../planejamento.md)), com estrutura e conteúdo conforme a **ISO/IEC/IEEE 26514:2022**. Ambas as normas permitem **adaptação ao contexto do projeto** (*tailoring*), desde que a seleção de elementos aplicados e adiados seja registrada. Este é o registro:

| Elemento da 26514 | Onde está | Situação |
|---|---|---|
| Análise de público-alvo e tarefas | Seção "Para quem é" + inventário de tarefas por área | ✅ Aplicado |
| Informação instrucional (tarefas passo a passo) | Corpo das páginas | 🟡 Em produção (4 de 5 páginas) |
| Informação conceitual | "Mapa das áreas de gestão" + introdução de cada página | 🟡 Em produção |
| Solução de problemas | Seção "Erros e situações comuns" de cada página | 🟡 Em produção |
| Mensagens de erro (textos exatos) | Depende da interface React estabilizada | ⬜ Adiado, com justificativa |
| Informação de referência | Coberta fora do guia pela [Descrição das Funcionalidades](../../funcionalidades.md) | ✅ Coberto pela Fase 3 |
| Glossário | [Glossário](../glossario.md), comum aos guias | ✅ Aplicado |
| Acessibilidade | [Seção comum aos guias](../index.md#acessibilidade-da-plataforma) | 🟡 Normas de referência identificadas e convenções definidas; textos alternativos pendentes com as capturas |
| Atribuição de perfis | Campo **Perfil** em cada tarefa + legenda | 🟡 Provisório até a definição da redistribuição |
| Validação com usuários | Prevista conforme a **ISO/IEC/IEEE 26513**, após a entrega da interface React | ⬜ Adiado, com justificativa |
