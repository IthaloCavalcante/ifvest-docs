# Referência da API

Esta página apresenta a especificação completa da API REST do IFVest: todas as rotas, seus parâmetros, os formatos de requisição e resposta, e os esquemas de dados.

!!! info "Sobre esta especificação"
    A especificação segue o padrão **OpenAPI 3.1** e foi **gerada a partir do código-fonte em produção**, e não escrita à mão. Ela reflete exatamente as rotas implementadas: **60 rotas e 80 esquemas de dados**. Cada rota é uma combinação de método e caminho — `GET` e `PUT` em `/features/{flag_key}`, por exemplo, contam como duas.

    Em produção, a documentação interativa gerada pelo FastAPI está fechada de propósito. Esta versão é estática: permite consultar a API **sem expor o ambiente de produção**. Por isso, o botão de testar as chamadas não funciona aqui.

---

## Visão geral

Todas as rotas estão sob o prefixo **`/api/v1`** e trocam dados em JSON.

| Grupo | Rotas | Cobre |
|---|---|---|
| `quiz` | 18 | Partidas, pergunta do dia, filtros de montagem, ranking, loja de avatares e histórico |
| `mocktests` | 12 | Montagem, resolução e correção de simulados, exportação em PDF, histórico e estatísticas |
| `essays` | 11 | Propostas, envio de redações, fila de correção, correção e histórico do corretor |
| `users` | 6 | Perfil do usuário, lista de usuários e concessão e revogação de permissões |
| `question-bank` | 5 | Busca, cadastro e edição de questões, e denúncia de erros |
| `features` | 3 | Consulta e alteração das feature flags |
| `admin` | 3 | Painel de indicadores e moderação das denúncias de questões |
| `auth` | 2 | Sessão do usuário |

O banco de questões tem grupo próprio porque é compartilhado pelos Simulados e pelo IFQuiz, mas manteve os caminhos `/mocktests/questions` para não quebrar os clientes que já os usavam.

### Autenticação

As rotas protegidas exigem o **token de identidade do Firebase** no cabeçalho de cada requisição:

```http
Authorization: Bearer <token-do-firebase>
```

O backend verifica o token, identifica o usuário e aplica as permissões que ele possui. Uma chamada a uma rota que exige permissão que o usuário não tem é recusada, com a indicação da permissão ausente. Ver [Arquitetura — Autenticação e autorização](arquitetura.md#autenticacao-e-autorizacao).

Três consultas respondem **sem token**: a situação dos módulos (`GET /features`) e as propostas de redação, na lista e no detalhe.

O registro do usuário é criado por `POST /auth/login`, no primeiro acesso. Até essa chamada, as demais rotas protegidas respondem **401** mesmo com um token válido, porque o usuário ainda não existe no banco.

### Feature flags

Rotas de módulos desligados são recusadas pelo backend com o código **503**, mesmo quando o usuário tem permissão. Ver [Arquitetura — Feature flags](arquitetura.md#feature-flags).

### Paginação

As listas que podem crescer muito — banco de questões, usuários e denúncias — são paginadas pelos parâmetros `limit` e `offset`. O total de itens, somando todas as páginas, vem no cabeçalho `X-Total-Count` da resposta.

---

## Especificação

<swagger-ui src="openapi.json"/>

---

## Como atualizar esta página

A especificação é gerada pelo próprio FastAPI a partir das rotas e dos esquemas Pydantic do backend, pelo script `scripts/gerar_openapi.py`, deste repositório. Após alterações na API, rode-o para que o arquivo `openapi.json` continue correspondendo ao que está implementado. Com o monorepo clonado ao lado deste repositório:

```bash
py -m pip install --user -r ../ifvest-monorepo/ifvest-backend/requirements.txt
py scripts/gerar_openapi.py ../ifvest-monorepo/ifvest-backend
```

O script importa a aplicação sem subir o servidor nem conectar ao banco, grava `docs/openapi.json` e mostra quantas rotas cada grupo tem. Esses números aparecem nesta página e na [Arquitetura](arquitetura.md#api), que são escritas à mão: confira se mudaram.

O arquivo também pode ser **baixado** e importado em ferramentas como Postman ou Insomnia: [openapi.json](openapi.json).

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Especificação OpenAPI | Gerada a partir do código-fonte do `ifvest-monorepo` (`ifvest-backend/src/`) pelo script de geração | set/2026 |
| Rotas sem autenticação e paginação | `ifvest-backend/src/api/v1/` e `src/core/pagination.py` | set/2026 |
