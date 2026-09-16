# Descrição do Sistema

## O que é o IFVest

O **IFVest** é uma plataforma web educacional gratuita voltada à preparação de estudantes para o **ENEM** e para os principais vestibulares do país, desenvolvida no âmbito acadêmico do **IFSP Campus Jacareí**.

A plataforma reúne, em um único ambiente, as ferramentas de prática que o estudante usa para estudar e os recursos de gestão pedagógica que o educador usa para produzir e curar conteúdo — questões, simulados, materiais de revisão, flashcards e correção de redações.

!!! info "Esta documentação descreve o IFVest V3"
    A plataforma foi reconstruída em 2026, com nova arquitetura, novo modelo de dados e nova organização de perfis. O histórico das versões anteriores está no [Registro de Versões](versoes.md), e o contexto da transição, no [Planejamento da Documentação](planejamento.md).

---

## Problema que resolve

A preparação para vestibulares e para o ENEM exige prática constante com questões de bancas oficiais, revisão teórica organizada e treino de redação com devolutiva — recursos que, em plataformas comerciais, costumam estar atrás de assinatura.

O IFVest oferece esse conjunto de forma gratuita e, diferente de um repositório de conteúdo estático, apoia-se em três características:

- **Organização curricular rigorosa**, que permite ao estudante praticar exatamente o assunto que precisa;
- **Aprendizagem ativa**, com repetição espaçada, simulados e devolutiva por questão;
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
| **Estudantes** | Praticam com questões de bancas oficiais e autorais, montam simulados, estudam com flashcards, acompanham a ofensiva diária de resolução e treinam redação com devolutiva |
| **Professores e educadores** | Elaboram e curam o banco de questões, escrevem colaborativamente os materiais de revisão e corrigem redações |
| **Administradores e moderadores** | Zelam pela qualidade pedagógica, auditam os conteúdos submetidos e gerenciam as permissões dos demais usuários |

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
- **Flashcards** têm associação flexível: podem ser vinculados a um tópico específico, a um assunto inteiro ou a uma disciplina completa.
- **Simulados** não guardam vínculo fixo com a taxonomia — usam a árvore como **filtro de busca** no momento de compor as questões.

---

## Perfis e permissões

O IFVest **não organiza os usuários em cargos fixos**. Não existe, no sistema, a figura de "aluno" ou "professor" como categoria rígida: toda a autorização é definida por **permissões granulares**, atribuídas individualmente a cada usuário.

Na prática, o que um usuário pode fazer é a soma das permissões que possui — e não a consequência de um rótulo.

### Como as permissões são atribuídas

| Situação | Permissões recebidas |
|---|---|
| Cadastro com **e-mail institucional** (`@ifsp.edu.br`) | Conjunto docente, com permissão de criar e editar conteúdo |
| Cadastro com e-mail comum | Nenhuma permissão especial — acesso aos recursos de estudo |
| **Administrador inicial**, definido na configuração do sistema | Conjunto administrativo completo |
| Concessão individual por um administrador | Permissões específicas, como corrigir redações ou moderar uma área |

### O que isso muda para o usuário

Quando alguém tenta executar uma ação para a qual não tem permissão, a plataforma informa **qual permissão está faltando** e orienta a procurar um administrador — em vez de simplesmente negar o acesso.

