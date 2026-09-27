# Modelo de Dados

Esta página apresenta a estrutura do banco de dados do IFVest: as tabelas, suas colunas e os relacionamentos entre elas.

!!! info "Gerado a partir do código em produção"
    Os diagramas abaixo foram gerados **diretamente dos modelos do backend**, e não desenhados à mão. Isso garante que correspondem exatamente ao esquema em uso: **22 tabelas, 22 chaves primárias e 27 chaves estrangeiras** — os mesmos números registrados pela equipe ao verificar o banco de produção.

    Para regenerá-los após alterações nos modelos, ver [Como atualizar esta página](#como-atualizar-esta-pagina).

---

## Visão geral dos relacionamentos

O diagrama abaixo mostra apenas as tabelas e como se relacionam, sem as colunas. A tabela `feature_flags` não aparece por não ter relacionamento com as demais.

```mermaid
erDiagram
    multiple_choice_questions ||--o{ alternatives : ""
    users ||--o{ essay_annotations : ""
    essays ||--o{ essay_annotations : ""
    proposals ||--o{ essays : ""
    users ||--o{ essays : ""
    users ||--o{ fixed_mocktests : ""
    users ||--o{ gradings : ""
    essays ||--o{ gradings : ""
    users ||--o{ items : ""
    users ||--o{ proposals : ""
    quiz_history ||--o{ question_history : ""
    users ||--o{ question_history : ""
    multiple_choice_questions ||--o{ question_history : ""
    topics ||--o{ question_topics : ""
    multiple_choice_questions ||--o{ question_topics : ""
    fixed_mocktests ||--o{ questions_mocktests : ""
    multiple_choice_questions ||--o{ questions_mocktests : ""
    users ||--o{ quiz_history : ""
    disciplines ||--o{ subjects : ""
    proposals ||--o{ support_texts : ""
    subjects ||--o{ topics : ""
    items ||--o{ transactions : ""
    users ||--o{ transactions : ""
    fixed_mocktests ||--o{ user_mocktests : ""
    users ||--o{ user_mocktests : ""
    permissions ||--o{ user_permissions : ""
    users ||--o{ user_permissions : ""
```

**Como ler o diagrama:** cada linha liga duas tabelas por uma chave estrangeira. O lado com duas barras (`||`) é a tabela referenciada; o lado com o círculo e o pé de galinha (`o{`) é a que guarda a referência — e que pode ter vários registros ligados a um mesmo registro do outro lado.

---

## Tabelas por domínio

Nas colunas, **PK** indica chave primária e **FK** indica chave estrangeira. Tabelas que aparecem em mais de um domínio estão repetidas para mostrar a ligação entre eles.

### Usuários e permissões

```mermaid
erDiagram
    permissions {
        int permission_id PK
        varchar name
        varchar description
    }
    user_permissions {
        int user_id PK, FK
        int permission_id PK, FK
    }
    users {
        int user_id PK
        varchar email
        bytea profile_picture
        int points
        int login_streak
        int total_corrects
        int total_answered
        bool correct_daily
        bool answered_daily
        date last_daily_date
        varchar nickname
        varchar avatar
        timestamp created_at
        timestamp updated_at
    }
    permissions ||--o{ user_permissions : ""
    users ||--o{ user_permissions : ""
```

### Taxonomia

```mermaid
erDiagram
    disciplines {
        int discipline_id PK
        varchar name
        varchar description
        timestamp created_at
        timestamp updated_at
    }
    subjects {
        int subject_id PK
        varchar name
        varchar description
        int discipline_id FK
        timestamp created_at
        timestamp updated_at
    }
    topics {
        int topic_id PK
        varchar name
        varchar description
        int subject_id FK
        timestamp created_at
        timestamp updated_at
    }
    disciplines ||--o{ subjects : ""
    subjects ||--o{ topics : ""
```

### Banco de questões

```mermaid
erDiagram
    alternatives {
        int alternative_id PK
        int question_id FK
        varchar alternative_letter
        text alternative_text
        varchar image_url
        bool is_correct
        timestamp created_at
        timestamp updated_at
    }
    multiple_choice_questions {
        int question_id PK
        varchar title
        text supplementary_text
        text question_text
        int year
        varchar exam_board
        int number
        varchar type_or_color
        int difficulty
        timestamp created_at
        timestamp updated_at
    }
    question_topics {
        int topic_id PK, FK
        int question_id PK, FK
    }
    topics {
        int topic_id PK
        varchar name
        varchar description
        int subject_id FK
        timestamp created_at
        timestamp updated_at
    }
    multiple_choice_questions ||--o{ alternatives : ""
    topics ||--o{ question_topics : ""
    multiple_choice_questions ||--o{ question_topics : ""
```

### Simulados

```mermaid
erDiagram
    fixed_mocktests {
        int fixed_mocktest_id PK
        varchar title
        varchar question_type
        int creator_id FK
        timestamp created_at
        timestamp updated_at
    }
    multiple_choice_questions {
        int question_id PK
        varchar title
        text supplementary_text
        text question_text
        int year
        varchar exam_board
        int number
        varchar type_or_color
        int difficulty
        timestamp created_at
        timestamp updated_at
    }
    questions_mocktests {
        int fixed_mocktest_id PK, FK
        int question_id PK, FK
    }
    user_mocktests {
        int user_mocktest_id PK
        int user_id FK
        int fixed_mocktest_id FK
        int total_questions
        int correct_answers
        int answered_questions
        int score
        timestamp started_at
        timestamp completed_at
        timestamp created_at
        timestamp updated_at
    }
    users {
        int user_id PK
        varchar email
        bytea profile_picture
        int points
        int login_streak
        int total_corrects
        int total_answered
        bool correct_daily
        bool answered_daily
        date last_daily_date
        varchar nickname
        varchar avatar
        timestamp created_at
        timestamp updated_at
    }
    users ||--o{ fixed_mocktests : ""
    fixed_mocktests ||--o{ questions_mocktests : ""
    multiple_choice_questions ||--o{ questions_mocktests : ""
    fixed_mocktests ||--o{ user_mocktests : ""
    users ||--o{ user_mocktests : ""
```

### Quiz e gamificação

```mermaid
erDiagram
    items {
        int item_id PK
        varchar name
        text description
        int price
        int created_by_user_id FK
        timestamp created_at
    }
    multiple_choice_questions {
        int question_id PK
        varchar title
        text supplementary_text
        text question_text
        int year
        varchar exam_board
        int number
        varchar type_or_color
        int difficulty
        timestamp created_at
        timestamp updated_at
    }
    question_history {
        int question_history_id PK
        int question_id FK
        int user_id FK
        int quiz_id FK
        varchar chosen_alternative
        bool is_correct
        timestamp answered_at
    }
    quiz_history {
        int quiz_id PK
        int user_id FK
        varchar name
        varchar subject
        varchar topic
        varchar difficulty
        int total_questions
        int correct_answers
        int quiz_score
        int attempts
        timestamp started_at
        timestamp completed_at
    }
    transactions {
        int transaction_id PK
        int user_id FK
        int item_id FK
        int amount
        timestamp created_at
    }
    users {
        int user_id PK
        varchar email
        bytea profile_picture
        int points
        int login_streak
        int total_corrects
        int total_answered
        bool correct_daily
        bool answered_daily
        date last_daily_date
        varchar nickname
        varchar avatar
        timestamp created_at
        timestamp updated_at
    }
    users ||--o{ items : ""
    quiz_history ||--o{ question_history : ""
    users ||--o{ question_history : ""
    multiple_choice_questions ||--o{ question_history : ""
    users ||--o{ quiz_history : ""
    items ||--o{ transactions : ""
    users ||--o{ transactions : ""
```

### Redação

```mermaid
erDiagram
    essay_annotations {
        int annotation_id PK
        int essay_id FK
        int evaluator_id FK
        int start_offset
        int end_offset
        varchar competency
        text comment
        timestamp created_at
    }
    essays {
        int essay_id PK
        int user_id FK
        int proposal_id FK
        text submitted_text
        varchar status
        timestamp submitted_at
    }
    gradings {
        int grading_id PK
        int essay_id FK
        int evaluator_id FK
        int c1_score
        int c2_score
        int c3_score
        int c4_score
        int c5_score
        text feedback
        date grading_date
        timestamp created_at
    }
    proposals {
        int proposal_id PK
        int user_id FK
        varchar title
        text description
        varchar tags
        timestamp created_at
    }
    support_texts {
        int support_text_id PK
        int proposal_id FK
        varchar type
        varchar title
        text content
        bytea image_data
        varchar image_url
        varchar source
        timestamp created_at
    }
    users {
        int user_id PK
        varchar email
        bytea profile_picture
        int points
        int login_streak
        int total_corrects
        int total_answered
        bool correct_daily
        bool answered_daily
        date last_daily_date
        varchar nickname
        varchar avatar
        timestamp created_at
        timestamp updated_at
    }
    users ||--o{ essay_annotations : ""
    essays ||--o{ essay_annotations : ""
    proposals ||--o{ essays : ""
    users ||--o{ essays : ""
    users ||--o{ gradings : ""
    essays ||--o{ gradings : ""
    users ||--o{ proposals : ""
    proposals ||--o{ support_texts : ""
```

### Plataforma

```mermaid
erDiagram
    feature_flags {
        varchar flag_key PK
        bool enabled
        text description
        timestamp created_at
        timestamp updated_at
    }
```


---

## Pontos de atenção do modelo

**Taxonomia e questões.** As questões se vinculam **apenas a tópicos**, por meio da tabela associativa `question_topics`, que permite a uma mesma questão pertencer a vários tópicos. Disciplina e assunto não são gravados na questão: são obtidos percorrendo a árvore `topics → subjects → disciplines`.

**Imagens gravadas no banco.** As colunas `profile_picture`, em `users`, e `image_data`, em `support_texts` — os textos de apoio das propostas de redação —, guardam **o próprio arquivo** em formato binário (`bytea`). Já as imagens das questões ficam em disco, fora do banco. Ver [Arquitetura — Armazenamento de arquivos](arquitetura.md#armazenamento-de-arquivos).

**Dados de gamificação no usuário.** Pontuação, ofensiva diária e totais de acertos ficam como colunas da própria tabela `users`, e não em uma tabela separada.

---

## Como atualizar esta página

Os diagramas são gerados a partir dos metadados do SQLAlchemy. Após qualquer alteração nos modelos — que sempre é acompanhada de uma migration do Alembic —, eles devem ser regenerados para que esta página continue correspondendo ao banco.

⬜ *Pendente: disponibilizar o script de geração no repositório, para que a atualização possa ser feita por qualquer pessoa da equipe.*

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Tabelas, colunas, chaves e relacionamentos | Metadados dos modelos SQLAlchemy do `ifvest-monorepo` (`ifvest-backend/src/models/`) | set/2026 |
| Contagem de tabelas e chaves em produção | Documentação de implantação do repositório (`deploy/README.md`) | set/2026 |
