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
Estudantes do ensino médio ou cursinho que desejam se preparar para o ENEM e vestibulares como FUVEST, UNICAMP e UNESP. A plataforma oferece a eles um ambiente de estudos gratuito, com simulados, revisão de conteúdos, flashcards e quizzes gamificados.

**Educadores (Professores)**
Professores que desejam utilizar a plataforma como ferramenta de apoio ao ensino. Podem criar e organizar questões por área e tópico, montar simulados personalizados para seus alunos e gerar provas em formato PDF para aplicação presencial.

!!! warning "Perfil de Administrador — previsto, não implementado"
    A plataforma prevê um terceiro perfil, o de **Administrador**, destinado à moderação de conteúdo e à gestão de usuários. O valor correspondente existe na estrutura do banco de dados, mas **não há implementação associada a ele**: o cadastro oferece apenas os perfis de estudante e professor, e nenhuma tela ou função exclusiva de administrador existe na versão atual.

    Esse perfil está sendo definido pelo subprojeto de refatoração do frontend, que prevê a transferência de parte das atribuições hoje exercidas pelo professor. Ver [Subprojetos Ativos](subprojetos/index.md).

---

## Funcionalidades

### Para Estudantes

- Realização de simulados montados pelos professores, com relatório de desempenho ao final (acertos, erros e percentual) e consulta ao gabarito
- Revisão de materiais educacionais organizados por área e tópico, com busca por título de assunto e por palavra-chave, sistema de paginação e hierarquia de conteúdos em estrutura de árvore
- **IFQuiz** — módulo de gamificação com questões do ENEM: seleção de disciplina e quantidade de questões, feedback imediato por resposta (acerto/erro com indicação da alternativa correta), cálculo de pontuação e placar de líderes com ranking comparativo entre usuários
- **Flashcards com repetição espaçada** — revisão de conteúdos por cartões baseada em *active recall*: filtro por área, tópico e nível de dificuldade, agrupamento automático por tempo desde a última revisão (1, 3, 7, 15 e mais de 15 dias), exibição de até 10 cartões aleatórios por sessão com animação de rotação para revelação da resposta

### Para Professores

- Criação de questões com editor de texto rico e editor de equações matemáticas (LaTeX)
- Classificação de questões por disciplina, tópico e subtópico
- Criação de simulados personalizados com associação de questões
- Edição e exclusão de questões e simulados
- Geração de provas em formato PDF para aplicação presencial
- Criação, edição e exclusão de flashcards categorizados por área, tópico e nível de dificuldade, com reflexo imediato para todos os alunos da plataforma

### Funcionalidades Técnicas

- Autenticação com sistema de sessões, com limite de tentativas de login por origem
- Armazenamento de senhas com hash criptográfico
- Validação de dados de entrada em todas as requisições
- Cabeçalhos de segurança e política de origem cruzada
- Interface responsiva adaptável a diferentes dispositivos

!!! note "Funcionalidades previstas, ainda não implementadas"
    A confirmação de cadastro e a recuperação de senha por e-mail constam do projeto da plataforma, mas **não existem na versão atual** — não há envio de e-mail implementado. A recuperação de senha em três etapas está prevista no redesign do frontend, e é documentada como tal no [Guia de Acesso e Conta](guias/conta/acesso.md#tarefa-3-recuperar-sua-senha).

---

## Restrições do Sistema

- O acesso a todos os módulos da plataforma (Simulados, Revisão, IFQuiz, Flashcards) requer autenticação prévia com conta cadastrada
- A criação, edição e exclusão de questões, simulados, materiais de revisão e flashcards é restrita ao perfil Professor
- A criação de simulados é exclusiva do perfil Professor; o estudante realiza os simulados disponibilizados, mas não os cria
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
