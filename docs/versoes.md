# Registro de Versões

Este documento registra o histórico de evolução da plataforma IFVest, organizado por marcos de desenvolvimento. Cada versão corresponde a uma entrega relevante: nova funcionalidade, reestruturação técnica ou mudança significativa no banco de dados.

As datas de cada versão são inferidas a partir das migrations do banco de dados, dos TCCs e dos relatórios de extensão disponíveis.

---

## v1.0 — Plataforma PHP/MariaDB (2021)

**Período:** 2021  
**Responsáveis:** Rafael Rodrigues de Sousa (backend), Fonseca (frontend)  
**Tipo:** TCC

Primeira versão da plataforma IFVest, desenvolvida como trabalho de conclusão de curso. Implementada com PHP no backend e MariaDB como banco de dados relacional.

**Funcionalidades entregues:**

- Autenticação de usuários (cadastro e login)
- Banco de questões de vestibular
- Módulo inicial de simulados

**Observação:** O projeto ficou inativo entre 2021 e 2023, sem manutenção ou desenvolvimento ativo.

---

## v2.0 — Reescrita em Node.js (2023–2024)

**Período:** 2023 (banco de dados) — 2024 (sistema completo)  
**Responsável:** Cristian Rodolfo Zago Da Silva  
**Tipo:** TCC + Iniciação Científica (PIBIFSP 2024)

Reescrita completa da plataforma, abandonando PHP/MariaDB em favor de uma stack moderna. A nova arquitetura adota o padrão MVC e a separação por domínios.

**Stack adotada:**

- Node.js + Express
- MySQL (Sequelize ORM)
- EJS (template engine)
- Bootstrap 5

**Funcionalidades entregues:**

- Autenticação com bcrypt e sessões
- Perfis de usuário: Aluno e Professor
- Módulo de simulados completo (criação, edição, realização, gabarito)
- Criação e gerenciamento de questões objetivas e dissertativas
- Geração de PDF de simulados

**Migrations iniciais do banco de dados:**

| Data | Tabela criada |
|---|---|
| 2023-03-19 | `Usuario` |
| 2024-03-19 | `Area`, `Topico` |
| 2024-03-20 | `Questao`, `Simulado`, `Opcao`, `Resposta`, `PerguntasProvas` |
| 2024-04-17 | `QuestaoTopico` (relação N:M entre questões e tópicos) |

---

## v2.1 — Editor Markdown e Módulo de Revisão de Conteúdo (2024–2025)

**Período:** 2024–2025  
**Responsáveis:** Ruan Patrick Santos Araujo (editor); João Pedro Veríssimo (módulo de revisão e arquitetura de domínios)  
**Tipo:** Extensão + Estágio

Introdução do módulo de revisão de conteúdo para professores criarem e alunos consumirem materiais de estudo em Markdown. Neste período também foi proposta e implementada a separação da aplicação em domínios isolados (`domains/`), que estrutura o projeto até hoje.

**Funcionalidades entregues:**

- Editor Markdown com preview em tempo real (React + Vite, isolado em `editor_markdown/`)
- Suporte a notação matemática LaTeX via KaTeX
- Módulo de revisão: criação, edição e exclusão de materiais por professores
- Navegação hierárquica por assuntos (árvore de categorias)
- Busca de conteúdo por área, tópico e assunto
- Upload de arquivos para materiais
- Contador de leituras por conteúdo

**Migrations:**

| Data | Tabela criada |
|---|---|
| 2025-02-02 | `Assunto` (com suporte a hierarquia via `id_assunto_ascendente`) |
| 2025-03-26 | `Session` (persistência de sessões no banco) |
| 2025-05-19 | `PalavraChave`, `Conteudo`, `TagConteudo` |

---

## v2.2 — Módulo de Flashcards (2025)

**Período:** 2025  
**Responsável:** André Vinícius Neves da Silva  
**Tipo:** Extensão

Implementação do módulo de flashcards com lógica de repetição espaçada integrada à plataforma.

**Funcionalidades entregues:**

- CRUD de flashcards para professores (criar, editar, excluir)
- Interface de estudo para alunos com filtros por Área, Tópico e Dificuldade
- Exibição de até 10 cartões aleatórios por sessão
- Animação de virada de cartão para revelação da resposta
- Repetição espaçada baseada no campo `visto_por_ultimo` com intervalos de 1, 3, 7, 15 e mais de 15 dias
- Navegação por grupos de flashcards
- Três níveis de dificuldade: Fácil, Médio, Difícil

**Migrations:**

| Data | Tabela criada |
|---|---|
| 2025-01-01 | `Dificuldade` |
| 2025-01-01 | `Flashcard` |
| 2025-09-18 | `FlashcardUsuario` (rastreamento de revisões por usuário) |

---

## v2.3 — IFQuiz e Verificação de Similaridade (2025)

**Período:** 2025  
**Responsáveis:** Nicolas Felipe Pinheiro Soares (IFQuiz); Guilherme Souza (verificação de similaridade por IA)  
**Tipo:** Extensão

Adição do módulo de gamificação IFQuiz e da funcionalidade de curadoria semiautomática de questões com IA.

**Funcionalidades entregues — IFQuiz:**

- Quizzes de múltipla escolha com questões do ENEM via API `enem.dev`
- Seleção de matéria e quantidade de questões
- Feedback imediato por questão (correto/incorreto)
- Tela de resultados com acertos e percentual de eficiência
- Ranking dos 5 melhores jogadores (placar público)
- Registro de pontuação para usuários logados e visitantes

**Funcionalidades entregues — Similaridade:**

- Verificação de duplicidade de questões via API Gemini (Google)
- Exibição de trechos similares encontrados no banco
- Disponível exclusivamente para professores

**Migrations:**

| Data | Alteração |
|---|---|
| 2025-10-28 | Campo `descricao` do `Simulado` alterado de `STRING` para `TEXT` |
| 2025-11-15 | Tabela `Placar` criada |
| 2025-12-06 | Adição de `id_placar` (PK) à tabela `Placar` |
| 2025-12-06 | Renomeação da tabela de placar para nome definitivo |

---

## v2.4 — LGPD e Adequação Legal (2025–2026)

**Período:** 2025–2026  
**Responsável:** Kendy de Oliveira Outi  
**Tipo:** Extensão

Análise de conformidade com a Lei Geral de Proteção de Dados (LGPD) e implementação das soluções documentais e de interface exigidas.

**Funcionalidades entregues:**

- Mapeamento dos dados pessoais coletados pela plataforma
- Texto da Política de Privacidade elaborado com embasamento jurídico
- Página de Política de Privacidade integrada à plataforma em `/shared/politica_de_privacidade`
- Propostas de canais de atendimento ao titular de dados

---

## Em desenvolvimento

Os itens abaixo estão em desenvolvimento ativo e não possuem data de entrega definida:

| Funcionalidade | Equipe |
|---|---|
| Migração do frontend para React | Isabella e Maria Luiza |
| Correção automatizada de redações via IA | Arthur, Douglas e Guilherme |
| Integração com API do ENEM e FUVEST | Vitor, Helena e Thales |
| Sistema de recomendação personalizado | João Pedro |
| Testes automatizados (unitários, funcionais e de mutação) | Vinicius Akio, Caio e Jorge |
| Melhorias de acessibilidade (WCAG) | Rafaela |
| Pipeline CI/CD | Jorge |
