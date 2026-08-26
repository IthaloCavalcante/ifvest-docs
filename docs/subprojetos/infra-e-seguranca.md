# Eixo 4: Infraestrutura, APIs e Segurança

Este eixo garante a robustez, a segurança e a conformidade legal da infraestrutura da plataforma IFVest. Os projetos visam desenvolver APIs para integração com serviços externos, aprimorar a gestão de dados e assegurar a proteção das informações dos usuários.

## Projetos Principais

### Adequação do Cadastro da IFVest à LGPD

*   **Líder:** Wilker
*   **Objetivo:** Garantir a conformidade do sistema de cadastro do IFVest com a Lei Geral de Proteção de Dados (LGPD), Lei n.º 13.709/2018.
*   **Tecnologias Envolvidas:** Firebase (Firebase Authentication, Cloud Firestore, Cloud Storage).
*   **Destaques:**
    *   Reestruturação técnica do banco de dados do cadastro com Firebase, utilizando Firebase Authentication para autenticação segura com hash de senhas via bcrypt.
    *   Configuração do Cloud Firestore com Security Rules para isolamento de dados por usuário.
    *   Configuração do Cloud Storage para armazenamento seguro de fotos de perfil.
    *   Formalização das bases legais para cada dado coletado, conforme exigido pelo art. 7.º da LGPD.
    *   Adoção de uma arquitetura integralmente aderente aos princípios de Segurança, Necessidade e Finalidade da LGPD.

### Criação de Tags para Integração com API do ENEM e Estruturação do Banco de Dados das Questões

*   **Líderes:** Vitor e Helena
*   **Objetivo:** Desenvolver uma API para extração de questões da FUVEST e ENEM, e estruturar o banco de dados para suportar a categorização e integração eficiente de questões.
*   **Destaques:**
    *   Criação de um sistema de tags robusto para classificar questões por disciplina, tópico e subtópico.
    *   Estudo e integração com APIs externas (como `enem.dev`) para importação automatizada de questões.
    *   Modelagem de dados para um banco de questões escalável e de fácil manutenção.
    *   Apoio à criação de simulados personalizados e materiais de revisão.

### Reestruturação da Plataforma/BD com Python

*   **Líder:** Jorge
*   **Objetivo:** Migrar e otimizar partes da infraestrutura e do banco de dados da plataforma para Python, visando melhor desempenho, manutenibilidade e escalabilidade.
*   **Tecnologias Envolvidas:** Python, ferramentas de gerenciamento de projetos (Trello).
*   **Destaques:**
    *   Reescrita de componentes do backend e do banco de dados em Python.
    *   Organização das tarefas de desenvolvimento e migração utilizando ferramentas de gerenciamento de projetos como Trello.
    *   Busca por melhorias na performance e na arquitetura geral do sistema.
