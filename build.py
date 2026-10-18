# -*- coding: utf-8 -*-
"""Gera as paginas do grupotr3.com.br. Copy: napoleao/docs/SITE-TR3-ESTRUTURA.md (17/10/2026),
com os ajustes do Diego: 'assessoria comercial B2B' na voz da marca, Pablo Marcal como socio,
endereco Avenida Ipanema 165 (conferido na Receita e no perfil do Google)."""
from pathlib import Path

RAIZ = Path(__file__).parent
LOGO = (RAIZ / "assets/marca.html").read_text(encoding="utf-8")
LOGO_FOOT = (RAIZ / "assets/marca-foot.html").read_text(encoding="utf-8")
SITE = "https://grupotr3.com.br"
TEL = "(62) 99139-7882"
EMAIL = "contato@diegovicente.com.br"
ENDERECO = "Avenida Ipanema, 165 &middot; Edifício Monte Carlo &middot; Empresarial 18 do Forte &middot; Barueri/SP &middot; 06472-002"
PERFIL_GOOGLE = "https://www.google.com/maps/place/?q=place_id:ChIJMy0aVngDz5QRdP8iKXaQ4cY"

def cta(conteudo, texto="Quero meu diagnóstico comercial"):
    url = ("https://diegovicente.com.br/?utm_source=grupotr3&utm_medium=organico"
           "&utm_campaign=institucional&utm_content=%s#agendar" % conteudo)
    return '<a class="cta" href="%s">%s <span class="arrow">&rarr;</span></a>' % (url, texto)

MENU = [
    ("/", "Início"),
    ("/assessoria-comercial-b2b/", "Assessoria comercial"),
    ("/imersao-de-vendas-sao-paulo/", "Imersão de vendas"),
    ("/treinamento-de-vendas-para-equipe/", "Treinamento"),
    ("/a-empresa/", "A empresa"),
]

def topo(atual):
    itens = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == atual else "", nome)
        for href, nome in MENU)
    return """<header class="topbar">
  <div class="wrap">
    <a href="/" aria-label="TR3 — Terras Raras Business, página inicial">%s</a>
    <nav class="nav">%s</nav>
  </div>
</header>""" % (LOGO, itens)

RODAPE = """<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        %s
        <p class="foot-tag">Assessoria comercial para empresas que querem vender sem depender do dono:
        processo, treino do time e acompanhamento com número.</p>
      </div>
      <div>
        <p class="foot-block">
          <strong>Empresa</strong>
          TERRAS RARAS BUSINESS PRODUTOS DIGITAIS LTDA<br>
          CNPJ 55.654.936/0001-28<br>
          TR3 — Terras Raras Business é a operação de assessoria comercial da empresa.
        </p>
        <p class="foot-block">
          <strong>Endereço</strong>
          %s
        </p>
        <p class="foot-block">
          <strong>Contato</strong>
          <a href="mailto:%s">%s</a><br>
          <a href="tel:+5562991397882">%s</a>
        </p>
        <p class="foot-block">
          <strong>Sócios</strong>
          Diego Vicente e Pablo Marçal, sócios do projeto.
          <!-- FOTO DOS SOCIOS: entra aqui quando o Diego enviar o arquivo -->
        </p>
      </div>
    </div>
    <div class="foot-legal">
      <span>&copy; 2026 Terras Raras Business Produtos Digitais LTDA. Todos os direitos reservados.</span>
      <span class="foot-links">
        <a href="%s">Avaliações no Google</a>
        <a href="https://diegovicente.com.br/">diegovicente.com.br</a>
        <a href="https://diegovicente.com.br/politica-de-privacidade/">Política de Privacidade</a>
        <a href="https://diegovicente.com.br/termos-de-uso/">Termos de Uso</a>
      </span>
    </div>
  </div>
</footer>""" % (LOGO_FOOT, ENDERECO, EMAIL, EMAIL, TEL, PERFIL_GOOGLE)

ORG_JSONLD = """{
  "@context":"https://schema.org",
  "@type":["Organization","LocalBusiness"],
  "name":"TR3 — Terras Raras Business",
  "alternateName":["Terras Raras Business - TR3","TR3 Assessoria Comercial"],
  "legalName":"TERRAS RARAS BUSINESS PRODUTOS DIGITAIS LTDA",
  "taxID":"55.654.936/0001-28",
  "url":"https://grupotr3.com.br/",
  "telephone":"+55 62 99139-7882",
  "email":"contato@diegovicente.com.br",
  "address":{"@type":"PostalAddress","streetAddress":"Avenida Ipanema, 165 — Edifício Monte Carlo",
    "addressLocality":"Barueri","addressRegion":"SP","postalCode":"06472-002","addressCountry":"BR"},
  "sameAs":["https://diegovicente.com.br/","%s"],
  "founder":{"@type":"Person","name":"Diego Vicente"},
  "description":"Assessoria comercial B2B: processo de vendas, treino de time comercial e acompanhamento com indicador. Realiza o MMV — Método Multiplicador de Vendas, imersão de vendas presencial em Alphaville, Barueri."
}""" % PERFIL_GOOGLE

def faq_jsonld(pares):
    itens = ",".join(
        '{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}'
        % (_j(p), _j(r)) for p, r in pares)
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[%s]}' % itens

def _j(t):
    import json
    return json.dumps(t, ensure_ascii=False)

def faq_html(pares):
    blocos = "".join(
        "<details><summary>%s</summary><p>%s</p></details>" % (p, r) for p, r in pares)
    return '<div class="faq">%s</div>' % blocos

def pagina(slug, title, descricao, corpo, jsonld_extra=None, canonical=None):
    canonical = canonical or (SITE + slug)
    extras = "".join('\n<script type="application/ld+json">%s</script>' % j for j in (jsonld_extra or []))
    html = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="TR3 — Terras Raras Business">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500;0,9..144,600;1,9..144,500&family=Archivo:wght@400;500;600&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">%s</script>%s
</head>
<body>
%s
%s
%s
</body>
</html>
""" % (title, descricao, canonical, title, descricao, canonical, ORG_JSONLD, extras,
       topo(slug), corpo, RODAPE)
    destino = RAIZ / (slug.strip("/") + "/index.html" if slug != "/" else "index.html")
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    return destino

print("base carregada")
