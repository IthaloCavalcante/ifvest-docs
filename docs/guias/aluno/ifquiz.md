# IFQuiz

O **IFQuiz** (`/quiz`) é o módulo de gamificação do IFVest: quizzes de múltipla escolha com questões do ENEM, com resposta corrigida na hora e um placar dos melhores desempenhos. O módulo exige [conta e sessão ativa](../conta/acesso.md#tarefa-2-entrar-na-sua-conta). Diferente dos [Simulados](simulados.md), o foco aqui é a prática rápida e o retorno imediato, não a simulação de uma prova completa.

!!! info "Versão documentada"
    Os fluxos abaixo funcionam na plataforma atual. **Esta é a página do guia com a menor cobertura da versão refatorada**: o módulo está sendo reconstruído e as telas do novo design ainda não estão disponíveis para consulta (ver [Sobre a reconstrução do módulo](#sobre-a-reconstrucao-do-modulo)). Veja [como ler as tarefas](index.md#como-ler-as-tarefas-deste-guia).

---

## Tarefa 1 — Jogar um quiz

**Status:** ✅ Atual

**Objetivo:** praticar questões do ENEM de uma matéria à sua escolha, com correção imediata a cada resposta.

**Pré-requisitos:** [estar logado](../conta/acesso.md#tarefa-2-entrar-na-sua-conta).

**Como fazer:**

1. Acesse o módulo **IFQuiz** (`/quiz`). A página de entrada apresenta o módulo e traz o botão para iniciar.
2. No **menu do quiz**, escolha a **matéria** e a **quantidade de questões** que deseja responder.
3. As questões são exibidas **uma a uma**. Para cada uma, selecione uma alternativa.
4. A correção é **imediata**: ao responder, você já vê se acertou ou errou, e então segue para a questão seguinte.
5. Ao terminar a última questão, o resultado é exibido (ver [Tarefa 2](#tarefa-2-ver-seu-resultado)).

!!! note "Sobre o registro \"Visitante\" no placar"
    O placar prevê o registro de pontuações sob o nome **"Visitante"**, quando a partida não está associada a um usuário identificado. Como o módulo exige sessão ativa, essa situação é excepcional — o esperado é que seu resultado apareça com o seu nome.

**Observações:**

- As questões são obtidas de um **serviço externo de questões do ENEM**. Se esse serviço estiver indisponível, as questões podem não carregar — nesse caso, tente novamente mais tarde.

---

## Tarefa 2 — Ver seu resultado

**Status:** ✅ Atual

**Objetivo:** conferir seu desempenho ao final do quiz.

**Pré-requisitos:** ter concluído um quiz.

**Como fazer:**

1. Ao responder a última questão, a **tela de resultados** é exibida automaticamente, com:

    - o **total de acertos**;
    - o **total de questões** respondidas;
    - o **[percentual de eficiência](../glossario.md#termos)** (proporção de acertos).

2. O resultado é enviado ao placar assim que o quiz é concluído — não é preciso fazer nada para registrá-lo.

**Observações:**

- Como o registro é automático, **todo quiz concluído entra no placar** — com seu nome, se você estiver logado, ou como "Visitante".
- Por consultar o percentual junto com o total de questões, vale saber: um quiz curto com 100% de acertos e um quiz longo com 100% de acertos aparecem com o mesmo percentual, mas com totais diferentes. O placar considera as duas informações (ver [Tarefa 3](#tarefa-3-ver-o-placar)).

---

## Tarefa 3 — Ver o placar

**Status:** ✅ Atual

**Objetivo:** comparar seu desempenho com os melhores resultados da plataforma.

**Pré-requisitos:** estar logado.

**Como fazer:**

1. Acesse o **placar** (`/quiz/placar`).
2. São exibidos os **5 melhores resultados**, ordenados por **número de acertos** e por **percentual**.

**Observações:**

- O placar mostra apenas o **top 5** — não há histórico pessoal de partidas nem posição individual fora dessas cinco primeiras colocações.

---

## Sobre a reconstrução do módulo

O IFQuiz está sendo reconstruído pelo subprojeto de continuidade do módulo, com telas novas e um backend próprio. Diferente dos outros módulos deste guia, **as telas do novo design não estão disponíveis no material consultado**, e por isso as tarefas acima não têm o bloco *"Na versão refatorada"*.

O que está registrado até o momento:

- As **telas do novo IFQuiz foram desenhadas** e os requisitos funcionais e não funcionais do módulo foram levantados e validados (maio/2026). ⬜ *Pendência: obter as telas e os requisitos com a responsável pelo subprojeto, para escrever a camada de interface futura desta página.*
- Está prevista a inclusão de **filtros** na escolha das questões, baseados em um sistema de **tags** definido em conjunto com os subprojetos das APIs de vestibulares. ⬜ *Quais filtros e como serão apresentados ainda não está detalhado.*
- O desenvolvimento do frontend em React do módulo teve início em junho/2026, posterior às demais telas do redesign.

*Fonte: atas de reunião do subprojeto de continuidade do IFQuiz (abr–jun/2026).*

!!! note "O que muda para você"
    A reconstrução inclui a troca da tecnologia de backend do módulo. Como no restante da plataforma, essa mudança é **invisível no uso** — os detalhes técnicos pertencem à [Descrição da Arquitetura](../../arquitetura.md), não a este guia. O que efetivamente mudará na sua experiência são as telas e os filtros, ainda a documentar.

---

## Acessibilidade

O IFQuiz está entre os módulos avaliados e ajustados para navegação apenas por teclado e uso com leitor de tela. Os detalhes estão em [Acessibilidade da plataforma](../index.md#acessibilidade-da-plataforma).

---

## Erros e situações comuns

| Situação | O que fazer |
|---|---|
| As questões não carregam | O quiz depende de um serviço externo de questões do ENEM. Se ele estiver fora do ar, aguarde e tente novamente — não é um problema da sua conta |
| Meu resultado apareceu como "Visitante" | O registro não foi associado à sua conta. Confira se sua sessão continua ativa e refaça o quiz |
| Meu resultado não aparece no placar | O placar exibe apenas os 5 melhores resultados; desempenhos fora dessa faixa não são listados |
| ⬜ Mensagens de erro específicas | As mensagens exatas exibidas pela plataforma serão documentadas junto com as capturas de tela, quando a interface refatorada estabilizar |

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Fluxos atuais (Tarefas 1–3): menu, jogo, resultados, placar e registro de pontuação | [Descrição das Funcionalidades](../../funcionalidades.md) — módulo IFQuiz, derivada do código-fonte (rotas `/quiz/*`) | jun/2026 |
| Estado da reconstrução do módulo, telas e filtros previstos | Atas de reunião do subprojeto de continuidade do IFQuiz | abr–jun/2026 |
| Acessibilidade (teclado e leitor de tela) | Relatório final do subprojeto de acessibilidade | 2025 |

Nenhum dos relatórios de redesign de frontend consultados (Isabella Pereira e Maria Luiza) cobre as telas do IFQuiz — o módulo é conduzido por subprojeto próprio.
