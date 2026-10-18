# -*- coding: utf-8 -*-
from build import pagina, cta, faq_html, faq_jsonld, RAIZ, SITE, PERFIL_GOOGLE
import json

def sec(eyebrow, h2, corpo, classe=""):
    return """<section class="%s">
  <div class="wrap">
    <p class="eyebrow">%s</p>
    <h2>%s</h2>
    %s
  </div>
</section>""" % (classe, eyebrow, h2, corpo)

def hero(eyebrow, h1, sub, body, botao, nota):
    return """<div class="hero">
  <div class="wrap">
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="hero-sub">%s</p>
    <p class="hero-body">%s</p>
    <p class="hero-actions">%s</p>
    <p class="cta-note">%s</p>
  </div>
</div>""" % (eyebrow, h1, sub, body, botao, nota)

NOTA = "Conversa de 1h30, gratuita, com especialista comercial e de marketing da TR3."

# ------------------------------------------------ ASSESSORIA COMERCIAL B2B
faq_a = [
    ("Qual a diferença entre assessoria e consultoria comercial?",
     "Consultoria entrega diagnóstico e relatório e vai embora. Assessoria fica: a gente monta o processo, treina o seu time e volta toda semana cobrar o número. Quem procura consultoria comercial normalmente quer o segundo — só não chama assim."),
    ("Quanto tempo dura o projeto?",
     "Depende do tamanho do time e de quanto da operação precisa ser reescrita. O diagnóstico define isso antes de qualquer proposta."),
    ("Vocês assumem o meu time?",
     "Não substituímos o seu gestor. A gente monta o processo, treina quem já está lá e cobra indicador junto com você. Se faltar gente, o modelo de recrutamento também entra no projeto."),
    ("Precisa ter CRM?",
     "Ajuda, mas não é pré-requisito. Parte do trabalho é justamente fazer o time usar o que a empresa já paga — CRM que ninguém preenche é o caso mais comum que a gente encontra."),
    ("E se eu já tiver feito consultoria antes e não funcionou?",
     "Na maioria das vezes o que faltou foi acompanhamento. Processo escrito que ninguém cobra vira PDF na gaveta. É por isso que a nossa entrega não termina na entrega."),
]
corpo_a = """<div class="lead">
  <p>Assessoria comercial não é palestra nem relatório. É entrar na sua operação, montar o processo que
  o seu time vai seguir todo dia e cobrar o número toda semana.</p>
</div>""" + sec("O que entra", "O que entra na assessoria comercial da TR3", """
    <ol class="steps">
      <li><h3>Diagnóstico do funil</h3><p>Com número: onde entra lead, onde ele para e quanto a empresa
        perde em cada etapa.</p></li>
      <li><h3>Playbook de vendas</h3><p>Escrito para o seu produto e para as suas objeções, não um modelo
        genérico.</p></li>
      <li><h3>Meta, cadência e rotina</h3><p>Quem liga, em quanto tempo, quantas vezes, e qual reunião de
        gestão sustenta isso.</p></li>
      <li><h3>Treino do time</h3><p>Seus vendedores praticam com as suas objeções reais.</p></li>
      <li><h3>Acompanhamento</h3><p>Reunião marcada, realizada, proposta, venda. Indicador por etapa,
        toda semana.</p></li>
    </ol>""", "band-2") + sec("Para quem", "Para quem é (e para quem não é)", """
    <div class="lead">
      <p><strong>É para</strong> empresa que já vende e quer previsibilidade: tem time comercial, fatura
      todo mês e sente que o resultado depende do dono.</p>
      <p><strong>Não é para</strong> quem quer curso gravado nem para quem procura modelo de playbook em
      PDF. Isso não muda o seu time.</p>
    </div>""") + sec("Prova", "Resultados de clientes", """
    <div class="cases">
      <div class="case"><p class="who">Edson</p><p class="num">R$ 5 milhões em cerca de um ano</p>
        <p>Imersão mais assessoria. Passou a negociar fora do Brasil.</p></div>
      <div class="case"><p class="who">André</p><p class="num">De 2 ou 3 vendas por mês para 18</p>
        <p>Organizou o time e o processo.</p></div>
      <div class="case"><p class="who">Juliano</p><p class="num">De 60 para 135 transportes por mês</p>
        <p>Mesmo time, mesma frota. Mudou a rotina comercial.</p></div>
    </div>""", "band") + sec("Dúvidas", "Perguntas frequentes sobre assessoria comercial B2B",
    faq_html(faq_a) + '<p style="margin-top:36px">%s</p>' % cta("assessoria-final"))

