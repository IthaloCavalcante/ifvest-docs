# Descrição das Funcionalidades

Esta página descreve o que cada funcionalidade do IFVest faz, organizada por módulo. As informações são baseadas no código-fonte da plataforma e nos relatórios das equipes de desenvolvimento.

---

## 1. Autenticação e Acesso

### Cadastro

Acessível em `/cadastro`. Permite que novos usuários criem uma conta na plataforma.

**Campos obrigatórios:**

- **Nome completo** — texto, mínimo 2 caracteres
- **Nome de usuário** — entre 3 e 30 caracteres, aceita letras, números, `_`, `.` e `-`
- **E-mail** — deve ser um endereço de e-mail válido
- **Senha** — mínimo 8 caracteres, obrigatoriamente contendo letras e números
- **Perfil** — seleção entre `USUARIO` (aluno) e `PROFESSOR`

Todos os campos são validados pelo servidor com Zod antes do registro. O nome de usuário deve ser único no sistema. A senha é armazenada com hash bcrypt.

Após o cadastro bem-sucedido, o usuário é redirecionado para a tela de login.

---

### Login

Acessível em `/login`. Autentica o usuário com nome de usuário e senha.

O sistema compara a senha fornecida com o hash armazenado via bcrypt. Em caso de sucesso, uma sessão é criada e o usuário é redirecionado para a página inicial logada (`/usuario/inicioLogado`). Em caso de erro, uma mensagem é exibida na mesma página.

**Proteção contra força bruta:** o endpoint de login possui um limitador de requisições — máximo de 5 tentativas por IP a cada 15 minutos. Ao exceder o limite, o usuário recebe uma mensagem de bloqueio temporário.

---

### Logoff

Disponível para usuários autenticados. Ao acionar o logoff, o sistema destrói a sessão no servidor, remove o registro da sessão no banco de dados e limpa o cookie de sessão no navegador. O usuário é redirecionado para `/login`.

---

### Perfil de Usuário

Acessível em `/usuario/perfil`. Permite ao usuário autenticado visualizar e editar suas informações.

**Campos editáveis:** nome, nome de usuário, e-mail, foto de perfil (upload de imagem), e troca de senha (campo senha atual + campo nova senha).

Usuários também podem solicitar a exclusão de sua conta. A exclusão remove o registro do usuário e, em cascata, seus dados associados (questões, respostas).

---

## 2. Módulo de Simulados

Acessível em `/simulados`. Funcionalidade central da plataforma, com experiências distintas para professores e alunos.

### Para o Professor

#### Criar Simulado

Rota: `GET /simulados/criar-simulado` (formulário) + `POST /simulados/criar-simulado` (envio).

O professor define título, descrição e tipo do simulado:

- **OBJETIVO** — questões de múltipla escolha (A–E)
- **DISSERTATIVO** — questões abertas
- **ALEATORIO** — mistura de ambos os tipos

Em seguida, seleciona as questões a vincular ao simulado. É necessário selecionar ao menos uma questão.

#### Gerenciar Simulados

- **Meus simulados** (`/simulados/meus-simulados`) — lista os simulados criados pelo professor, com opções de editar, excluir e gerenciar questões.
- **Editar simulado** (`/simulados/:id/editar`) — altera título, descrição e tipo.
- **Adicionar questões** (`/simulados/:simuladoId/adicionar-questoes`) — vincula novas questões ao simulado existente.
- **Remover questões** (`/simulados/:simuladoId/remover-questoes`) — desvincula questões do simulado.

#### Imprimir Simulado

Rota: `/simulados/:simuladoId/imprimir`. Gera uma versão formatada do simulado para impressão, com template dedicado (`templatePDF.ejs`).

#### Criar e Gerenciar Questões

- **Minhas questões** (`/simulados/questoes`) — lista as questões criadas pelo professor.
- **Criar questão** (`/simulados/registrar-questao/:tipo`) — o professor escolhe o tipo (`OBJETIVA` ou `DISSERTATIVA`) e preenche título, enunciado, área, tópicos e, para questões objetivas, as opções de resposta (A–E) e indica a correta.
- **Editar questão** (`/simulados/editar_questao/:id`) — altera os dados de uma questão existente.
- **Excluir questão** (`/simulados/excluir-questao/:id`) — remove a questão e suas opções associadas.

O campo de enunciado utiliza o editor de equações matemáticas com suporte a LaTeX.

#### Tópicos

Rota: `/simulados/meus-topicos` (visualização). Professores podem criar tópicos vinculados a uma área de conhecimento para categorizar questões.

#### Verificação de Similaridade por IA

