# Requisitos Funcionais (RF)

Esta página descreve as funcionalidades do sistema IFVest, categorizadas por perfil de usuário e por módulos em desenvolvimento nos subprojetos ativos.

---

## 1. Perfil: Estudante

O estudante é o principal usuário da plataforma, focado no consumo de conteúdo e na prática de exercícios.

| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| **RF01** | **Autenticação Segura** | O sistema deve permitir o cadastro e login utilizando e-mail institucional ou conta Google (via Firebase). |
| **RF02** | **Recuperação de Senha** | O sistema deve oferecer um fluxo de recuperação de senha em três etapas: inserção de e-mail, validação de código e definição de nova senha. |
| **RF03** | **Gestão de Perfil** | O estudante deve poder alterar sua foto de perfil, atualizar informações cadastrais e solicitar a exclusão de sua conta (em conformidade com a LGPD). |
| **RF04** | **Revisão de Conteúdo** | O estudante deve acessar materiais de estudo divididos por áreas (Matemática, Humanas, Naturais, Linguagens e Informática). |
| **RF05** | **Consumo de Materiais** | O sistema deve exibir videoaulas, textos teóricos em Markdown e exercícios de fixação específicos para cada assunto. |
| **RF06** | **Prática com IFQuiz** | O estudante deve poder realizar quizzes com filtros por disciplina, assunto e tags específicas, visualizando seu placar e desempenho. |
| **RF07** | **Uso de Flashcards** | O estudante deve poder criar seus próprios flashcards ou utilizar baralhos institucionais criados por professores. |
| **RF08** | **Submissão de Redação** | O estudante deve poder realizar o upload de redações (manuscritas ou digitadas) para correção automatizada ou por professores. |

---

## 2. Perfil: Professor / Administrador

O professor atua como curador de conteúdo e gestor da plataforma.

| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| **RF09** | **Criação de Conteúdo** | O professor deve poder criar materiais de revisão utilizando um editor Markdown com preview em tempo real. |
| **RF10** | **Gestão de Exercícios** | O sistema deve permitir que o professor crie questões manualmente ou as importe de um banco de questões pré-existente (via API ENEM/FUVEST). |
| **RF11** | **Curadoria de Flashcards** | O professor deve poder criar e disponibilizar baralhos de flashcards oficiais para as turmas. |
| **RF12** | **Correção de Redações** | O professor/corretor deve poder visualizar as redações submetidas e aplicar critérios de correção manuais, complementando a IA. |

---

## 3. Módulos de Inteligência e Integração

Funcionalidades transversais suportadas por APIs e modelos de IA.

| ID | Requisito | Descrição |
| :--- | :--- | :--- |
| **RF13** | **Correção via OCR/IA** | O sistema deve ser capaz de realizar o reconhecimento de caracteres (OCR) em redações manuscritas e sugerir correções baseadas em redes neurais. |
| **RF14** | **Recomendação de Estudo** | O sistema deve sugerir materiais e exercícios baseados no histórico de desempenho e erros do estudante. |
| **RF15** | **Integração de Questões** | O sistema deve consumir APIs externas para manter o banco de questões atualizado com os últimos exames do ENEM e FUVEST. |

---

## Notas sobre a Implementação
Os requisitos RF01, RF02 e RF03 estão sendo reestruturados no subprojeto de **Adequação à LGPD**. Os requisitos RF04 e RF05 estão em fase de migração para **React**. Os requisitos RF13 e RF14 representam a fronteira de inovação do eixo de **IA e Recomendação**.