pagina("/assessoria-comercial-b2b/", "Assessoria Comercial B2B | TR3 — Diego Vicente",
       "Assessoria comercial B2B: processo, playbook, treino do time e acompanhamento com número. 2.500 times estruturados. Comece pelo diagnóstico gratuito.",
       "<main>" + hero("Assessoria comercial B2B",
         "Assessoria comercial B2B para empresas que querem parar de depender do dono",
         "2.500 times comerciais estruturados. R$ 500 milhões faturados pelos nossos clientes.",
         "A gente entra na sua operação, monta o processo que o seu time vai seguir todo dia e cobra o número toda semana.",
         cta("assessoria-topo"), NOTA) + corpo_a + "</main>",
       jsonld_extra=[faq_jsonld(faq_a)])

# ------------------------------------------------ IMERSAO
faq_i = [
    ("Onde acontece a imersão de vendas?",
     "Em Alphaville, Barueri, na Grande São Paulo. O endereço exato vai junto com a confirmação da inscrição."),
    ("Quanto custa o ingresso?",
     "R$ 997 por pessoa. Em dupla, R$ 1.497 — vale levar quem lidera o seu time."),
    ("Para quem é a imersão?",
     "Para dono de empresa e líder comercial que já vende e quer processo. Se você ainda vende sozinho, a imersão é o melhor ponto de partida."),
    ("É palestra motivacional?",
     "Não. São dois dias de implementação: você sai com o processo do seu comercial desenhado, não com frases de efeito."),
    ("Dá direito a algum acompanhamento depois?",
     "A imersão é o evento. O acompanhamento contínuo é a assessoria, e quem quiser conhece o formato durante os dois dias."),
]
corpo_i = sec("O que você leva", "O que você leva da imersão de vendas", """
    <ol class="steps">
      <li><h3>Atração</h3><p>Os canais de geração de demanda para encher o funil de oportunidade
        qualificada.</p></li>
      <li><h3>Conversão</h3><p>Processos, scripts e rotinas de negociação que elevam a taxa de
        conversão.</p></li>
      <li><h3>Performance</h3><p>Recrutamento, treinamento e gestão para o time bater meta.</p></li>
    </ol>""", "band-2") + """
<!-- ATUALIZAR A CADA TURMA -->
<section>
  <div class="wrap">
    <p class="eyebrow">Próxima turma</p>
    <h2>Próxima turma, data e local</h2>
    <div class="event">
      <p class="when">30 e 31 de outubro de 2026 &middot; Alphaville, Barueri/SP</p>
      <h3>MMV — Método Multiplicador de Vendas</h3>
      <p>Dois dias, presencial. Individual R$ 997, dupla R$ 1.497.</p>
      <p style="margin-top:26px">%s</p>
      <p class="cta-note">Vagas limitadas pelo tamanho da sala.</p>
    </div>
  </div>
</section>""" % cta("imersao-turma", "Quero minha vaga no MMV") + sec("Quem vai",
    "Para quem é a imersão", """<div class="lead">
      <p>Empresário que busca tração comercial e previsibilidade. Mais de 2.000 empresas já passaram
      pelo método.</p></div>""") + sec("Turmas anteriores",
    "O que aconteceu nas turmas anteriores", """
    <div class="cases">
      <div class="case"><p class="who">Cassius</p><p class="num">R$ 127 mil fechados no intervalo</p>
        <p>Aplicou a abordagem no segundo dia e fechou antes de a imersão acabar.</p></div>
      <div class="case"><p class="who">Thiago</p><p class="num">Estava quase fechando a empresa</p>
        <p>Hoje continua com a gente.</p></div>
      <div class="case"><p class="who">Edson</p><p class="num">R$ 5 milhões em cerca de um ano</p>
        <p>Imersão mais assessoria.</p></div>
    </div>""", "band") + sec("Dúvidas", "Perguntas frequentes sobre a imersão de vendas",
    faq_html(faq_i) + '<p style="margin-top:36px">%s</p>' % cta("imersao-final", "Quero minha vaga no MMV"))

