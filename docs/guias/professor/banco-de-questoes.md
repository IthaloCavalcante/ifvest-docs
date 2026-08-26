# Banco de Questões

O **banco de questões** reúne as questões que alimentam os simulados da plataforma. Cada questão pertence a uma área e a um ou mais tópicos, é classificada como **objetiva** (alternativas A–E) ou **dissertativa** (resposta escrita), e pode ser reaproveitada em quantos simulados você quiser — criar a questão e montar o simulado são etapas separadas.

O banco é acessível pelo módulo de Simulados (`/simulados/questoes`).

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. Os blocos *"Na versão refatorada"* descrevem o novo design em elaboração e **podem mudar até a entrega**. Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Ver suas questões

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** consultar as questões que você já cadastrou, para reaproveitá-las, revisá-las ou removê-las.

**Pré-requisitos:** estar logado com perfil de professor.

**Como fazer:**

1. Acesse **Minhas questões** (`/simulados/questoes`).
2. A lista exibe as questões criadas por você, com acesso às ações de editar e excluir.

**Observações:**

- A listagem é **por autor**: aqui você vê apenas as suas questões.
- Ao montar um simulado, porém, a seleção de questões **não filtra por autor** — aparecem as questões de todos os professores, disponíveis para reaproveitamento. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

---

## Tarefa 2 — Criar uma questão

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** cadastrar uma nova questão no banco, disponível para uso em simulados.

