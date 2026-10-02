# Descrição do Sistema

## O que é o IFVest

O **IFVest** é uma plataforma web educacional gratuita voltada à preparação de estudantes para o **ENEM** e para os principais vestibulares do país, desenvolvida no âmbito acadêmico do **IFSP Campus Jacareí**.

A plataforma reúne, em um único ambiente, as ferramentas de prática que o estudante usa para estudar e os recursos de gestão pedagógica que o educador usa para produzir e curar conteúdo — questões, simulados, propostas e correção de redações e, nas próximas versões, materiais de revisão e flashcards.

!!! info "Esta documentação descreve o IFVest V3"
    A plataforma foi reconstruída em 2026, com nova arquitetura, novo modelo de dados e nova organização de perfis. O histórico das versões anteriores está no [Registro de Versões](versoes.md), e o contexto da transição, no [Planejamento da Documentação](planejamento.md).

---

## Problema que resolve

A preparação para vestibulares e para o ENEM exige prática constante com questões de bancas oficiais, revisão teórica organizada e treino de redação com devolutiva — recursos que, em plataformas comerciais, costumam estar atrás de assinatura.

O IFVest oferece esse conjunto de forma gratuita e, diferente de um repositório de conteúdo estático, apoia-se em três características:

- **Organização curricular rigorosa**, que permite ao estudante praticar exatamente o assunto que precisa;
- **Aprendizagem ativa**, com quizzes, simulados e devolutiva por questão;
- **Curadoria docente**, com conteúdo produzido e auditado por professores, e não apenas agregado automaticamente.

---

## Escopo

O foco da plataforma é a **preparação para o ensino superior**: ENEM, FUVEST, UNICAMP, VUNESP e os processos seletivos dos Institutos Federais.

!!! warning "Fora do escopo"
    A plataforma **não** se destina às provas de ingresso ao ensino médio integrado ou aos cursos técnicos. Todo o conteúdo, taxonomia e nível de dificuldade são orientados ao acesso ao ensino superior.

---

## Público-alvo

