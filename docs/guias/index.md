# Guias de Uso do IFVest

Esta é a documentação de usuário do IFVest: como usar a plataforma, tarefa por tarefa. Escolha por onde começar.

| Se você é... | Vá para | O que encontra |
|---|---|---|
| **Aluno** | [Guia do Aluno](aluno/index.md) | Estudar pelos módulos de Revisão, IFQuiz, Flashcards e Simulados |
| **Professor** | [Guia do Professor](professor/index.md) | Criar e gerenciar questões, simulados, flashcards e materiais |

**Todos os perfis** usam as mesmas páginas de conta:

- [Acesso e Conta](conta/acesso.md) — criar conta, entrar, recuperar senha, sair
- [Perfil e Seus Dados](conta/perfil.md) — editar dados, foto e senha; excluir a conta

Onde uma tarefa de conta funciona de forma diferente conforme o perfil, a diferença está sinalizada na própria página.

Os termos usados na plataforma estão no [Glossário](glossario.md).

---

## Qual versão da plataforma esta documentação descreve

!!! warning "Leia antes de usar os guias"
    O IFVest está em processo de **refatoração do frontend** (migração para React, com redesign completo da interface). Por orientação do projeto, os guias são escritos tendo a **plataforma refatorada como referência**, para evitar documentar telas transitórias que serão substituídas.

    Cada tarefa distingue duas camadas:

    - O **fluxo da tarefa** (objetivo, pré-requisitos, sequência de passos) — válido hoje e após a refatoração, verificado no sistema em produção.
    - A **interface** (telas, botões, navegação) — descrita nos blocos *"Na versão refatorada"*, com base nos relatórios do subprojeto de frontend. Esse design **ainda está em elaboração e pode mudar** até a entrega.

    Capturas de tela e instruções visuais definitivas serão adicionadas quando a interface React estabilizar.

---

## Como ler as tarefas

Cada tarefa dos guias segue a mesma estrutura, baseada na **ISO/IEC/IEEE 26514:2022** — *Design and development of information for users*:

| Campo | O que informa |
|---|---|
| **Status** | Se a tarefa funciona hoje ou é prevista no redesign (ver legenda abaixo) |
| **Objetivo** | O que você realiza ao completar a tarefa |
| **Pré-requisitos** | O que precisa estar pronto antes |
| **Como fazer** | A sequência de passos, do início ao resultado |
| **Na versão refatorada** | Como a tela/fluxo ficará no novo design, com a fonte citada |
| **Observações** | Limites, validações e situações comuns |

O Guia do Professor acrescenta o campo **Perfil**, que indica a qual perfil cada tarefa pertence enquanto a redistribuição entre professor e administrador não é concluída.

### Legenda de status

- ✅ **Atual** — a tarefa funciona hoje na plataforma em produção. A interface será redesenhada, mas o fluxo permanece.
- 🟡 **Refatorado (em design)** — a tarefa **ainda não existe** na plataforma atual; está prevista no design da versão refatorada.
- 🔵 **Em deliberação** — a tarefa **ainda não foi decidida**: o projeto avalia se ela existirá. Documentada aqui porque há design proposto, mas **pode não ser implementada**.
- ⬜ **Pendência** — item aguardando confirmação ou material (captura de tela, verificação na plataforma, decisão do projeto).

Toda informação da camada *"Na versão refatorada"* cita sua fonte (relatório e figura do subprojeto de frontend), seguindo o critério desta documentação: **nada é documentado sem evidência confirmada**.

Alguns comportamentos aparecem marcados como *"conforme o código-fonte da plataforma anterior ao redesign"*. São detalhes verificados diretamente no repositório do projeto — regras de validação, restrições de acesso e efeitos de exclusão — e não em uso da plataforma. A distinção é registrada porque o repositório pode não corresponder exatamente ao que está no ar.

---

## Acessibilidade da plataforma

Os módulos de **Simulados**, **Flashcards** e **IFQuiz** passaram por avaliação e ajustes de acessibilidade conduzidos pelo subprojeto responsável. Na prática, isso significa que estes módulos podem ser usados:

- **apenas com o teclado**, com indicação visível de onde está o foco e ordem de tabulação adequada;
- **com leitor de tela**, que percorre e lê o conteúdo das páginas.

As telas de confirmação e a página de geração de PDF, que apresentavam falhas de foco, tabulação e leitura, também foram corrigidas. Os ajustes foram verificados em teste conduzido com um usuário cego, navegando pela plataforma apenas com teclado e leitor de tela (NVDA).

*Fonte: relatório final do subprojeto de acessibilidade (2025).*

### Normas de referência

A acessibilidade da plataforma é avaliada com base em dois referenciais adotados pelo projeto:

- **WCAG 2.2** (*Web Content Accessibility Guidelines*, W3C) — conjunto internacional de diretrizes organizado em quatro princípios: conteúdo perceptível, operável, compreensível e robusto.
- **ABNT NBR 17225:2025** — norma brasileira de acessibilidade em produtos e serviços digitais, alinhada às WCAG 2.2. Ela regulamenta o Art. 63 da Lei Brasileira de Inclusão da Pessoa com Deficiência (Lei nº 13.146/2015) e adota o **nível AA** de conformidade como padrão.

!!! note "Estas são as normas de referência, não uma declaração de conformidade"
    A avaliação de acessibilidade do IFVest está **em andamento**. As auditorias automatizadas, inspeções técnicas e validações manuais realizadas até o momento identificaram pontos a corrigir — entre eles estrutura semântica, contraste entre cores, navegação por teclado, hierarquia de cabeçalhos e uso de atributos de acessibilidade.

    Portanto, esta documentação registra **quais normas orientam o trabalho** e quais ajustes já foram aplicados, sem afirmar que a plataforma atende integralmente a um nível de conformidade.

*Fonte: estudo de benchmark e aplicação de ferramentas de avaliação de acessibilidade no IFVest, subprojeto de testes de software (2026).*

⬜ *A atualizar quando a avaliação de acessibilidade for concluída e houver resultado consolidado por nível de conformidade.*

### Convenções de acessibilidade destes guias

- Toda captura de tela terá **texto alternativo** descritivo — as pendências ⬜ de captura já reservam esse campo.
- Os marcadores de status **nunca dependem apenas de símbolo ou cor**: vêm sempre acompanhados da palavra correspondente (Atual, Refatorado, Pendente).
- A hierarquia de títulos é consistente (página → tarefa) para permitir navegação por leitores de tela.

---

## Onde esta documentação se encaixa

Estes guias constituem o item **"Documentação de Usuário"** previsto no mapeamento da **ISO/IEC/IEEE 15289:2019** adotado pelo projeto, com estrutura e conteúdo conforme a **ISO/IEC/IEEE 26514:2022**. O registro de conformidade de cada guia — quais elementos da norma foram aplicados e quais foram adiados, com justificativa — está na página inicial do [Guia do Aluno](aluno/index.md#conformidade-com-as-normas) e do [Guia do Professor](professor/index.md#conformidade-com-as-normas).

Para o plano geral da documentação e as demais fases, ver [Planejamento da Documentação](../planejamento.md).
