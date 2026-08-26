# Materiais de Revisão

O módulo de **Revisão** (`/revisao`) reúne os conteúdos teóricos da plataforma: textos escritos pelos professores, categorizados por área e tópico, que os alunos leem para estudar antes de praticar nos demais módulos.

Os materiais são escritos em **Markdown**, com suporte a fórmulas matemáticas, e ficam vinculados a um ponto da organização de conteúdos da plataforma.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

!!! danger "Esta é a página mais afetada pela redistribuição de perfis"
    O redesign redistribui as tarefas deste módulo entre professor e administrador. As decisões registradas até o momento são:

    - a **criação de materiais sai da área do professor** — apenas as telas de edição permanecem;
    - a tela **"Meus Materiais" é substituída por "Histórico de Edições"**;
    - o **administrador** passa a adicionar novas matérias e conteúdos, e ganha uma tela para acompanhar quais alterações foram feitas.

    Cada tarefa abaixo indica seu perfil. As marcadas 🔄 poderão migrar para um futuro **Guia do Administrador** — o que **não** significa que deixarão de existir, apenas que mudarão de responsável.

    *Fonte: atas de reunião do subprojeto de frontend, 22/05/2026.*

---

## Tarefa 1 — Ver seus materiais

**Status:** ✅ Atual  
**Perfil:** 🔄 A definir — a tela será substituída

**Objetivo:** consultar os materiais que você publicou, para revisá-los ou atualizá-los.

**Pré-requisitos:** estar logado com perfil de professor.

**Como fazer:**

1. Acesse **Meus materiais** (`/revisao/meus_materiais`).
2. A lista exibe os conteúdos criados por você, a partir da qual é possível editar e remover.

!!! warning "Esta tela será substituída"
    No redesign, "Meus Materiais" dá lugar a um **"Histórico de Edições"**. A mudança acompanha a redistribuição: se a criação de materiais passa ao administrador, o professor deixa de ter materiais de sua autoria e passa a ter o registro das **alterações que realizou**.

    ⬜ *O conteúdo e o formato dessa tela ainda não foram detalhados em nenhum relatório — a documentar quando houver material.*

!!! abstract "Na versão refatorada (design anterior à decisão)"
    O Relatório 4 descreve a página "Meus Materiais" redesenhada: um painel em lista com todas as aulas publicadas pelo professor, cada linha com o nome do conteúdo e ações nas extremidades — **visualizar** (clicando sobre o nome), **editar** e **excluir**.

    Esse design é anterior à decisão de 22/05 que substitui a tela. Fica registrado porque as ações descritas podem ser reaproveitadas na tela que a substituir.

    *Fonte: Relatório 4 — Maria Luiza (frontend), fig. 3.0. Design sujeito à redistribuição de perfis.*

---

## Tarefa 2 — Criar um material de estudo

**Status:** ✅ Atual  
**Perfil:** 🔄 A definir — a criação sai da área do professor

**Objetivo:** publicar um conteúdo teórico para os alunos estudarem.

**Pré-requisitos:** estar logado com perfil de professor; ter definidos a área e o tópico do material.

**Como fazer:**

