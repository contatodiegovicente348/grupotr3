# grupotr3.com.br — site institucional da TR3

Site estático da TR3 — Terras Raras Business, publicado por GitHub Pages no domínio grupotr3.com.br.

- Copy e estrutura: `napoleao/docs/SITE-TR3-ESTRUTURA.md` na sede (Napoleão, 17/10/2026).
- Decisões e pendências: `docs/projetos/site-tr3.md` na sede.
- As páginas são geradas: edite `build.py` (base, topo, rodapé), `paginas.py` (home) e
  `internas.py` (demais páginas), depois rode `python3 paginas.py && python3 internas.py`.
- Não edite os `index.html` à mão: eles são sobrescritos na próxima geração.

Conversão: todos os botões apontam para o formulário de diagnóstico de diegovicente.com.br, que já
grava no Clint (origem MMV, etapa Base, tag "diagnostico site Diego"), com UTM por página e seção.
