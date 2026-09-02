# Arquitetura do Sistema

O IFVest é uma aplicação web full-stack construída sobre Node.js, com arquitetura baseada em domínios e padrão MVC (Model-View-Controller). Esta página descreve como o sistema está organizado internamente, quais tecnologias compõem cada camada e como as partes se comunicam.

---

## Visão Geral

```
┌─────────────────────────────────────────────┐
│                  USUÁRIO                    │
│         (Navegador Web / Dispositivo)       │
└───────────────────┬─────────────────────────┘
                    │ HTTP/HTTPS
┌───────────────────▼─────────────────────────┐
│               FRONTEND                      │
│     Bootstrap 5 + JavaScript (ES6+)         │
│            Templates EJS                    │
└───────────────────┬─────────────────────────┘
                    │
┌───────────────────▼─────────────────────────┐
│               BACKEND                       │
│         Node.js + Express.js                │
│     Arquitetura MVC por domínios            │
│    Middleware: Helmet, CORS, Sessões        │
└───────────────────┬─────────────────────────┘
                    │ Sequelize ORM
┌───────────────────▼─────────────────────────┐
│            BANCO DE DADOS                   │
│   MySQL (produção) / PostgreSQL (testes)    │
└─────────────────────────────────────────────┘
```

---

## Diagramas C4

A arquitetura está documentada em diagramas C4 separados por nível:

- [Nível 1 — Contexto](c4/contexto.md)
- [Nível 2 — Contêineres](c4/containers.md)
- [Nível 3 — Componentes](c4/componentes.md)

---

## Camadas do Sistema

### Frontend

O frontend adota uma **arquitetura híbrida**: a base da aplicação é renderizada no servidor via **EJS** (Embedded JavaScript Templates), enquanto o editor de conteúdo do módulo de revisão utiliza componentes **React** compilados e servidos como assets estáticos.

Essa integração React é **isolada na pasta `editor_markdown/`**, que possui seu próprio `package.json` com React e Vite. O processo de build (`npm run build:editor`) compila os componentes e deposita os arquivos otimizados em `public/`, onde o Express os serve normalmente. O `package.json` principal do projeto não contém React nem Vite — eles são dependências exclusivas do subprojeto `editor_markdown/`.

A estilização global é feita com **Bootstrap 5**, complementada por folhas CSS personalizadas. A comunicação assíncrona entre frontend e backend é feita via **Axios** (v1.10.0).

A renderização de conteúdo Markdown é feita com **marked** (v16.3.0), com suporte a equações matemáticas via extensão **marked-katex-extension** (v5.1.5). A geração de PDFs é feita no servidor via **Puppeteer** (v24.25.0), que controla uma instância headless do Chrome para renderizar e exportar páginas como PDF com fidelidade ao layout da aplicação.

### Backend

O backend é construído com **Node.js** (v22.5.0) e o framework web **Express.js** (v5.1.0). Ele é responsável por receber as requisições do usuário, processar a lógica de negócio e retornar as respostas.

O sistema adota o padrão arquitetural **MVC**, organizado em domínios:

```
IFVest/
├── .github/            # Configurações do GitHub (CI/CD workflows)
├── config/             # Configurações do banco de dados
├── domains/            # Módulos por domínio de negócio
│   ├── simulados/      # Sistema de simulados e questões
│   ├── revisao/        # Sistema de revisão de conteúdos
│   ├── flashcards/     # Módulo de flashcards com repetição espaçada
│   └── shared/         # Componentes compartilhados
├── editor_markdown/    # Editor Markdown em React + Vite (build isolado, próprio package.json)
├── logs/               # Logs de execução da aplicação
├── middleware/         # Middlewares customizados (autenticação, segurança, validação)
├── migrations/         # Migrações do banco de dados
├── models/             # Modelos Sequelize (entidades do banco)
├── modules/            # Módulos utilitários reutilizáveis
├── public/             # Assets estáticos (CSS, JS, imagens, output do build React)
├── routes/             # Rotas principais da aplicação
├── seeders/            # Dados iniciais para o banco
├── utils/              # Funções auxiliares gerais
├── validations/        # Schemas de validação Zod por entidade
├── views/              # Templates EJS
├── ecosystem.config.js # Configuração do PM2 (gerenciador de processos)
├── eslint.config.cjs   # Configuração do ESLint
└── index.js            # Ponto de entrada da aplicação
```

A segurança é gerenciada por middlewares dedicados:

- **Helmet** — define cabeçalhos HTTP de segurança
- **CORS** — controla o acesso cross-origin
- **Express-session** — gerencia sessões de usuário autenticado
- **Validação em duas camadas** — client-side via JavaScript (feedback visual imediato, bloqueio de caracteres inválidos) e server-side via middleware **Zod** (`validateRequest`), que intercepta requisições antes dos controllers e aplica schemas tipados por entidade (Autenticação, Questões, Simulados, Tópicos, Conteúdos)
- Prevenção de **SQL Injection** via expressão regular no middleware Zod, rejeitando termos reservados SQL em todos os campos de texto
- **Criptografia de senhas** com `bcrypt` e criptografia de URLs de recuperação