pagina("/imersao-de-vendas-sao-paulo/", "Imersão de Vendas em São Paulo | MMV — TR3",
       "Imersão de vendas presencial em Alphaville, São Paulo: 2 dias para montar o processo do seu comercial. Próxima turma 30 e 31 de outubro de 2026.",
       "<main>" + hero("MMV — Método Multiplicador de Vendas",
         "Imersão de vendas presencial em São Paulo: 2 dias para montar o processo do seu comercial",
         "MMV — Método Multiplicador de Vendas. Mais de 2.000 empresas já passaram.",
         "Dois dias em Alphaville, Barueri, na Grande São Paulo. Você entra com o seu comercial do jeito que ele está e sai com o processo desenhado: quem faz o quê, em quanto tempo, com qual meta.",
         cta("imersao-topo", "Quero minha vaga no MMV"), "Ingresso individual R$ 997. Em dupla, R$ 1.497.") + corpo_i + "</main>",
       jsonld_extra=[faq_jsonld(faq_i)])

# ------------------------------------------------ TREINAMENTO
faq_t = [
    ("O treinamento é na minha empresa ou na de vocês?",
     "Funciona dos dois jeitos: presencial em Alphaville ou dentro da sua empresa, com o seu time."),
    ("Quantas pessoas precisam participar?",
     "Funciona a partir de um vendedor além do dono. Time pequeno costuma ganhar mais rápido, porque a rotina muda no dia seguinte."),
    ("Vocês treinam com o nosso produto?",
     "Sim. O treino usa o seu produto, o seu preço e as objeções que o seu cliente realmente faz."),
    ("Qual a diferença para a imersão MMV?",
     "A imersão é para o dono desenhar o processo da empresa. O treinamento é para o time executar esse processo no dia a dia."),
]
corpo_t = sec("Como funciona", "Como funciona o treinamento de vendas para equipe", """
    <ol class="steps">
      <li><h3>Levantamento</h3><p>A gente ouve ligação e reunião do seu time antes de treinar qualquer
        coisa.</p></li>
      <li><h3>Treino prático</h3><p>Abordagem, pergunta e objeção da sua operação, treinadas na
        prática.</p></li>
      <li><h3>Material de consulta</h3><p>O que foi combinado fica escrito, para o time consultar depois
        — e para o próximo contratado aprender sem recomeçar do zero.</p></li>
      <li><h3>Rotina</h3><p>Treino vira cadência semanal, não evento de sexta-feira.</p></li>
    </ol>""", "band-2") + sec("Formatos", "Treinamento presencial ou na sua empresa", """
    <div class="lead"><p>Presencial em Alphaville, na sua empresa ou on-line, conforme onde o seu time
      está. O conteúdo é o mesmo; o que muda é a logística.</p></div>""") + sec("Estrutura",
    "Como estruturar um time de vendas que não depende do dono", """
    <div class="lead">
      <p>Estruturar time comercial é definir quatro coisas: para qual etapa do funil você contrata
      (pré-vendedor, closer, pós-venda), como remunera, qual a rotina de gestão da semana e quais
      indicadores você lê.</p>
      <p>Sem essas quatro, técnica de vendas não para em pé: script que ninguém segue, CRM que ninguém
      preenche, meta que vira surpresa no fim do mês.</p>
    </div>""", "band") + sec("Dúvidas", "Perguntas frequentes sobre treinamento de vendas",
    faq_html(faq_t) + '<p style="margin-top:36px">%s</p>' % cta("treinamento-final"))

