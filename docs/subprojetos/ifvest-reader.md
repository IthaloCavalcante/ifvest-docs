# IFVest Reader

Aplicativo leitor de documentos PDF voltado ao estudo, desenvolvido como subprojeto vinculado ao IFVest. Diferente dos demais subprojetos, que evoluem a plataforma web, este **produziu um software próprio**: um aplicativo instalado no dispositivo do estudante, com funcionamento independente da plataforma.

!!! info "Como esta página se distingue das demais"
    As páginas de eixo descrevem frentes de trabalho **sobre a plataforma**. Esta descreve um **produto de software distinto**, gerado por um subprojeto do IFVest. Por isso, adota uma estrutura de descrição de sistema reduzida — propósito, funcionalidades, arquitetura e relação com a plataforma.

---

## Situação atual

| | |
|---|---|
| **Tipo** | Aplicativo multiplataforma (software independente) |
| **Situação** | Em desenvolvimento — versão 0.1.0 |
| **Código-fonte** | Disponibilizado pelo autor do subprojeto |
| **Distribuição** | ⬜ Não definida — não há instalador nem publicação em loja de aplicativos |
| **Relação com a plataforma** | Ferramenta complementar; não é módulo do IFVest (ver [Relação com a plataforma](#relacao-com-a-plataforma-ifvest)) |

---

## Propósito

O aplicativo oferece um ambiente de leitura de PDF voltado ao estudo, reunindo em um só lugar os documentos do estudante e os recursos de apoio à leitura: anotações sobre o texto, organização por categorias, leitura em voz alta e retomada do ponto onde a leitura parou.

A proposta apresentada ao projeto é que o IFVest possa **recomendar seu uso** aos estudantes como ferramenta de apoio, sem que ele constitua uma funcionalidade da plataforma.

---

## Funcionalidades

As funcionalidades abaixo foram verificadas na estrutura do código-fonte.

### Leitura

- Abertura de documentos PDF selecionados a partir do próprio dispositivo.
- **Busca textual** dentro do documento.
- **Modo leitura**, com sobreposição de configurações próprias de exibição.
- Controle de navegação entre páginas.

### Leitura em voz alta

- Conversão do texto do documento em áudio, com controle de reprodução.
- Leitura cumulativa, que acompanha o avanço do texto.

### Anotações

- Marcações e comentários vinculados a um **trecho específico** de uma página.
- Cada anotação registra o documento, a página, o tipo, o conteúdo e a área marcada.

### Organização

- **Categorias** criadas pelo próprio usuário para agrupar documentos.
- Registro da **última página acessada** por documento, permitindo retomar a leitura.
- Registro da data do último acesso.
- Tela de configurações do aplicativo.

---

## Arquitetura

### Tecnologias

| Camada | Tecnologia |
|---|---|
| **Framework** | Flutter (Dart) |
| **Renderização de PDF** | `pdfx` e `syncfusion_flutter_pdfviewer` |
| **Manipulação de PDF** | `syncfusion_flutter_pdf` |
| **Leitura em voz alta** | `flutter_tts` |
| **Banco de dados local** | Drift sobre SQLite |
| **Seleção de arquivos** | `file_picker`, `image_picker` |
| **Preferências e caminhos** | `shared_preferences`, `path_provider` |

O projeto contém as pastas de build para **Android, iOS, Web, Windows, Linux e macOS**, características de um projeto Flutter multiplataforma. ⬜ *A confirmar com o autor em quais dessas plataformas o aplicativo foi efetivamente testado.*

### Modelo de dados

Todo o armazenamento é **local ao dispositivo**, em banco SQLite gerenciado pelo Drift, com quatro tabelas:

| Tabela | Conteúdo |
|---|---|
| **Document** | Nome, arquivo (caminho ou conteúdo), data do último acesso, última página lida e categoria |
| **Category** | Nome da categoria criada pelo usuário |
| **Annotation** | Documento, página, tipo, conteúdo e área marcada da anotação |
| **Config** | Preferências do aplicativo, em pares de chave e valor |

Cada tabela possui um objeto de acesso a dados próprio, e a conexão com o banco tem implementações distintas para plataformas nativas e para a web.

---

## Relação com a plataforma IFVest

!!! warning "Divergência entre a documentação do repositório e o código-fonte"
    O arquivo de apresentação do repositório descreve o aplicativo como **integrado nativamente à plataforma IFVest**, mencionando a centralização de materiais didáticos e o consumo das APIs REST da plataforma.

    Na análise do código-fonte, **nenhuma integração foi localizada**: não há chamadas à plataforma, endereços de API ou qualquer referência ao IFVest no código do aplicativo. Os documentos são obtidos exclusivamente do dispositivo do usuário, por seleção manual de arquivo, e armazenados apenas localmente.

    Esta página adota o **comportamento verificado no código**. A integração descrita é registrada como **intenção declarada**, não como característica existente.

    ⬜ *A esclarecer com o autor do subprojeto: se a integração está prevista para versões futuras e em que forma.*

**O que isso significa na prática.** Na versão atual, o aplicativo é um leitor de PDF autônomo: o estudante escolhe os arquivos que quer ler, incluindo materiais baixados do IFVest, mas o aplicativo não os obtém da plataforma nem envia informação de volta. Progresso de leitura e anotações permanecem no dispositivo.

---

## Pendências

| Pendência | Impacto |
|---|---|
| ⬜ **Forma de distribuição** | Sem instalador ou publicação, o aplicativo não pode ser recomendado aos estudantes |
| ⬜ **Integração com a plataforma** | Definir se está prevista e em que forma |
| ⬜ **Plataformas suportadas** | Confirmar em quais sistemas o aplicativo foi testado |
| ⬜ **Relatório do subprojeto** | Ainda não disponível; a análise atual baseia-se no código-fonte e no repositório |

!!! note "Sobre o nome"
    O produto é referido nesta documentação como **IFVest Reader**, nome adotado oficialmente pelo projeto. O repositório e o pacote interno do aplicativo utilizam outras denominações, de origem técnica.

---

## Fontes desta página

| Camada | Fonte | Data |
|---|---|---|
| Funcionalidades, arquitetura, modelo de dados e plataformas | Código-fonte do repositório do aplicativo (versão 0.1.0) | ago/2026 |
| Propósito e integração declarada | Documento de apresentação do repositório | ago/2026 |
| Enquadramento como ferramenta complementar | Apresentação do subprojeto em reunião do projeto de extensão | ago/2026 |
