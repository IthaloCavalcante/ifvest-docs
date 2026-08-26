# Revisão de Conteúdo

O módulo de **Revisão** (`/revisao`) reúne os materiais de estudo teóricos da plataforma: textos escritos pelos professores, organizados por assunto, com suporte a fórmulas matemáticas. É o ponto de partida para estudar a teoria antes de praticar nos demais módulos.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração pelo subprojeto de frontend e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Navegar pelos conteúdos de estudo

**Status:** ✅ Atual

**Objetivo:** encontrar materiais de estudo explorando a organização de conteúdos da plataforma, quando você ainda não sabe exatamente o que procura.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta) — o módulo de Revisão exige sessão ativa.

**Como fazer:**

1. Acesse o módulo **Revisão** a partir do menu da plataforma.
2. Abra a **busca por assunto**. Os materiais são organizados em uma [hierarquia de assuntos](../glossario.md#como-os-conteudos-sao-organizados) — um assunto pode conter subassuntos, formando uma árvore de categorias.
3. Navegue pela árvore até o assunto do seu interesse. Os materiais vinculados a ele são listados.
4. Selecione um material para abri-lo (ver [Tarefa 3](#tarefa-3-ler-um-material-de-estudo)).

!!! abstract "Na versão refatorada"
    A navegação muda de forma: a página inicial da Revisão passa a exibir um **carrossel único de matérias** no topo (Física, Química, Biologia, Matemática etc.), com rolagem horizontal. Dentro das páginas de conteúdo, uma **barra lateral (sidebar)** permite alternar entre disciplinas e tópicos sem voltar à página inicial.

    *Fonte: Relatório 3 — Maria Luiza (frontend), figs. 1.0, 1.1 e 3.0. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente (aguardando estabilização da interface).

!!! note "Observação — o design ainda está em iteração"
    A proposta anterior (Relatório 1 — Maria Luiza, fig. 4.0) dividia a Revisão em cinco grandes áreas: Matemática, Ciências Humanas, Ciências Naturais, Linguagens e Informática. O Relatório 3 **substituiu** essa divisão pelo carrossel unificado de matérias. O registro da mudança fica aqui como evidência de que a camada de interface segue em evolução.

---

## Tarefa 2 — Buscar um material específico

**Status:** ✅ Atual

**Objetivo:** localizar rapidamente um material quando você já sabe o que procura.

**Pré-requisitos:** os mesmos da Tarefa 1.

**Como fazer:**

1. No módulo Revisão, use a **busca**.
2. A plataforma aceita três formas de pesquisa: por **área** de conhecimento, por **tópico** ou pelo **nome do material**.
3. Os resultados listam os materiais correspondentes; selecione um para abri-lo.

!!! abstract "Na versão refatorada"
    A busca ganha um campo de **filtro direto** ("Filtrar Matérias") na página da Revisão: você digita o nome da disciplina desejada e a lista se ajusta na hora, sem precisar percorrer o carrossel.

    *Fonte: Relatório 3 — Maria Luiza (frontend), fig. 2.0. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente.

**Observações:**

- Se a busca não retornar resultados, tente um termo mais amplo (ex.: a área em vez do nome exato do material) ou navegue pela árvore de assuntos ([Tarefa 1](#tarefa-1-navegar-pelos-conteudos-de-estudo)).

---

## Tarefa 3 — Ler um material de estudo

**Status:** ✅ Atual

**Objetivo:** acessar e ler o conteúdo completo de um material.

**Pré-requisitos:** ter localizado o material (via navegação ou busca).

**Como fazer:**

1. Abra o material a partir da lista de resultados ou da árvore de assuntos.
2. O conteúdo é exibido com formatação completa: o texto é escrito pelos professores em Markdown e renderizado pela plataforma, incluindo **fórmulas matemáticas** (notação LaTeX) exibidas corretamente.
3. Quando houver, **links externos de referência** adicionados pelo professor aparecem junto ao material.
4. Sua leitura é registrada automaticamente — a plataforma mantém um contador de leituras por material. Nenhuma ação sua é necessária para isso.

!!! abstract "Na versão refatorada"
    A página de conteúdo passa a ter uma anatomia fixa de estudo, nesta ordem:

    1. **Vídeo-aula** no topo, introduzindo o conteúdo;
    2. **Anotações** — o texto teórico com os pontos principais e exemplos práticos;
    3. **Exercícios de fixação** ao final, focados na matéria estudada.

    *Fonte: Relatório 1 — Maria Luiza (frontend), itens 4–6 e figs. 4.2/4.3. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente. ⬜ O fluxo de resposta dos exercícios (como o aluno responde e recebe correção) ainda não está detalhado nos relatórios — a documentar quando definido.

---

## Tarefa 4 — Acompanhar seu progresso de estudo

**Status:** 🟡 Refatorado (em design)

**Objetivo:** visualizar quanto de cada assunto você já estudou e identificar o que precisa revisar.

!!! warning "Disponível apenas a partir da versão refatorada"
    A plataforma atual **não exibe** métricas de progresso ao aluno. Esta tarefa descreve uma capacidade nova, prevista no redesign.

**Como funcionará (conforme o design):**

- Cada assunto terá um **painel de progresso** com sua pontuação de acertos e indicações do que revisar (ex.: *"Revisar: Funções"*).
- Cada card de conteúdo exibirá uma **barra de progresso individual**, indicando o percentual de conclusão daquele conteúdo específico.

*Fontes: Relatório 1 — Maria Luiza (frontend), item 3 e fig. 4.1; Relatório 3 — Maria Luiza, item 4 e fig. 4.0. Design em andamento, sujeito a alteração.*

⬜ A regra de cálculo do progresso (o que conta como "concluído") ainda não está definida nos relatórios — a documentar quando especificada.

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A busca não retorna resultados | Use um termo mais amplo ou navegue pela árvore de assuntos |
| Um assunto aparece sem materiais | Nem todo assunto da árvore possui conteúdo publicado; explore os subassuntos vizinhos |
| ⬜ Mensagens de erro específicas | As mensagens exatas exibidas pela plataforma serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

Conforme o critério desta documentação, cada camada tem origem rastreável:

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–3) | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Revisão, derivada do código-fonte (rotas `/revisao/*`, repositório IFVEST-main) | jun/2026 |
| Interface futura (blocos "Na versão refatorada") | Relatórios 1 e 3 — Maria Luiza, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |
| Progresso de estudo (Tarefa 4) | Relatórios 1 e 3 — Maria Luiza (mesmo subprojeto) | abr/2026 |

Os Relatórios 2 e 4 do mesmo subprojeto tratam da área do professor e não afetam as tarefas do aluno nesta página.