pagina("/treinamento-de-vendas-para-equipe/", "Treinamento de Vendas para Equipe | TR3",
       "Treinamento de vendas para equipe com o seu produto e as suas objeções, presencial ou na sua empresa. Treinamento é evento, treino é rotina.",
       "<main>" + hero("Treinamento de vendas",
         "Treinamento de vendas para equipe, com o seu produto e as suas objeções",
         "Treinamento é evento. Treino é rotina. A gente entrega as duas coisas.",
         "A maior parte do treinamento de vendas não muda nada porque acaba na sexta-feira. O nosso treino vira rotina: o time pratica a abordagem, a pergunta e a objeção que aparecem na sua operação, e depois tem onde consultar o que foi combinado.",
         cta("treinamento-topo"), NOTA) + corpo_t + "</main>",
       jsonld_extra=[faq_jsonld(faq_t)])

# ------------------------------------------------ A EMPRESA
corpo_e = sec("O que fazemos", "O que a TR3 faz", """
    <div class="lead">
      <p>A TR3 — Terras Raras Business é a operação de assessoria comercial e treinamento de
      <strong>Diego Vicente</strong>. A empresa implanta processo de vendas, treina times comerciais e
      acompanha indicador dentro da operação do cliente.</p>
      <p>Realiza o MMV — Método Multiplicador de Vendas, imersão presencial de dois dias em Alphaville,
      e o Playbook Times de Elite, material digital com os processos de recrutamento, remuneração,
      rotina de gestão e indicadores.</p>
    </div>""") + sec("Dados", "Dados da empresa", """
    <div class="lead">
      <p><strong>Razão social:</strong> TERRAS RARAS BUSINESS PRODUTOS DIGITAIS LTDA<br>
      <strong>Nome de mercado:</strong> TR3 — Terras Raras Business<br>
      <strong>CNPJ:</strong> 55.654.936/0001-28<br>
      <strong>Situação cadastral:</strong> ativa</p>
    </div>""", "band-2") + sec("Onde estamos", "Onde estamos", """
    <div class="lead">
      <p>Avenida Ipanema, 165 — Edifício Monte Carlo<br>
      Empresarial 18 do Forte — Barueri/SP — CEP 06472-002</p>
      <p><a class="linkgold" href="%s" rel="noopener">Ver no Google, com as 141 avaliações</a></p>
    </div>""" % PERFIL_GOOGLE, "band") + sec("Contato", "Contato", """
    <div class="lead">
      <p><a class="linkgold" href="mailto:contato@diegovicente.com.br">contato@diegovicente.com.br</a><br>
      <a class="linkgold" href="tel:+5562991397882">(62) 99139-7882</a></p>
      <p>Site pessoal do fundador: <a class="linkgold" href="https://diegovicente.com.br/">diegovicente.com.br</a></p>
    </div>""")

pagina("/a-empresa/", "A TR3 — Terras Raras Business | CNPJ e endereço",
       "TR3 — Terras Raras Business, assessoria comercial em Barueri/SP. Razão social, CNPJ, endereço e contato.",
       """<main><div class="hero"><div class="wrap">
         <p class="eyebrow">A empresa</p>
         <h1>A TR3 — Terras Raras Business</h1>
         <p class="hero-sub">Assessoria comercial, treinamento de times e imersão de vendas, em Barueri/SP.</p>
       </div></div>""" + corpo_e + "</main>")

# ------------------------------------------------ arquivos tecnicos
paginas = ["/", "/assessoria-comercial-b2b/", "/imersao-de-vendas-sao-paulo/",
           "/treinamento-de-vendas-para-equipe/", "/a-empresa/"]
urls = "".join('  <url><loc>%s%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>\n'
               % (SITE, p, "1.0" if p == "/" else "0.8") for p in paginas)
(RAIZ / "sitemap.xml").write_text(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls,
    encoding="utf-8")
(RAIZ / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE, encoding="utf-8")
(RAIZ / "CNAME").write_text("grupotr3.com.br\n", encoding="utf-8")
(RAIZ / ".nojekyll").write_text("", encoding="utf-8")
print("internas + sitemap ok")