**Pré-requisitos:** estar logado com perfil de professor; ter definidos a área e os tópicos aos quais a questão pertence (ver [Tarefa 6](#tarefa-6-criar-topicos-para-categorizar-questoes)).

**Como fazer:**

1. A partir de **Minhas questões**, escolha criar uma nova questão.
2. Escolha o **tipo** da questão — essa decisão vem primeiro e define os campos seguintes:

    | Tipo | Como é respondida |
    |---|---|
    | **Objetiva** | O aluno seleciona uma alternativa (A a E) |
    | **Dissertativa** | O aluno escreve a resposta em texto livre |

3. Preencha os campos comuns aos dois tipos:

    | Campo | Função |
    |---|---|
    | **Título** | identifica a questão nas listagens |
    | **Enunciado** | o texto da questão apresentado ao aluno |
    | **Área** | área de conhecimento à qual a questão pertence |
    | **Tópicos** | categorização mais específica dentro da área |

4. **Se a questão for objetiva**, preencha as **opções de resposta (A a E)** e indique qual é a **correta**.
5. Salve a questão. Ao salvar, o sistema pode acionar a verificação de similaridade (ver [Tarefa 3](#tarefa-3-conferir-a-similaridade-com-questoes-existentes)).

!!! tip "Fórmulas matemáticas no enunciado"
    O campo de enunciado usa um **editor de equações com suporte a LaTeX**. Fórmulas escritas nessa notação são exibidas formatadas para o aluno — não é necessário inserir imagens de equações.

!!! abstract "Na versão refatorada"
    ⬜ **Nenhum dos relatórios de redesign consultados descreve a tela de criação de questões do banco.** Os relatórios cobrem em detalhe a *consulta* e a *importação* de questões (ver [Tarefa 4](#tarefa-4-editar-uma-questao) e a página de Simulados), mas não o formulário de cadastro — a documentar quando o material estiver disponível.

    Uma definição já tomada sobre o formulário: no cadastro manual de questões, o número de alternativas passa a ser **opcional entre quatro (A a D) e cinco (A a E)**, para acomodar tanto o formato do ENEM quanto o de outras bancas. Na versão atual, o formulário trabalha apenas com cinco alternativas.

    *Fonte: definição do subprojeto de frontend registrada em reunião (ago/2026).*

---

## Tarefa 3 — Conferir a similaridade com questões existentes

**Status:** ⬜ Indisponível — a confirmar  
**Perfil:** 👤 Professor

**Objetivo:** verificar se a questão que você está cadastrando já existe no banco em forma semelhante, evitando duplicidades.

!!! danger "Funcionalidade não localizada no código-fonte"
    A [Descrição das Funcionalidades](../../funcionalidades.md) registra esta verificação como existente, mas na versão do código-fonte analisada **não há rota nem processamento correspondente** — apenas a tela de exibição dos resultados, sem nada que a acione, e sem nenhuma biblioteca de inteligência artificial entre as dependências do projeto.

    Duas explicações são possíveis: a funcionalidade foi descrita a partir de relatórios de subprojeto e não chegou a ser integrada, ou existiu e foi removida antes desta versão. ⬜ *A esclarecer com a coordenação do projeto; a correção alcança também a Fase 3.*

    O funcionamento descrito abaixo reflete o que consta na Fase 3 e é mantido aqui **até que a situação seja esclarecida** — não confie nele para evitar duplicidades sem antes confirmar que a verificação está ativa.

**Pré-requisitos:** estar cadastrando ou editando uma questão.

**Como fazer:**

1. Ao **cadastrar** ou **editar** uma questão, o sistema pode acionar automaticamente a verificação de similaridade.
2. A verificação compara sua questão com as já existentes no banco usando um serviço externo de inteligência artificial, que identifica semelhança de **sentido**, não apenas de palavras iguais.
3. A **tela de verificação de similaridade** exibe o resultado, indicando os trechos semelhantes encontrados.
4. Avalie o resultado e decida se mantém a questão, ajusta o enunciado ou aproveita a questão já existente.

**Observações:**

- A verificação é uma funcionalidade **exclusiva do perfil de professor** — não existe equivalente para o aluno.
- Como a comparação é semântica, ela detecta questões que dizem a mesma coisa com outras palavras — situação comum quando vários professores cadastram conteúdo do mesmo tópico.
- ⬜ *A confirmar: se a verificação é automática ou acionada por você, e se um resultado de alta similaridade impede o salvamento ou apenas emite um aviso — pendente do esclarecimento acima.*

!!! abstract "Na versão refatorada"
    ⬜ Os relatórios de redesign consultados não mencionam a verificação de similaridade — a documentar quando definido se a funcionalidade será mantida, e como.

---

## Tarefa 4 — Editar uma questão

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** corrigir ou atualizar uma questão já cadastrada.

**Pré-requisitos:** ter a questão cadastrada por você.

**Como fazer:**

1. Em **Minhas questões**, localize a questão e acione a edição.
2. Altere os campos desejados — os mesmos do cadastro (título, enunciado, área, tópicos e, nas objetivas, as alternativas e o gabarito).
3. Salve. A verificação de similaridade também pode ser acionada na edição (ver [Tarefa 3](#tarefa-3-conferir-a-similaridade-com-questoes-existentes)).

**Observações:**

- A edição altera a questão **em todos os simulados que a utilizam** — o vínculo é com a questão, não com uma cópia dela. Respostas já registradas por alunos permanecem associadas à questão editada. *(Conforme o código-fonte da plataforma anterior ao redesign.)*

!!! abstract "Na versão refatorada"
    O redesign detalha a **consulta ao banco de questões** com um menu lateral de filtros — palavra-chave, disciplina, assunto, tipo de questão (objetivas ou dissertativas), banca (por exemplo, ENEM) e nível de dificuldade —, exibindo as questões encontradas em lista, com a opção **"Ver questão completa"** para expandir enunciado e alternativas.

    *Fontes: Relatório 4 — Maria Luiza (frontend), importação via banco de questões; Relatório 3 — Isabella Pereira (frontend), filtros e seleção de questões. Design em andamento, sujeito a alteração.*

    ⬜ Captura de tela pendente.

---

## Tarefa 5 — Excluir uma questão

**Status:** ✅ Atual  
**Perfil:** 👤 Professor

**Objetivo:** remover definitivamente uma questão do banco.

**Pré-requisitos:** ter a questão cadastrada por você.

**Como fazer:**

1. Em **Minhas questões**, localize a questão e acione a exclusão.
2. A questão é removida do banco, junto com as **opções de resposta associadas** a ela.

!!! warning "A exclusão alcança os simulados que usam a questão"
    Excluir uma questão remove, junto com ela: as **alternativas**, os **vínculos com todos os simulados** que a utilizavam e as **respostas já registradas** por alunos para aquela questão. Os simulados continuam existindo, mas passam a ter uma questão a menos.

    Se a questão estiver em simulados já aplicados, prefira **editá-la** ([Tarefa 4](#tarefa-4-editar-uma-questao)) a excluí-la.

    *Conforme o código-fonte da plataforma anterior ao redesign.*

---

## Tarefa 6 — Criar tópicos para categorizar questões

**Status:** ✅ Atual  
**Perfil:** 🔄 A definir — pode migrar para administrador

**Objetivo:** criar as subdivisões temáticas usadas para classificar as questões dentro de uma área.

**Pré-requisitos:** estar logado com perfil de professor.

**Como fazer:**

1. Acesse **Meus tópicos** (`/simulados/meus-topicos`) para visualizar os tópicos existentes.
2. Crie um tópico vinculado a uma **área de conhecimento**.
3. O tópico passa a estar disponível na categorização de questões ([Tarefa 2](#tarefa-2-criar-uma-questao)).

!!! warning "Esta tarefa pode mudar de perfil"
    O redesign prevê que a inclusão de novas matérias e conteúdos passe ao **perfil de administrador**. Se a organização de conteúdos migrar, esta tarefa sairá deste guia e passará ao Guia do Administrador.

    *Fonte: atas de reunião do subprojeto de frontend (mai/2026).*

---

## Sobre a reconstrução do banco de questões

Além do redesign da interface, o **próprio banco de questões está sendo reconstruído** por subprojetos dedicados, com um repositório de questões alimentado pelas APIs de vestibulares (ENEM, FUVEST, UNICAMP) e um sistema de **tags** para classificação, com busca semântica prevista.

Para você, isso significa que a forma de **classificar e localizar** questões tenderá a mudar — o conjunto atual de área e tópicos deve conviver com, ou dar lugar a, um sistema de tags e filtros por banca.

⬜ *A documentar quando o novo banco e o sistema de tags estiverem definidos.*

*Fonte: atas de reunião dos subprojetos de banco de questões e APIs de vestibulares (abr–jun/2026).*

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| A questão não aparece para vincular a um simulado | Confira se ela foi salva e se a área e os tópicos correspondem aos do simulado que você está montando |
| Não encontro o tópico adequado para a questão | Crie o tópico na área correspondente ([Tarefa 6](#tarefa-6-criar-topicos-para-categorizar-questoes)) antes de cadastrar a questão |
| A verificação apontou similaridade com uma questão que não é igual à minha | A comparação é por sentido, não por texto idêntico. Cabe a você avaliar se as questões de fato se sobrepõem |
| A fórmula do enunciado não aparece formatada | Confira a notação LaTeX no editor de equações antes de salvar |
| ⬜ Mensagens de erro específicas | As mensagens exatas serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–5): listagem, cadastro, edição, exclusão, tópicos, editor LaTeX e verificação de similaridade | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo Simulados, seção "Para o Professor", derivada do código-fonte (rotas `/simulados/questoes`, `/simulados/registrar-questao`, `/simulados/meus-topicos`) | jun/2026 |
| Consulta e filtros do banco na versão refatorada (Tarefa 4) | Relatório 4 — Maria Luiza e Relatório 3 — Isabella Pereira, subprojeto *Refatoração para React e Redesign do IFVest* | abr/2026 |
| Divergência no número de alternativas (Tarefa 2) | Relatório 4 — Maria Luiza, módulo de exercícios de fixação | abr/2026 |
| Reconstrução do banco, tags e APIs de vestibulares | Atas de reunião dos subprojetos correspondentes | abr–jun/2026 |
