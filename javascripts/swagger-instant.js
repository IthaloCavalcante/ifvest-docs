/*
   IFVest — Documentação
   Swagger UI (plugin mkdocs-swagger-ui-tag) com a navegação instantânea do Material

   O plugin troca a tag <swagger-ui> da Referência da API por um iframe e põe,
   no fim da página, o script de que esse iframe depende: a função que ajusta
   a altura dele e o aviso de tema claro/escuro.

   Com navigation.instant, o Material não recarrega a página ao seguir um link:
   troca só o conteúdo e roda de novo apenas os scripts que estão dentro dele.
   O script do plugin fica de fora, então quem chega à Referência da API por um
   link fica sem essas funções. O iframe para na altura padrão de 150 px e o
   tema não é aplicado, até alguém dar F5.

   Este arquivo entra em extra_javascript. O Material o carrega uma vez, na
   primeira página aberta, e as funções abaixo passam a valer para o site
   inteiro. Os nomes são os que o iframe do plugin procura (versão 0.8.1).
*/
(function () {
  "use strict";

  var ESQUEMA_ESCURO = "slate"; // o mesmo "scheme" do tema escuro no mkdocs.yml

  function temaEscuro() {
    return document.body.getAttribute("data-md-color-scheme") === ESQUEMA_ESCURO;
  }

  function iframesDoSwagger() {
    return document.querySelectorAll("iframe.swagger-ui-iframe");
  }

  function aplicarTema(iframe) {
    var janela = iframe.contentWindow;
    if (!janela || !janela.enable_dark_mode) return;
    if (temaEscuro()) {
      janela.enable_dark_mode();
    } else {
      janela.disable_dark_mode();
    }
  }

  // Altura: o iframe chama esta função sempre que o conteúdo dele muda de tamanho
  window.update_swagger_ui_iframe_height = function (id) {
    var iframe = document.getElementById(id);
    if (!iframe || !iframe.contentWindow) return;
    var altura = iframe.contentWindow.document.body.scrollHeight + 80 + "px";
    iframe.height = altura;
    iframe.style.height = altura;
  };

  // Tema inicial: o iframe consulta esta variável ao terminar de carregar.
  // Ela passa a ser calculada na hora da consulta; o valor que o script do
  // plugin tenta gravar é ignorado, porque às vezes ele calcula errado.
  Object.defineProperty(window, "__init_is_dark_mode", {
    configurable: true,
    get: temaEscuro,
    set: function () {}
  });

  // Troca de tema pelo botão do cabeçalho
  new MutationObserver(function () {
    iframesDoSwagger().forEach(aplicarTema);
  }).observe(document.body, { attributeFilter: ["data-md-color-scheme"] });

  // A cada página aberta: confere o tema quando o iframe terminar de carregar
  document$.subscribe(function () {
    iframesDoSwagger().forEach(function (iframe) {
      iframe.addEventListener("load", function () {
        aplicarTema(iframe);
      });
    });
  });

  // Janelas do Swagger (como a de "Authorize") acompanham a rolagem da página
  var agendado = false;
  document.addEventListener("scroll", function () {
    if (agendado) return;
    agendado = true;
    window.requestAnimationFrame(function () {
      var meiaTela = window.innerHeight / 2;
      iframesDoSwagger().forEach(function (iframe) {
        var janela = iframe.contentWindow;
        if (janela && janela.update_top_val) {
          janela.update_top_val(meiaTela - iframe.getBoundingClientRect().top);
        }
      });
      agendado = false;
    });
  }, { passive: true });
})();
