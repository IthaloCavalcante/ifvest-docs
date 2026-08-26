# Descrição do Sistema

O **IFVest** é uma plataforma educacional gratuita desenvolvida no Instituto Federal de Educação, Ciência e Tecnologia de São Paulo (IFSP), Campus Jacareí, pelo curso de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS).

Seu objetivo é oferecer um ambiente digital interativo para auxiliar estudantes na preparação para o ENEM e vestibulares, além de fornecer ferramentas para que professores criem e apliquem simulados e atividades avaliativas.

---

## Contexto e Motivação

A plataforma tem origem em dois Trabalhos de Conclusão de Curso desenvolvidos em 2021 no IFSP Campus Jacareí: um focado na interface e experiência do usuário (Fonseca, 2021) e outro no back-end e banco de dados da plataforma de simulados (Sousa, 2021). Essa primeira versão foi construída em PHP com banco de dados MariaDB.

O projeto não teve continuidade documentada entre 2021 e 2023. Em 2024, Cristian Rodolfo Zago Da Silva resgatou e reconstruiu integralmente a plataforma como seu próprio TCC, migrando para uma stack moderna baseada em Node.js, Express.js, Sequelize e MySQL, com arquitetura MVC. Essa reconstrução é o sistema atual em produção. A partir daí, o projeto passou a crescer como iniciativa de extensão do IFSP Campus Jacareí, com múltiplos subprojetos ativos vinculados ao curso de ADS.

A principal motivação é a desigualdade no acesso à educação de qualidade. Grande parte das plataformas de estudo para vestibulares são pagas ou impõem limitações aos usuários gratuitos. O IFVest se propõe a ser uma alternativa completamente gratuita, acessível a estudantes de baixa renda que desejam se preparar para os principais exames do país por conta própria.

---

## Público-alvo

A plataforma atende dois perfis principais de usuários:

**Estudantes (Alunos)**
Estudantes do ensino médio ou cursinho que desejam se preparar para o ENEM e vestibulares como FUVEST, UNICAMP e UNESP. A plataforma oferece a eles um ambiente de estudos gratuito, com simulados personalizados, revisão de conteúdos e acompanhamento de desempenho.

**Educadores (Professores)**
Professores que desejam utilizar a plataforma como ferramenta de apoio ao ensino. Podem criar e organizar questões por área e tópico, montar simulados personalizados para seus alunos e gerar provas em formato PDF para aplicação presencial.

Existe também o perfil de **Administrador**, responsável por moderar o conteúdo da plataforma — autorizar questões enviadas por professores e gerenciar usuários.

---

## Funcionalidades

### Para Estudantes

- Realização de simulados personalizados com filtro por disciplina e tópico
- Simulado no **modo desafio**: com cronômetro baseado no número de questões e tela de desempenho ao final (acertos, erros, tempo médio por questão)
- Revisão de materiais educacionais organizados por área e tópico, com busca por título de assunto e por palavra-chave, sistema de paginação e hierarquia de conteúdos em estrutura de árvore
- Histórico de simulados realizados e acompanhamento de desempenho
- Download de simulados e gabaritos em formato PDF
- **IFQuiz** — módulo de gamificação com questões do ENEM: seleção de disciplina e quantidade de questões, feedback imediato por resposta (acerto/erro com indicação da alternativa correta), cálculo de pontuação e placar de líderes com ranking comparativo entre usuários
- **Flashcards com repetição espaçada** — revisão de conteúdos por cartões baseada em *active recall*: filtro por área, tópico e nível de dificuldade, agrupamento automático por tempo de última revisão (≤3 dias, 7 dias, 15 dias e 15+ dias), exibição de até 10 cartões aleatórios por sessão com animação de rotação para revelação da resposta

### Para Professores

- Criação de questões com editor de texto rico e editor de equações matemáticas (LaTeX)
- Classificação de questões por disciplina, tópico e subtópico
- Criação de simulados personalizados com associação de questões
- Edição e exclusão de questões e simulados
- Geração de provas em formato PDF para aplicação presencial
- Criação, edição e exclusão de flashcards categorizados por área, tópico e nível de dificuldade, com reflexo imediato para todos os alunos da plataforma

### Para Administradores

- Autorização de questões enviadas por professores
- Promoção de usuários ao perfil de professor
- Gerenciamento de notícias na página inicial
- Leitura de feedbacks enviados pelos usuários

### Funcionalidades Técnicas

- Autenticação com sistema de sessões
- Confirmação de cadastro por e-mail
- Recuperação de senha por e-mail
- Criptografia de senhas e dados sensíveis
- Proteção contra SQL Injection e XSS
- Interface responsiva adaptável a diferentes dispositivos

---

## Restrições do Sistema

- O acesso a todos os módulos da plataforma (Simulados, Revisão, IFQuiz, Flashcards) requer autenticação prévia com conta cadastrada
- A criação, edição e exclusão de questões, simulados, materiais de revisão e flashcards é restrita aos perfis Professor e Administrador
- A autorização de questões submetidas por professores é exclusiva do perfil Administrador
- A plataforma depende de conexão ativa com a internet, tanto para o acesso dos usuários quanto para o carregamento de questões do ENEM pelo módulo IFQuiz (via API externa [enem.dev](https://enem.dev))
- O sistema não oferece modo offline

---

## Histórico do Projeto

| Período | Marco |
|---------|-------|
| 2021 | TCC de Fonseca (interface/frontend) e TCC de Sousa (back-end e banco de dados) — v1 em PHP + MariaDB |
| 2021–2023 | Período sem documentação disponível. O projeto não teve continuidade registrada após os TCCs de 2021. |
| 2024 | TCC de Cristian Rodolfo Zago Da Silva — resgate e reconstrução completa da plataforma em Node.js + Express + MySQL (v2, versão atual em produção) |
| 2024 | Relatório de extensão de Rafaela dos Santos Machado — testes de acessibilidade, usabilidade e performance |
| 2025 | Relatório de extensão de Ruan Patrick Santos Araujo — editor Markdown com integração React/Vite |
| 2025 | Relatório de extensão de Nicolas Felipe Pinheiro Soares — módulo IFQuiz (gamificação com questões do ENEM) |
| 2025 | Relatório de extensão de André Vinícius Neves da Silva — módulo de Flashcards com repetição espaçada |
| 2025–2026 | Projeto de extensão ativo: múltiplos subprojetos em desenvolvimento simultâneo |

---

## Acesso à Plataforma

A plataforma está disponível publicamente em:

**[https://ifvest.jcr.ifsp.edu.br/home](https://ifvest.jcr.ifsp.edu.br/home)**

!!! warning "Ambiente em desenvolvimento"
    A plataforma está em desenvolvimento ativo. Funcionalidades podem mudar entre versões.
