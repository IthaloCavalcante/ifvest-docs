# IFVest — Documentação

Documentação técnica oficial da plataforma **IFVest**, projeto de extensão do IFSP Campus Jacareí dedicado à preparação gratuita de estudantes para o ENEM e vestibulares.

[Acessar a Plataforma IFVest](https://ifvest.jcr.ifsp.edu.br/home){ .md-button .md-button--primary target="_blank" }

!!! warning "Projeto em desenvolvimento ativo"
    O IFVest evolui continuamente através de múltiplos subprojetos de extensão. Esta documentação acompanha o estado real do sistema e é atualizada conforme o desenvolvimento avança — consulte o [planejamento](planejamento.md) para o status de cada item.

---

## Sobre o Projeto

- **Instituição:** IFSP — Campus Jacareí, curso de Tecnologia em Análise e Desenvolvimento de Sistemas (ADS)
- **Origem:** TCCs de Fonseca e Sousa (2021), resgatado e reconstruído integralmente por Cristian Rodolfo Zago Da Silva (2024)
- **Stack atual:** Node.js, Express, Sequelize e MySQL, com integração híbrida de componentes React
- **Status:** versão v2 em produção, com subprojetos de extensão ativos organizados em quatro eixos

Veja a [Descrição do Sistema](descricao-do-sistema.md) completa para contexto, motivação, público-alvo e histórico detalhado.

---

## Como Esta Documentação Está Organizada

A documentação está dividida pelas perguntas que ela responde sobre o sistema:

| Seção | Responde |
|---|---|
| **[Descrição do Sistema](descricao-do-sistema.md)** | O que é o IFVest, qual problema resolve e quem usa |
| **[Arquitetura do Sistema](arquitetura.md)** e **Diagramas C4** ([Contexto](c4/contexto.md), [Contêineres](c4/containers.md), [Componentes](c4/componentes.md)) | Como o sistema está construído |
| **Requisitos** ([Funcionais](requisitos/funcionais.md), [Não-Funcionais](requisitos/nao-funcionais.md)) | O que o sistema deve fazer |
| **[Descrição das Funcionalidades](funcionalidades.md)** | O que o sistema faz hoje |
| **[Guias de Uso](guias/index.md)** | Como usar a plataforma, tarefa por tarefa |
| **[Registro de Versões](versoes.md)** | O que mudou até agora |
| **[Subprojetos Ativos](subprojetos/index.md)** | O que está sendo construído: [Frontend](subprojetos/frontend.md), [Qualidade e Testes](subprojetos/qualidade-e-testes.md), [IA e Recomendação](subprojetos/ia-e-recomendacao.md) e [Infraestrutura e Segurança](subprojetos/infra-e-seguranca.md) |

A ordem em que esses itens foram produzidos, as normas adotadas e os critérios aplicados estão no [planejamento da documentação](planejamento.md).

---

## Por Onde Começar

=== "Avaliadores e banca"

    Comece pela [Descrição do Sistema](descricao-do-sistema.md) para entender o propósito e o escopo do projeto, seguida da [Arquitetura](arquitetura.md) para os aspectos técnicos.

=== "Novos colaboradores"

    Leia a [Arquitetura do Sistema](arquitetura.md) e os [Diagramas C4](c4/contexto.md) antes de explorar a documentação do eixo de [Subprojetos](subprojetos/index.md) em que for atuar.

=== "Consulta de requisitos"

    Vá direto aos [Requisitos Funcionais](requisitos/funcionais.md) ou [Requisitos Não-Funcionais](requisitos/nao-funcionais.md).

---

Esta documentação é voltada a avaliadores, colaboradores e demais pessoas externas à equipe de desenvolvimento, e segue como referência a norma **ISO/IEC/IEEE 15289:2019**.
