# -*- coding: utf-8 -*-
from build import pagina, cta, faq_html, faq_jsonld, RAIZ, SITE, PERFIL_GOOGLE, ENDERECO
import json

MMV_CTA = cta("home-mmv-out26", "Quero minha vaga no MMV")

# ---------------------------------------------------------------- HOME
faq_home = [
    ("A TR3 atende empresas de qualquer tamanho?",
     "A gente trabalha melhor com empresa que já vende e quer previsibilidade: tem time comercial, ou pelo menos um vendedor além do dono. Se você ainda vende sozinho, a imersão resolve mais que a assessoria."),
    ("Vocês fazem consultoria comercial?",
     "O que a TR3 faz é assessoria comercial, que é diferente de consultoria. Consultoria entrega diagnóstico e relatório e vai embora. Assessoria fica: a gente monta o processo, treina o seu time e volta toda semana cobrar o número. O diagnóstico é só a porta de entrada."),
    ("Quanto custa?",
     "A imersão MMV tem preço público: R$ 997 por pessoa. A assessoria é orçada depois do diagnóstico, porque depende do tamanho do time e do tempo de acompanhamento. O diagnóstico é gratuito e não tem compromisso."),
    ("Em quanto tempo eu vejo resultado?",
     "Processo e treino começam a mudar a rotina do time nas primeiras semanas. No evento já teve cliente fechando contrato no intervalo. Mas número de verdade é o que se sustenta por três meses, e é isso que a gente acompanha."),
    ("É presencial ou on-line?",
     "A imersão é presencial em Alphaville. A assessoria e o treinamento do time funcionam nos dois formatos, inclusive dentro da sua empresa."),
    ("Vocês atendem fora de São Paulo?",
     "Sim. A imersão acontece em Alphaville e recebe empresário de todo o Brasil; assessoria e treinamento são feitos onde o seu time está."),
    ("Quem atende: o Diego ou o time?",
     "O diagnóstico é com um especialista comercial e de marketing da TR3. O Diego conduz a imersão e participa dos projetos de assessoria."),
]

evento_jsonld = json.dumps({
    "@context": "https://schema.org", "@type": "Event",
    "name": "MMV — Método Multiplicador de Vendas",
    "description": "Imersão de vendas presencial de dois dias em Alphaville, Barueri/SP.",
    "startDate": "2026-10-30T09:00-03:00", "endDate": "2026-10-31T19:00-03:00",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "eventStatus": "https://schema.org/EventScheduled",
    "location": {"@type": "Place", "name": "Alphaville, Barueri",
                 "address": {"@type": "PostalAddress", "addressLocality": "Barueri",
                             "addressRegion": "SP", "addressCountry": "BR"}},
    "organizer": {"@type": "Organization", "name": "TR3 — Terras Raras Business",
                  "url": "https://grupotr3.com.br/"},
    "offers": {"@type": "Offer", "price": "997", "priceCurrency": "BRL",
               "availability": "https://schema.org/InStock", "url": "https://grupotr3.com.br/imersao-de-vendas-sao-paulo/"},
}, ensure_ascii=False)