!!! note "Por que este modelo importa para a documentação"
    Como as capacidades não derivam de um cargo, a documentação de uso **não se organiza por perfil**. Cada tarefa indica a permissão que exige, permitindo que qualquer usuário identifique o que pode fazer a partir do que possui. Ver [Planejamento da Documentação](planejamento.md#-fase-4--usuario).

---

## Módulos

### Revisão de Conteúdo

Cada tópico da taxonomia possui um **material didático único**, escrito em Markdown, com **autoria colaborativa** e histórico de alterações comparáveis entre si, no estilo de um sistema de controle de versão.

A edição feita por um professor **entra no ar imediatamente**, mas o material passa a exibir publicamente uma marcação de **auditoria pendente** e entra na fila de moderação, até que um administrador o revise e aprove. O conteúdo não fica bloqueado enquanto aguarda revisão — a transparência substitui a espera.

### Flashcards

Baralhos de cartões, públicos ou privados, com agendamento de revisões por **repetição espaçada**: o intervalo até a próxima aparição de cada cartão é calculado a partir da dificuldade que o estudante relata ao respondê-lo.

Baralhos públicos podem ser importados **por referência**: correções e melhorias feitas no baralho original **propagam automaticamente** para todos que o importaram, em vez de gerar cópias que envelhecem separadamente.

### Simulados

Criação de provas com questões escolhidas individualmente ou geradas automaticamente a partir de filtros da taxonomia. A plataforma registra o **histórico completo de tentativas**, com tempo gasto, respostas fornecidas e pontuação obtida.

### Quizzes e gamificação

Módulo de prática rápida, com elementos de jogo:

- **Ofensiva diária** — contabilizada pela **resolução de ao menos uma questão no dia**, e não por acessar a plataforma.
- **Questão diária** — uma questão sorteada a cada dia, exibida em destaque, com histórico visual em mapa de calor: verde para acerto, vermelho para erro e cinza para os dias sem resposta.
- **Pontuação, loja de itens cosméticos e histórico de transações**, além de ranking entre usuários.

### Redação

Publicação de **propostas temáticas**, com textos motivadores e imagens de apoio. Os estudantes submetem suas redações, e corretores autorizados as avaliam segundo a **grade de competências do ENEM (C1 a C5)**, com devolutiva descritiva.

---

## Banco de questões

O acervo combina **questões de bancas oficiais** — extraídas de provas anteriores de ENEM, FUVEST, UNICAMP e outros processos seletivos — com questões autorais produzidas pelos professores do projeto, identificadas como **Banca IFVest**.

Cada questão de múltipla escolha registra suas alternativas com indicação de qual é a correta, e vincula-se a um ou mais tópicos da taxonomia.

---

## Tecnologias

| Camada | Tecnologia |
|---|---|
| **Frontend** | Next.js e React, hospedados na Vercel |
| **Backend** | Python 3.12 com FastAPI, em arquitetura assíncrona, hospedado em VPS |
| **Banco de dados** | PostgreSQL 16 |
| **Autenticação** | Firebase Authentication, com login por e-mail/senha e Google |
| **Infraestrutura local** | Docker Compose |

O detalhamento da estrutura interna, das dependências e das integrações está na [Arquitetura do Sistema](arquitetura.md).

---

## Restrições e dependências

- O acesso aos módulos da plataforma **exige conta e sessão ativa**, autenticada pelo Firebase.
- A criação e a edição de conteúdo dependem de **permissões específicas**, não do tipo de conta.
- A atribuição automática de permissões docentes depende de cadastro com **e-mail institucional do IFSP**.
- O acervo de questões depende do trabalho de **curadoria e extração** conduzido pelas frentes do projeto; a plataforma não gera questões automaticamente.
- ⬜ *A confirmar: limites de uso, como número de submissões de redação por período.*

---

## Projetos do ecossistema

Além da plataforma, o projeto mantém iniciativas que se integram a ela:

| Projeto | Relação com a plataforma |
|---|---|
| **Leitor de PDFs educacionais** | Aplicativo independente, que consumirá materiais exportados da plataforma em PDF. ⬜ *Integração ainda não implementada.* |
| **Extrator de questões por IA** | Sistema que lê provas anteriores em PDF e extrai as questões estruturadas para alimentar o banco automaticamente |

O detalhamento está em [Subprojetos Ativos](subprojetos/index.md).

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Proposta de valor, escopo, público-alvo, taxonomia, permissões e módulos | Documentação do repositório do backend (README — Visão de Negócio) | set/2026 |
| Escopo do MVP, stack e infraestrutura | Documento de onboarding do projeto | set/2026 |
| Regras de atribuição de permissões e mensagens de restrição | Código-fonte do backend (`src/core/permissions.py`) | set/2026 |
| Estrutura do banco de questões e da taxonomia | Modelo relacional do backend (`docs/database_model.md`) | set/2026 |

!!! note "Divergência entre fontes quanto ao escopo da primeira versão"
    O documento de onboarding indica que a primeira versão contempla os módulos de **Redação, Quiz e Simulados**, ficando Revisão e Flashcards para depois. O roadmap do repositório do backend, por sua vez, situa **Redação e Quiz** em uma segunda fase de implementação.

    ⬜ *A esclarecer com a coordenação do projeto.* Esta página descreve os módulos previstos para a plataforma, sem afirmar quais estarão disponíveis na primeira entrega.