### Banco de Dados

O banco de dados principal é o **MySQL**, utilizado em desenvolvimento e produção. Em ambiente de testes, é utilizado o **PostgreSQL**. O acesso ao banco é feito exclusivamente através do **Sequelize** (v6.37.3), um ORM (Object-Relational Mapper) que abstrai as queries SQL e gerencia as migrações e seeders.

### Infraestrutura de Hospedagem

A plataforma está disponível publicamente em `ifvest.jcr.ifsp.edu.br`, hospedada em servidor externo provido pelo serviço [GoInfinite](https://goinfinite.net). O gerenciamento de processos em produção é feito via **PM2** (v6.0.5), configurado no arquivo `ecosystem.config.js`.

As principais entidades do sistema são:

**Cadastro e acesso**

| Tabela | Descrição |
|--------|-----------|
| `usuarios` | Dados de cadastro, autenticação e perfil do usuário |
| `sessions` | Sessões ativas, persistidas em banco pelo `connect-session-sequelize` |

**Organização de conteúdo**

| Tabela | Descrição |
|--------|-----------|
| `areas` | Disciplinas/áreas de conhecimento disponíveis na plataforma |
| `topicos` | Tópicos de estudo organizados por área |
| `assuntos` | Assuntos em estrutura hierárquica, com autorreferência que permite subassuntos |

**Banco de questões e simulados**

| Tabela | Descrição |
|--------|-----------|
| `questoes` | Questões cadastradas na plataforma (objetivas e dissertativas) |
| `opcoes` | Alternativas de resposta de cada questão objetiva, com indicação da correta |
| `questoes_topicos` | Associação entre questões e tópicos (relação N:N) |
| `simulados` | Simulados criados pelos professores |
| `perguntas_provas` | Associação entre questões e simulados (relação N:N) |
| `respostas` | Respostas submetidas pelos alunos em cada simulado |

**Materiais de revisão**

| Tabela | Descrição |
|--------|-----------|
| `conteudos` | Materiais de estudo em Markdown, com título, links externos e contador de leituras |
| `palavras_chave` | Palavras-chave utilizadas na busca de materiais |
| `tag_conteudo` | Associação entre materiais e palavras-chave (relação N:N) |

**Flashcards e gamificação**

| Tabela | Descrição |
|--------|-----------|
| `flashcards` | Cartões de estudo categorizados por área, tópico e nível de dificuldade |
| `dificuldades` | Níveis de dificuldade disponíveis para classificação |
| `flashcard_usuario` | Histórico de revisão por usuário (relação N:N); sustenta a lógica de repetição espaçada |
| `placar` | Pontuações registradas no módulo IFQuiz (acertos, total de questões, porcentagem e data) |

**Controle interno**

| Tabela | Descrição |
|--------|-----------|
| `SequelizeMeta` | Controle de migrações gerenciado pelo Sequelize |

---

## Tecnologias Utilizadas

### Backend
| Tecnologia | Versão | Função |
|------------|--------|--------|
| Node.js | 22.5.0 | Runtime JavaScript |
| Express.js | 5.1.0 | Framework web |
| Sequelize | 6.37.3 | ORM para banco de dados |
| EJS | 3.1.9 | Template engine (renderização server-side) |
| Express-session | 1.17.3 | Gerenciamento de sessões de usuário |
| connect-session-sequelize | 8.0.2 | Persistência de sessões no banco de dados |
| Helmet | 8.1.0 | Cabeçalhos HTTP de segurança |
| CORS | 2.8.5 | Cross-Origin Resource Sharing |
| express-rate-limit | 7.5.0 | Limitação de taxa de requisições |
| Zod | 3.25.64 | Validação de schemas server-side |
| body-parser | 2.2.0 | Interpretação do corpo das requisições |
| express-ejs-layouts | 2.5.1 | Layouts reutilizáveis nas views EJS |
| method-override | 3.0.0 | Suporte a PUT e DELETE a partir de formulários HTML |
| bcrypt | 5.1.1 | Criptografia de senhas |
| Multer | 1.4.5-lts.1 | Upload de arquivos (imagens de perfil, materiais) |
| Puppeteer | 24.25.0 | Geração de PDFs via Chrome headless (server-side) |
| dotenv | 16.4.5 | Carregamento de variáveis de ambiente |
| Nodemon | 3.0.1 | Auto-reload em desenvolvimento |
| PM2 | 6.0.5 | Gerenciador de processos em produção |

### Frontend
| Tecnologia | Versão | Função |
|------------|--------|--------|
| Bootstrap | 5.3.8 | Framework CSS responsivo |
| JavaScript | ES6+ | Lógica no cliente |
| CSS3 | — | Estilização personalizada |
| React + Vite | — | Editor Markdown interativo — isolados em `editor_markdown/` com build próprio; o output é servido como asset estático pelo Express |
| Axios | 1.10.0 | Requisições HTTP assíncronas no cliente |
| marked | 16.3.0 | Renderização de Markdown no servidor |
| marked-katex-extension | 5.1.5 | Suporte a equações matemáticas LaTeX no Markdown |
| markdown-it | 14.1.0 | Parser Markdown alternativo (uso interno) |

### Banco de Dados
| Tecnologia | Uso |
|------------|-----|
| MySQL | Desenvolvimento e produção |
| PostgreSQL | Ambiente de testes |
| MariaDB | Suporte adicional |

### Ferramentas de Desenvolvimento e Testes
| Tecnologia | Versão | Função |
|------------|--------|--------|
| Jest | 29.7.0 | Testes unitários |
| Cypress | 15.0.0 | Testes end-to-end |
| ESLint | 9.27.0 | Análise estática de código |
| sequelize-cli | 6.6.0 | Gerenciamento de migrações e seeders via CLI |
| supertest | 7.0.0 | Testes de integração de rotas HTTP |

---

## Interface de Programação (API)

A plataforma expõe rotas REST que retornam dados em JSON, utilizadas pelos componentes de interface — como o placar do IFQuiz e a consulta de áreas e tópicos. As demais rotas seguem o modelo tradicional de renderização no servidor.

A relação completa das rotas, com seus métodos, parâmetros e respostas, é mantida na **especificação da API** produzida pelos subprojetos responsáveis, em formato OpenAPI (Swagger). ⬜ *A referência será incluída aqui quando a especificação estiver publicada.*

O comportamento de cada módulo, do ponto de vista funcional, está descrito em [Descrição das Funcionalidades](funcionalidades.md).

## Integrações Externas

O sistema conta com uma integração externa em uso e outras em desenvolvimento ativo ou planejadas:

| Integração | Finalidade | Status |
|------------|------------|--------|
| [enem.dev](https://enem.dev) | Importação de questões do ENEM para o módulo IFQuiz | Em uso |
| API da FUVEST | Extração de questões da FUVEST para o banco de dados | Em desenvolvimento |
| API da UNICAMP | Extração de questões da UNICAMP para o banco de dados | Em desenvolvimento |
| API de outro vestibular | Extração de questões de vestibular adicional para o banco de dados | Em desenvolvimento |
| Firebase Authentication | Login social via conta Google | Planejado |
| Elastic Search | Busca avançada de materiais por palavra-chave | Planejado |
| Redis | Cache para otimização de consultas frequentes | Planejado |

!!! info "Subprojetos ativos"
    As integrações com as APIs da FUVEST, UNICAMP e demais vestibulares são subprojetos de extensão em andamento no IFSP Campus Jacareí. A documentação detalhada de cada subprojeto está disponível na seção [Subprojetos Ativos](subprojetos/index.md).

---

## Evolução da Stack

O sistema passou por uma migração significativa desde sua concepção:

| Versão | Stack | Origem | Período |
|--------|-------|--------|---------|
| v1 (original) | PHP + MariaDB + MVC nativo | TCCs de Fonseca e Sousa | 2021 |
| v2 (atual) | Node.js + Express + Sequelize + MySQL + EJS | TCC de Cristian Zago Da Silva | 2024 |
| v2.x (atual) | Integração híbrida de componentes React via Vite + Zod + Axios | Projeto de extensão | 2025–2026 |
| v3 (em desenvolvimento) | Reescrita do frontend em React, com redesign completo da interface | Projeto de extensão | 2026– |

A migração de PHP para Node.js foi realizada integralmente por Cristian Rodolfo Zago Da Silva como seu TCC (2024). A reconstrução manteve a arquitetura MVC e os conceitos de domínio da v1, modernizando a stack para o ecossistema JavaScript e unificando a linguagem entre frontend e backend. É essa versão que está em produção hoje e sobre a qual os subprojetos ativos de extensão operam.

A versão em produção adota uma **estratégia de integração híbrida incremental**: componentes React são compilados com Vite e injetados como assets estáticos nas páginas EJS existentes, permitindo modernizar partes críticas da interface — como o editor de materiais — sem substituir o backend ou reescrever o código legado.

!!! info "Reescrita do frontend em andamento"
    Desde 2026, um subprojeto de extensão conduz a **reescrita completa do frontend em React**, acompanhada de redesign de toda a interface. Diferente da integração híbrida descrita acima, trata-se da substituição das telas construídas em EJS.

    Enquanto essa entrega não é concluída, esta documentação descreve a plataforma em produção, e a documentação de usuário é produzida tendo a versão refatorada como referência. Ver [Planejamento da Documentação](planejamento.md) e [Subprojetos Ativos](subprojetos/index.md).