home = """<main>
<div class="hero">
  <div class="wrap">
    <p class="eyebrow">TR3 — Terras Raras Business</p>
    <h1>Assessoria comercial B2B que estrutura o time de vendas da sua empresa</h1>
    <p class="hero-sub">A TR3 já estruturou <strong>2.500 times comerciais</strong>. Os clientes somam
      <strong>R$ 500 milhões</strong> faturados.</p>
    <p class="hero-body">Se a sua empresa vende, mas só vende quando você entra na reunião, o problema
      não é o produto nem o mercado. É o processo. A gente entra no seu comercial, monta o processo,
      treina o seu time e acompanha até o número subir.</p>
    <p class="hero-actions">%s</p>
    <p class="cta-note">Conversa de 1h30, gratuita, com especialista comercial e de marketing da TR3.</p>
  </div>
</div>

<div class="marks">
  <div class="mark"><div class="fig">2.500</div><p>times comerciais estruturados</p></div>
  <div class="mark"><div class="fig">R$ 500 mi</div><p>faturados pelos nossos clientes</p></div>
  <div class="mark"><div class="fig">141</div><p>avaliações no Google, nota 5,0</p></div>
  <div class="mark"><div class="fig">25 anos</div><p>dentro de operação comercial</p></div>
</div>

<section>
  <div class="wrap">
    <p class="eyebrow">O diagnóstico começa aqui</p>
    <h2>Como estruturar um time de vendas que não depende do dono</h2>
    <p class="lead-muted">Quase sempre a empresa que nos procura tem os mesmos três sinais:</p>
    <ul class="signs">
      <li>Proposta enviada há seis meses que ninguém mais tocou.</li>
      <li>Vendedor que bate meta no mês que o dono acompanha e não bate no mês seguinte.</li>
      <li>Lead que chega, entra na planilha e fica lá, porque ninguém ligou no mesmo dia.</li>
    </ul>
    <p class="verdict">Nenhum desses três se resolve com palestra de motivação. Treinamento é evento.
      <em>Treino é rotina.</em></p>
  </div>
</section>

<section class="band-2">
  <div class="wrap">
    <p class="eyebrow">O mecanismo</p>
    <h2>O que a TR3 faz dentro do seu comercial</h2>
    <ol class="steps">
      <li><h3>Diagnóstico</h3><p>A gente olha a sua carteira, o seu funil e as suas últimas vendas
        perdidas e mostra onde o dinheiro está vazando, com número.</p></li>
      <li><h3>Processo</h3><p>Playbook de vendas feito para a sua empresa: quem faz a primeira ligação,
        em quanto tempo, o que pergunta, o que manda depois, quando desiste.</p></li>
      <li><h3>Treino do time</h3><p>Seus vendedores treinam o processo com a gente, na prática, com as
        suas objeções reais — não com exemplo de livro.</p></li>
      <li><h3>Acompanhamento</h3><p>A gente volta e cobra o número. Reunião marcada, reunião realizada,
        proposta, venda. O que não é medido não melhora.</p></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Três caminhos</p>
    <h2>Assessoria, imersão ou treinamento do time</h2>
    <div class="paths">
      <div class="path">
        <h3>Assessoria comercial B2B</h3>
        <p>A gente assume o projeto do seu comercial junto com você: processo, time, metas e
          acompanhamento. Para quem quer parar de depender do dono para vender.</p>
        <a class="linkgold" href="/assessoria-comercial-b2b/">Ver como funciona a assessoria</a>
      </div>
      <div class="path">
        <h3>MMV — Imersão de vendas presencial em São Paulo</h3>
        <p>Dois dias em Alphaville, Barueri, com o Diego Vicente e o nosso time. Você sai com o processo
          de vendas da sua empresa desenhado.</p>
        <a class="linkgold" href="/imersao-de-vendas-sao-paulo/">Ver a próxima turma</a>
      </div>
      <div class="path">
        <h3>Treinamento de vendas para equipe</h3>
        <p>Treino do seu time comercial, com o seu produto e as suas objeções. Presencial ou na sua
          empresa.</p>
        <a class="linkgold" href="/treinamento-de-vendas-para-equipe/">Ver o treinamento para equipe</a>
      </div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Prova</p>
    <h2>Resultados de clientes da TR3</h2>
    <p class="lead-muted">Nome, número e o que mudou. Todos autorizaram a publicação.</p>
    <div class="cases">
      <div class="case">
        <p class="who">Cassius</p>
        <p class="num">Contrato de R$ 127 mil fechado no intervalo do evento</p>
        <p>Aplicou a abordagem no segundo dia do MMV, ligou no intervalo e fechou antes de a imersão
          acabar.</p>
      </div>
      <div class="case">
        <p class="who">Edson</p>
        <p class="num">R$ 5 milhões de faturamento em cerca de um ano</p>
        <p>Imersão mais assessoria. Além do faturamento do produto, passou a negociar fora do Brasil.</p>
      </div>
      <div class="case">
        <p class="who">André</p>
        <p class="num">De 2 ou 3 vendas por mês para 18</p>
        <p>Pensava em desistir do negócio. Organizou o time e o processo, e o número mudou de patamar.</p>
      </div>
      <div class="case">
        <p class="who">Juliano</p>
        <p class="num">De 60 para 135 transportes por mês</p>
        <p>Mesmo time, mesma frota. Mudou a rotina comercial.</p>
      </div>
      <div class="case">
        <p class="who">Thiago</p>
        <p class="num">Estava quase fechando a empresa</p>
        <p>Hoje continua com a gente.</p>
      </div>
    </div>
    <p class="lead">Quer saber qual desses números é possível no seu comercial? É isso que o
      diagnóstico responde.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Reputação</p>
    <h2>141 avaliações no Google, nota 5,0</h2>
    <p class="lead">A gente não pede que você acredite na nossa palavra. O perfil da TR3 no Google tem
      141 avaliações de quem já passou por aqui, com nota 5,0. Dá para ler todas antes de falar com a
      gente.</p>
    <p style="margin-top:22px"><a class="linkgold" href="%s" rel="noopener">Ver as avaliações no Google</a></p>
  </div>
</section>

<section class="band-2">
  <div class="wrap">
    <p class="eyebrow">Quem está por trás</p>
    <h2>Quem está por trás da TR3</h2>
    <div class="lead">
      <p>A TR3 (Terras Raras Business) é a empresa de assessoria comercial do <strong>Diego
        Vicente</strong>.</p>
      <p>São 25 anos dentro de operação comercial. Ele pegou uma indústria com R$ 6 milhões de prejuízo,
        transformou o comercial em máquina previsível e a empresa foi vendida por milhões. Depois criou
        o MMV — Método Multiplicador de Vendas, por onde já passaram mais de 2.000 empresas.</p>
      <p>Hoje o time da TR3 faz isso dentro da empresa dos clientes: processo, treino e acompanhamento,
        até o número subir.</p>
    </div>
    <div class="people">
      <div class="person">
        <p class="role">Sócio</p>
        <h3>Diego Vicente</h3>
        <p>Criador do MMV. Conduz as imersões e participa dos projetos de assessoria.</p>
      </div>
      <div class="person">
        <p class="role">Sócio</p>
        <h3>Pablo Marçal</h3>
        <p>Sócio do projeto.</p>
      </div>
    </div>
  </div>
</section>

<!-- ATUALIZAR A CADA TURMA -->
<section>
  <div class="wrap">
    <p class="eyebrow">Próxima turma</p>
    <h2>Próxima imersão de vendas presencial: 30 e 31 de outubro de 2026, em Alphaville</h2>
    <div class="event">
      <p class="when">30 e 31 de outubro de 2026 &middot; Alphaville, Barueri/SP</p>
      <h3>Dois dias para desenhar o processo do seu comercial</h3>
      <p>Você entra com o seu comercial do jeito que ele está e sai com o processo desenhado: quem faz o
        quê, em quanto tempo e com qual meta.</p>
      <p>Ingresso individual R$ 997. Em dupla, R$ 1.497 — vale levar quem lidera o seu time.</p>
      <p style="margin-top:26px">%s</p>
      <p class="cta-note">Vagas limitadas pelo tamanho da sala.</p>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <p class="eyebrow">Dúvidas</p>
    <h2>Perguntas frequentes sobre assessoria comercial</h2>
    %s
  </div>
</section>

<section>
  <div class="wrap">
    <p class="eyebrow">Último passo</p>
    <h2>Quer saber onde o seu comercial está vazando?</h2>
    <p class="lead">Em 1h30 a gente olha o seu funil, as suas últimas vendas perdidas e te mostra onde
      está o dinheiro que já está dentro de casa. Se fizer sentido trabalharmos juntos, a gente fala
      disso no fim. Se não fizer, você sai com o diagnóstico de graça.</p>
    <p style="margin-top:32px">%s</p>
  </div>
</section>
</main>""" % (cta("home-topo"), PERFIL_GOOGLE, MMV_CTA, faq_html(faq_home), cta("home-final"))

pagina("/", "TR3 | Assessoria Comercial B2B e Imersão de Vendas",
       "Assessoria comercial B2B e imersão de vendas presencial. A TR3 já estruturou 2.500 times comerciais. Diagnóstico gratuito de 1h30 com especialista.",
       home, jsonld_extra=[faq_jsonld(faq_home), evento_jsonld])
print("home ok")