Funcionalidade disponível apenas para professores. Ao cadastrar ou editar uma questão, o sistema pode acionar a função `comparaPerguntasIAGemini`, que consulta a API Gemini (Google) para identificar se já existe uma questão semanticamente similar no banco de dados. O resultado é exibido na tela de verificação de similaridade (`/simulados/views/professor/verificar_similaridade.ejs`), indicando os trechos similares encontrados.

---

### Para o Aluno

#### Visualizar Simulados

Rota: `/simulados/visualizar`. Exibe os simulados disponíveis na plataforma.

#### Fazer Simulado

Rota: `/simulados/:simuladoId/fazer`. O aluno responde ao simulado no tempo que desejar. Para questões objetivas, seleciona a alternativa (A–E). Para questões dissertativas, insere texto livre.

Ao finalizar, as respostas são submetidas via `POST /simulados/responder-prova/:simuladoId`.

#### Gabarito

Rota: `/simulados/:simuladoId/gabarito`. Exibe as respostas corretas após a realização do simulado.

---

## 3. IFQuiz

Acessível em `/quiz`. Módulo de gamificação com quizzes de múltipla escolha baseados em questões do ENEM.

### Fluxo do Usuário

1. **Página de entrada** (`/quiz/`) — apresentação do módulo, com botão para iniciar.
2. **Menu do Quiz** (`/quiz/MenuQuiz`) — o usuário seleciona a matéria e a quantidade de questões desejada.
3. **Tela de jogo** — exibe as questões uma a uma, buscadas da API externa `enem.dev`. Para cada questão, o usuário seleciona uma alternativa e recebe feedback imediato (correto/incorreto).
4. **Tela de resultados** — ao término, exibe o total de acertos, o total de questões e o percentual de eficiência.
5. **Placar** (`/quiz/placar`) — exibe o ranking dos 5 melhores jogadores, ordenados por número de acertos e percentual.

### Registro de Pontuação

Ao concluir o quiz, o resultado é enviado via `POST /quiz/api/Placar`. O sistema registra nome (do usuário logado ou "Visitante"), acertos, total de questões e percentual.

O ranking é recuperado via `GET /quiz/api/Placar`, retornando os 5 melhores registros.

---

## 4. Flashcards

Acessível em `/flashcards`. Módulo de estudo com repetição espaçada para revisão de conteúdo.

### Para o Aluno

#### Estudar Flashcards

Rota: `/flashcards/`. Exibe flashcards disponíveis com filtros opcionais por **Área**, **Tópico** e **Dificuldade** (Fácil, Médio, Difícil). Até 10 cartões são exibidos por vez, selecionados de forma aleatória conforme os filtros e o histórico de revisão do usuário.

Cada cartão exibe a pergunta na frente; ao virar, revela a resposta. A interação de virada utiliza animação CSS.

#### Repetição Espaçada

Ao visualizar um flashcard, o sistema registra a data do acesso na tabela `FlashcardUsuario` (campo `visto_por_ultimo`). A lógica de priorização agrupa os cartões por urgência de revisão com base nos intervalos: 1, 3, 7, 15 e mais de 15 dias desde o último acesso. Cartões não vistos ou com revisão mais antiga recebem maior prioridade.

#### Grupos

Rota: `/flashcards/grupos`. Permite ao aluno navegar os flashcards organizados por grupo/categoria.

---

### Para o Professor

#### Criar Flashcard

Rota: `GET /flashcards/criar` (formulário) + `POST /flashcards/criar`.

O professor preenche a pergunta, a resposta, a área, o tópico e o nível de dificuldade do cartão.

#### Editar Flashcard

Rota: `GET /flashcards/:id/editar` (formulário) + `POST /flashcards/:id/editar`.

Permite alterar qualquer campo do flashcard.

#### Excluir Flashcard

Rota: `POST /flashcards/:id/excluir`. Remove o flashcard do banco de dados.

---

## 5. Revisão de Conteúdo

Acessível em `/revisao`. Módulo de materiais de estudo criados pelos professores e consumidos pelos alunos.

### Para o Aluno

#### Navegar por Conteúdo

- **Home** (`/revisao/`) — página principal do módulo com acesso à navegação e busca.
- **Busca por assunto** (`/revisao/busca` ou `/revisao/busca/:id_assunto`) — exibe materiais organizados hierarquicamente por assunto. Os assuntos possuem estrutura em árvore (cada assunto pode ter subitens, definidos pelo campo `id_assunto_ascendente`).
- **Leitura** (`/revisao/leitura/:id_conteudo`) — exibe o material completo em Markdown renderizado. O sistema registra a leitura incrementando o contador `contagem_leituras` do conteúdo.

A busca também aceita pesquisa por área (`POST /revisao/buscar_area`), por tópico (`POST /revisao/buscar_topico`) e por material (`POST /revisao/buscar_material`).

---

### Para o Professor