O ecossistema atende a três perfis operacionais. Eles descrevem **papéis de uso**, não cargos fixos no sistema — a distinção é importante e está explicada em [Perfis e permissões](#perfis-e-permissoes).

| Perfil | O que faz na plataforma |
|---|---|
| **Estudantes** | Praticam com questões de provas e autorais em quizzes e simulados, mantêm a sequência de respostas à Pergunta do Dia e treinam redação com devolutiva |
| **Professores e educadores** | Cadastram e curam o banco de questões, montam simulados, publicam propostas de redação e corrigem redações |
| **Administradores e moderadores** | Zelam pela qualidade pedagógica, moderam as denúncias de erros nas questões, controlam os módulos ativos e gerenciam as permissões dos demais usuários |

---

## Organização do conhecimento

Todo o conteúdo pedagógico da plataforma obedece a uma **hierarquia curricular de três níveis**:

**Disciplina → Assunto → Tópico**

| Nível | O que representa | Exemplo |
|---|---|---|
| **Disciplina** | Grande área do conhecimento | Matemática |
| **Assunto** | Subdivisão curricular da disciplina | Álgebra |
| **Tópico** | Nível atômico de aprendizagem | Equações do 2º grau |

Cada funcionalidade se associa a essa árvore de uma forma distinta:

- **Questões** vinculam-se **estritamente a tópicos**, podendo abranger mais de um ao mesmo tempo. A disciplina e o assunto são herdados automaticamente pela árvore, e não informados separadamente.
- **Simulados** e **quizzes** não guardam vínculo fixo com a taxonomia — usam a árvore como **filtro de busca** no momento de reunir as questões.
- **Flashcards**, previstos para as próximas versões, terão associação flexível: poderão ser vinculados a um tópico específico, a um assunto inteiro ou a uma disciplina completa.

---

## Perfis e permissões

O IFVest **não organiza os usuários em cargos fixos**. Não existe, no sistema, a figura de "aluno" ou "professor" como categoria rígida: toda a autorização é definida por **permissões granulares**, atribuídas individualmente a cada usuário.

Na prática, o que um usuário pode fazer é a soma das permissões que possui — e não a consequência de um rótulo.

### Como as permissões são atribuídas

| Situação | Permissões recebidas |
|---|---|
| Cadastro com **e-mail institucional** (`@ifsp.edu.br`) | Conjunto docente: cadastrar e editar questões, criar simulados e gerenciar os simulados de outras pessoas |
| Cadastro com e-mail comum | Nenhuma permissão especial — acesso aos recursos de estudo |
| **Administrador inicial**, definido na configuração do sistema | Todas as permissões |
| Concessão individual por um administrador | Permissões específicas, como corrigir redações ou publicar propostas de redação |

As permissões automáticas valem só na criação da conta: o que um administrador conceder ou revogar depois permanece nos acessos seguintes. O catálogo completo está em [Arquitetura — Permissões](arquitetura.md#permissoes).

### O que isso muda para o usuário

Quando alguém tenta executar uma ação para a qual não tem permissão, a plataforma informa **qual permissão está faltando** e orienta a procurar um administrador — em vez de simplesmente negar o acesso.

!!! note "Por que este modelo importa para a documentação"
    Como as capacidades não derivam de um cargo, a documentação de uso **não se organiza por perfil**. Cada tarefa indica a permissão que exige, permitindo que qualquer usuário identifique o que pode fazer a partir do que possui. Ver [Planejamento da Documentação](planejamento.md#fase-4-usuario).

---

## Módulos

| Módulo | Situação |
|---|---|
| Quizzes e gamificação (IFQuiz) | Implementado |
| Simulados | Implementado |
| Redação | Implementado |
| Revisão de Conteúdo | Previsto, em construção |
| Flashcards | Previsto, em construção |

Cada módulo pode ser ligado e desligado sem alterar o código. Ver [Arquitetura — Feature flags](arquitetura.md#feature-flags).

### Quizzes e gamificação (IFQuiz)

Módulo de prática rápida, com elementos de jogo:

- **Quiz personalizado** — o estudante escolhe disciplina, assunto e quantidade de questões, entre as que existem no banco, responde e, ao final, vê o resultado e a revisão de cada questão.
- **Pergunta do Dia** — uma questão por dia, a mesma para todos os estudantes, exibida em destaque, com histórico visual em mapa de calor: verde para acerto, vermelho para erro e cinza para os dias sem resposta.
- **Sequência diária** — conta os dias seguidos em que o estudante respondeu à Pergunta do Dia, no horário de Brasília, e volta a zero quando ele passa um dia sem responder. Responder a outras questões ou apenas acessar a plataforma não conta.
- **Pontos, loja e ranking** — acertos rendem pontos, que podem ser gastos em itens cosméticos da loja de avatares. O ranking, geral e semanal, considera os pontos ganhos, e não o saldo: compras na loja não fazem o estudante perder posição.

### Simulados

Professores com permissão montam simulados escolhendo as questões do banco. O estudante pode montar o seu próprio simulado de treino ou gerar um simulado aleatório a partir de filtros da taxonomia.

A resolução pode ser feita na própria plataforma, com a correção de cada questão, e o caderno de questões pode ser exportado em PDF. A cada envio, a plataforma registra a tentativa — número de questões, quantas foram respondidas, acertos e nota —, e o estudante acompanha o histórico e as estatísticas das suas tentativas.

### Redação

Publicação de **propostas temáticas**, com textos de apoio — escritos ou em imagem — e etiquetas de tema. Os estudantes enviam suas redações, e corretores autorizados as avaliam segundo a **grade de competências do ENEM (C1 a C5)**, com devolutiva descritiva e comentários em trechos do próprio texto.

Cada redação recebe uma única correção, e ninguém corrige a própria redação.

### Revisão de Conteúdo

*Módulo previsto, ainda sem implementação. A descrição registra o que foi definido pela equipe.*

Cada tópico da taxonomia terá um **material didático único**, escrito em Markdown, com **autoria colaborativa** e histórico de alterações comparáveis entre si, no estilo de um sistema de controle de versão.

A edição feita por um professor **entrará no ar imediatamente**, mas o material passará a exibir publicamente uma marcação de **auditoria pendente** e entrará na fila de moderação, até que um administrador o revise e aprove. O conteúdo não ficará bloqueado enquanto aguarda revisão — a transparência substitui a espera.

### Flashcards

*Módulo previsto, ainda sem implementação. A descrição registra o que foi definido pela equipe.*

Baralhos de cartões, públicos ou privados, com agendamento de revisões por **repetição espaçada**: o intervalo até a próxima aparição de cada cartão será calculado a partir da dificuldade que o estudante relata ao respondê-lo.

Baralhos públicos poderão ser importados **por referência**: correções e melhorias feitas no baralho original **se propagarão automaticamente** para todos que o importaram, em vez de gerar cópias que envelhecem separadamente.

---

## Banco de questões

O acervo combina **questões de provas de vestibulares** com **questões autorais**, cadastradas pelos professores com permissão. As provas entram no banco por uma carga a partir dos arquivos de cada prova — hoje, as da UNICAMP; o escopo prevê também ENEM, FUVEST e outros processos seletivos.

Cada questão de múltipla escolha registra suas alternativas com indicação de qual é a correta, e vincula-se a um ou mais tópicos da taxonomia. O mesmo banco abastece os simulados e os quizzes.

Qualquer usuário pode **denunciar um erro** numa questão. As denúncias entram na moderação do painel administrativo, onde a questão pode ser corrigida e a denúncia, resolvida ou descartada.

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| **Frontend** | React e TypeScript, construído com Vite |
| **Backend** | Python 3.12 com FastAPI, em arquitetura assíncrona |
| **Hospedagem** | Servidor próprio (VPS), com frontend, backend e banco sob o domínio `ifvest.com.br` |
| **Banco de dados** | PostgreSQL 16 |
| **Autenticação** | Firebase Authentication, com login pela conta Google |
| **Infraestrutura local** | Docker Compose |

O detalhamento da estrutura interna, das dependências e das integrações está na [Arquitetura do Sistema](arquitetura.md).

---

## Restrições e dependências

- O uso da plataforma **exige conta e sessão ativa**, autenticada pelo Firebase. Respondem sem login apenas a consulta às propostas de redação e a situação dos módulos.
- A criação e a edição de conteúdo dependem de **permissões específicas**, não do tipo de conta.
- A atribuição automática de permissões docentes depende de cadastro com **e-mail institucional do IFSP**.
- O acervo de questões depende do trabalho de **curadoria e extração** conduzido pelas frentes do projeto; a plataforma não gera questões automaticamente.
- **Não há limites de uso** definidos no código: o envio de redações, por exemplo, não tem limite por período. Ver [Arquitetura — Pontos de atenção](arquitetura.md#pontos-de-atencao).

---

## Projetos do ecossistema

Além da plataforma, o projeto mantém iniciativas que se integram a ela:

| Projeto | Relação com a plataforma |
|---|---|
| **Leitor de PDFs educacionais** | Aplicativo independente, que consumirá materiais exportados da plataforma em PDF. ⬜ *Integração ainda não implementada.* |
| **Extrator de questões por IA** | Sistema que lê provas anteriores em PDF e extrai as questões estruturadas para alimentar o banco. ⬜ *O repositório da plataforma não registra a integração: hoje as provas entram por carga de arquivos, sem vínculo documentado com o extrator.* |

O detalhamento está em [Subprojetos Ativos](subprojetos/index.md).

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Proposta de valor, escopo, público-alvo e taxonomia | Documentação do repositório do backend (README — Visão de Negócio) | set/2026 |
| Módulos implementados e suas regras | Código-fonte do backend e do frontend do `ifvest-monorepo` | set/2026 |
| Módulos previstos (Revisão e Flashcards) | Documentação do repositório do backend (README — Visão de Negócio) e documento de onboarding | set/2026 |
| Regras de atribuição de permissões e mensagens de restrição | Código-fonte do backend (`src/core/permission_catalog.py` e `src/core/permissions.py`) | set/2026 |
| Banco de questões e carga das provas | Modelos do backend e `docs/atualizar-questoes-na-vps.md` | set/2026 |
| Stack e hospedagem | Configuração de produção do `ifvest-monorepo` | set/2026 |

!!! note "Escopo da primeira versão — divergência resolvida"
    O documento de onboarding e o roadmap do repositório do backend divergiam sobre quais módulos entrariam primeiro. O **código em produção resolve a questão**: ele define os módulos por meio de *feature flags*, com **Quiz, Redação e Simulados** implementados e **Revisão e Flashcards** marcados como em construção — o que confirma o onboarding. Ver [Arquitetura — Feature flags](arquitetura.md#feature-flags).

!!! note "Divergências entre o README do backend e o código"
    A visão de negócio do README do backend descreve alguns comportamentos de forma diferente do que o código implementa. Esta página adota o código:

    | Tema | README do backend | Código |
    |---|---|---|
    | Login | E-mail e senha, além do Google | Apenas a conta Google |
    | Sequência diária | Resolução de ao menos uma questão no dia | Resposta à Pergunta do Dia |
    | Pergunta do Dia | Sorteada a cada dia | Definida pela data, a mesma para todos |
    | Histórico de simulados | Tempo gasto, respostas fornecidas e pontuação | Número de questões, respondidas, acertos e nota |
    | Questões autorais | Identificadas como "Banca IFVest" | A banca é um campo livre do cadastro |