1. Acesse **Criar material** (`/revisao/criar_material`).
2. Preencha os campos:

    | Campo | Regra |
    |---|---|
    | **Título** | nome do material, até 200 caracteres |
    | **Área** e **Tópico** | categorização do conteúdo |
    | **Palavras-chave** | **ao menos uma** — usadas na busca dos alunos |
    | **Conteúdo** | texto em Markdown, no mínimo 10 caracteres (ver [Tarefa 3](#tarefa-3-escrever-e-formatar-o-conteudo)) |
    | **Links externos** | URLs de referência, opcionais |

3. Salve. O material passa a estar disponível para os alunos no módulo de Revisão.

!!! tip "As palavras-chave determinam se o aluno encontra seu material"
    A busca do módulo de Revisão usa área, tópico e o nome do material — e as palavras-chave alimentam o tagueamento do conteúdo. Um material bem categorizado e com palavras-chave adequadas é o que garante que ele apareça para quem procura aquele assunto.

!!! abstract "Na versão refatorada"
    A tela de criação foi redesenhada com uma estrutura nova:

    - **Dados da aula**: campos dedicados para o título do material e para o **link da vídeo-aula** (recurso que não existe na versão atual);
    - **Menu expansível de disciplinas**, que se abre conforme os cliques e permite selecionar tópicos específicos;
    - **Editor com Markdown e preview em duas colunas** — à esquerda você digita, à direita o texto aparece formatado exatamente como o aluno verá;
    - **Exercícios de fixação** ao final (ver [Tarefa 4](#tarefa-4-montar-exercicios-de-fixacao)).

    *Fontes: Relatório 2 — Maria Luiza (frontend), figs. 2.0 e 5.0; Relatório 4 — Maria Luiza, figs. 1.0 e 2.0. Design sujeito à redistribuição de perfis.*

    ⬜ Captura de tela pendente. ⬜ *A confirmar: o design descrito não menciona os campos de **palavras-chave** nem de **links externos**, que existem no formulário atual — resta esclarecer se foram mantidos, já que as palavras-chave alimentam a busca dos alunos.*

!!! note "Onde esta tarefa ficará"
    A decisão de 22/05 remove esta tela da área do professor, mas **não indica o destino do design** descrito acima. A leitura mais provável é que a criação passe ao perfil de administrador com essa mesma interface. ⬜ *A confirmar com o subprojeto de frontend.*

    Ainda que a criação migre, os detalhes de interface acima continuam relevantes para você: o Relatório 4 registra que a tela de **edição espelha a estrutura e o comportamento do fluxo de criação** (ver [Tarefa 5](#tarefa-5-editar-um-material)).

---

## Tarefa 3 — Escrever e formatar o conteúdo

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** redigir o texto do material com a formatação que o aluno verá — títulos, listas, destaques e fórmulas matemáticas.

**Pré-requisitos:** estar criando ou editando um material.

**Como fazer:**

1. O campo de conteúdo abre o **Editor Markdown** da plataforma, com a tela dividida: à esquerda você escreve, à direita vê o resultado formatado **em tempo real**.
2. Escreva usando a notação **Markdown** para a estrutura do texto.
3. Para fórmulas matemáticas, use a notação **LaTeX** — o editor a converte e exibe as fórmulas formatadas, do mesmo modo que aparecerão para o aluno.
4. O painel de visualização mostra exatamente o que o aluno verá na página de leitura: use-o para conferir antes de salvar.

**Observações:**

- O conteúdo precisa ter **no mínimo 10 caracteres** para ser salvo.
- Você não precisa conhecer Markdown ou LaTeX em profundidade: o painel de preview permite ajustar por tentativa, vendo o resultado imediatamente.
- A plataforma aceita **anexar arquivos** aos materiais de revisão, sem restrição definida de tipo ou de tamanho. O arquivo enviado passa a ficar disponível como link no material. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

!!! abstract "Na versão refatorada"
    O editor com Markdown e preview lado a lado é **mantido** no redesign, inclusive com suporte a imagens, tanto na criação quanto na edição de aulas.

    *Fonte: Relatório 4 — Maria Luiza (frontend), fig. 2.0 e seção de edição. Design em andamento, sujeito a alteração.*

---

## Tarefa 4 — Montar exercícios de fixação

**Status:** 🟡 Refatorado (em design)  
**Perfil:** 👤 Professor — por meio da edição do material

**Objetivo:** anexar questões de fixação ao final de um material, para o aluno praticar logo após estudar o conteúdo.

!!! warning "Disponível apenas a partir da versão refatorada"
    Na plataforma atual, um material de revisão contém apenas texto, links e anexos — **não há exercícios vinculados a ele**. Esta é uma capacidade nova prevista no redesign.

**Como funcionará (conforme o design):**

Haverá **dois modos** de montar o questionário, que podem ser combinados:

**1. Criação manual de questões**

- Um campo no cabeçalho define ou altera a **quantidade de questões**;
- Para cada questão, você edita o **título**, o **enunciado** e as **alternativas**;
- O **gabarito** é indicado marcando a alternativa correta;
- Um botão de exclusão rápida remove a questão.

**2. Importação do banco de questões**

- Um menu lateral filtra as questões por **palavra-chave, disciplina, tipo (objetiva ou dissertativa), assunto, banca** (por exemplo, ENEM) **e nível de dificuldade**;
- Os resultados aparecem à direita conforme o filtro; **"Ver questão completa"** expande os detalhes;
- Marcar a caixa de seleção importa a questão diretamente para a aula.

*Fonte: Relatório 4 — Maria Luiza (frontend), figs. 2.1 e 2.2. Design em andamento, sujeito a alteração.*

!!! note "Número de alternativas"
    No cadastro manual de questões, o número de alternativas será **opcional entre quatro (A a D) e cinco (A a E)**, acomodando tanto o formato do ENEM quanto o de outras bancas — o mesmo critério vale no [Banco de Questões](banco-de-questoes.md#tarefa-2-criar-uma-questao).

    *Fonte: definição do subprojeto de frontend registrada em reunião (ago/2026).*

⬜ Captura de tela pendente. ⬜ *A confirmar: como as respostas dos alunos aos exercícios de fixação serão registradas e se ficarão visíveis para você.*

---

## Tarefa 5 — Editar um material

**Status:** ✅ Atual  
**Perfil:** 👤 Professor — **mantida** na área do professor

**Objetivo:** corrigir ou atualizar um material já publicado.

**Pré-requisitos:** ter o material publicado.

**Como fazer:**

1. A partir da listagem dos seus materiais, acione a edição (`/revisao/editar_material/:id_conteudo`).
2. Altere os campos desejados — título, área, tópico, palavras-chave, conteúdo e links externos.
3. Salve. A versão atualizada passa a ser a exibida aos alunos.

!!! tip "Esta é a tarefa central do seu perfil neste módulo"
    Entre as tarefas desta página, a edição é a **explicitamente mantida** na área do professor pela decisão de redistribuição. É por ela que você continuará atuando sobre os conteúdos, inclusive sobre os exercícios de fixação.

!!! abstract "Na versão refatorada"
    A página de edição **espelha a estrutura e o comportamento do fluxo de criação**: você atualiza o título, o link do vídeo, modifica as anotações mantendo o editor Markdown com suporte a imagens, e reestrutura os exercícios de fixação usando os mesmos dois modos — criação manual ou consulta ao banco de questões.

    Na prática, isso significa que toda a interface descrita na [Tarefa 2](#tarefa-2-criar-um-material-de-estudo) permanece acessível a você por esta tela.

    *Fonte: Relatório 4 — Maria Luiza (frontend), fig. 4.0. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente.

---

## Tarefa 6 — Remover um material

**Status:** ✅ Atual  
**Perfil:** 🔄 A definir

**Objetivo:** retirar da plataforma um material que não deve mais ser exibido aos alunos.

**Pré-requisitos:** ter o material publicado.

**Como fazer:**

1. A partir da listagem dos seus materiais, acione a remoção (`/revisao/remover_material/:id_conteudo`).
2. O material é removido e deixa de aparecer para os alunos.

!!! warning "Antes de remover, considere editar"
    Todos os campos de um material são editáveis ([Tarefa 5](#tarefa-5-editar-um-material)). Corrigir preserva o material no acervo e o histórico de leituras já registrado; remover descarta o conteúdo.

    A remoção apaga o material e desfaz seus vínculos com as palavras-chave, em uma única operação — **não há como desfazer**. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

!!! note "Esta tarefa pode mudar de perfil"
    A decisão de 22/05 não menciona a remoção de materiais. Como a única via documentada para removê-los é a tela "Meus Materiais" — que será substituída —, o destino desta tarefa fica indefinido. ⬜ *A confirmar com o subprojeto de frontend se o professor continuará podendo remover materiais.*

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| Não consigo salvar o material | Confira se o título tem até 200 caracteres, se há **ao menos uma palavra-chave** e se o conteúdo tem no mínimo 10 caracteres |
| O aluno relata não encontrar meu material | Confira a área, o tópico e as palavras-chave — são por eles que a busca do aluno chega ao conteúdo |
| A fórmula não aparece formatada na leitura | Confira a notação LaTeX no painel de preview do editor antes de salvar ([Tarefa 3](#tarefa-3-escrever-e-formatar-o-conteudo)) |
| Preciso corrigir um material já publicado | Use a edição — todos os campos são alteráveis, sem necessidade de remover e recriar |
| ⬜ Mensagens de erro específicas | As mensagens exatas serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–3, 5 e 6): listagem, criação, campos e validações, edição, remoção e upload | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Revisão de Conteúdo, seção "Para o Professor", derivada do código-fonte (rotas `/revisao/meus_materiais`, `criar_material`, `editar_material`, `remover_material`, `upload`) | jun/2026 |
| Editor Markdown: preview em tempo real, LaTeX via KaTeX, painel dividido (Tarefa 3) | [Descrição das Funcionalidades](../../funcionalidades.md) — Editor Markdown | jun/2026 |
| Interface futura: criação, Meus Materiais, carrossel e componentes | Relatório 2 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |
| Interface futura: criação detalhada, exercícios de fixação, Meus Materiais e edição (Tarefas 1, 2, 4 e 5) | Relatório 4 — Maria Luiza, mesmo subprojeto | mai/2026 |
| Redistribuição de perfis entre professor e administrador | Atas de reunião do subprojeto de frontend, 22/05/2026 | mai/2026 |

!!! note "Sobre a ordem das fontes"
    O Relatório 4 (17/05) descreve as telas do professor em detalhe; a ata de 22/05, cinco dias depois, redistribui parte dessas telas entre professor e administrador. Esta página documenta o design do relatório **e** a decisão posterior, sinalizando em cada tarefa qual das duas prevalece — o design permanece útil, mas a atribuição de perfil mudou.

A página de [Revisão de Conteúdo do Guia do Aluno](../aluno/revisao.md) documenta o outro lado do módulo: como os materiais publicados aqui são navegados e lidos.