#### Meus Materiais

Rota: `/revisao/meus_materiais`. Lista os conteúdos criados pelo professor logado.

#### Criar Material

Rota: `GET /revisao/criar_material` (formulário) + `POST /revisao/criar_material`.

O professor preenche:

- **Título** — nome do material (máx. 200 caracteres)
- **Área** e **Tópico** — categorização do conteúdo
- **Palavras-chave** — ao menos uma, usadas para busca e tagueamento
- **Conteúdo** — texto em Markdown, editado com o Editor Markdown integrado (mínimo 10 caracteres)
- **Links externos** — URLs opcionais de referência

#### Editar Material

Rota: `GET /revisao/editar_material/:id_conteudo` + `PATCH /revisao/editar_material/:id_conteudo`.

#### Remover Material

Rota: `DELETE /revisao/remover_material/:id_conteudo`. Remove o conteúdo do banco.

#### Upload de Arquivos

Rota: `POST /revisao/upload`. Permite anexar arquivos a materiais de revisão via upload (campo `file`).

---

## 6. Editor Markdown

O editor Markdown é um componente React + Vite isolado em `editor_markdown/`, compilado separadamente (`npm run build:editor`) e servido como assets estáticos pelo Express.

Ele é utilizado internamente nas telas de criação e edição de conteúdo do módulo de Revisão.

**Funcionalidades:**

- Edição de texto em formato Markdown com preview em tempo real
- Suporte a notação matemática LaTeX via extensão KaTeX (`marked-katex-extension`)
- Interface dividida em painel de edição e painel de visualização

O conteúdo produzido é armazenado no campo `conteudo_markdown` da tabela `Conteudo` e renderizado nas páginas de leitura do módulo de Revisão.

---

## 7. Gestão Compartilhada (Shared)

Acessível em `/shared`. Contém funcionalidades administrativas compartilhadas entre os domínios.

### Áreas de Conhecimento

- **Listar** (`GET /shared/areas`) — exibe todas as áreas cadastradas
- **Listar em JSON** (`GET /shared/api/areas`) — retorna as áreas em formato JSON para uso interno
- **Criar** (`POST /shared/areas`)
- **Editar** (`PATCH /shared/areas/:id_area`)
- **Excluir** (`DELETE /shared/areas/:id_area`)

As áreas pré-cadastradas via seeder são: Matemática, Português, História, Geografia, Ciências, Artes, Informática, Química, Física, Biologia, Filosofia, Sociologia, Educação Física e Língua Estrangeira.

### Assuntos

- **Listar** (`GET /shared/assuntos`)
- **Criar** (`POST /shared/assuntos`)
- **Editar** (`PATCH /shared/assuntos/:id_assunto`)
- **Excluir** (`DELETE /shared/assuntos/:id_assunto`)

Assuntos suportam hierarquia — cada assunto pode ter um assunto ascendente (`id_assunto_ascendente`), formando uma árvore de categorias de conteúdo.

### Tópicos

- **Listar** (`GET /shared/topicos`)
- **Criar** (`POST /shared/topicos`)
- **Editar** (`PATCH /shared/topicos/:id_topico`)
- **Excluir** (`DELETE /shared/topicos/:id_topico`)
- **Consultar por área** (`GET /shared/api/topicos/:id_area`) — retorna tópicos em JSON filtrados por área, usado por outros domínios

### Política de Privacidade

Rota: `/shared/politica_de_privacidade`. Página da Política de Privacidade do IFVest, elaborada em conformidade com a LGPD, exibida sem o layout padrão da plataforma (layout independente).

---

## 8. Perfis de Usuário e Controle de Acesso

O sistema possui dois perfis:

| Perfil | Acesso |
|---|---|
| `USUARIO` (Aluno) | Fazer simulados, usar IFQuiz, estudar flashcards, ler materiais de revisão, editar próprio perfil |
| `PROFESSOR` | Tudo do aluno + criar/editar/excluir questões, simulados, flashcards, tópicos, áreas, assuntos e materiais de revisão |

O controle de acesso é baseado em sessão. O middleware `sessionMidleware.js` (`secure_pass`) protege as rotas autenticadas, redirecionando para `/login` caso não haja sessão ativa. O perfil do usuário (`req.session.perfil`) é disponibilizado para as views via `authLocals.js`.

---

!!! note "Funcionalidades em desenvolvimento"
    Os seguintes módulos estão em desenvolvimento ativo por equipes de subprojeto e ainda não estão disponíveis em produção: correção automatizada de redações (Arthur, Douglas e Guilherme), migração do frontend para React (Isabella e Maria Luiza), integração com APIs do ENEM e FUVEST (Vitor, Helena e Thales), e sistema de recomendação personalizado (João Pedro).
