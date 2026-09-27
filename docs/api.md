# Referência da API

Esta página apresenta a especificação completa da API REST do IFVest: todas as rotas, seus parâmetros, os formatos de requisição e resposta, e os esquemas de dados.

!!! info "Sobre esta especificação"
    A especificação segue o padrão **OpenAPI 3.1** e foi **gerada a partir do código-fonte em produção**, e não escrita à mão. Ela reflete exatamente as rotas implementadas: **43 rotas e 63 esquemas de dados**.

    Em produção, a documentação interativa gerada pelo FastAPI está fechada de propósito. Esta versão é estática: permite consultar a API **sem expor o ambiente de produção**. Por isso, o botão de testar as chamadas não funciona aqui.

---

## Visão geral

Todas as rotas estão sob o prefixo **`/api/v1`** e trocam dados em JSON.

| Grupo | Rotas | Cobre |
|---|---|---|
| `quiz` | 17 | Partidas, pergunta do dia, ranking, loja de avatares e histórico |
| `mocktests` | 14 | Questões, simulados e tentativas |
| `essays` | 11 | Propostas, redações e correções |
| `users` | 4 | Perfil do usuário |
| `features` | 3 | Consulta e alteração das feature flags |
| `auth` | 2 | Sessão do usuário |

### Autenticação

As rotas protegidas exigem o **token de identidade do Firebase** no cabeçalho de cada requisição:

```http
Authorization: Bearer <token-do-firebase>
```

O backend verifica o token, identifica o usuário e aplica as permissões que ele possui. Uma chamada a uma rota que exige permissão que o usuário não tem é recusada, com a indicação da permissão ausente. Ver [Arquitetura — Autenticação e autorização](arquitetura.md#autenticacao-e-autorizacao).

### Feature flags

Rotas de módulos desligados são recusadas pelo backend, mesmo quando o usuário tem permissão. Ver [Arquitetura — Feature flags](arquitetura.md#feature-flags).

---

## Especificação

<swagger-ui src="openapi.json"/>

---

## Como atualizar esta página

A especificação é gerada pelo próprio FastAPI a partir das rotas e dos esquemas Pydantic do backend. Após alterações na API, o arquivo `openapi.json` deve ser regenerado para que esta página continue correspondendo ao que está implementado.

O arquivo também pode ser **baixado** e importado em ferramentas como Postman ou Insomnia: [openapi.json](openapi.json).

⬜ *Pendente: disponibilizar o script de geração no repositório, para que a atualização possa ser feita por qualquer pessoa da equipe.*

---

## Fontes desta página

| Conteúdo | Fonte | Data |
|---|---|---|
| Especificação OpenAPI | Gerada a partir do código-fonte do `ifvest-monorepo` (`ifvest-backend/src/`) | set/2026 |
