import feedparser
import datetime
import pytz
import html
import os
import urllib.request

BR = pytz.timezone("America/Sao_Paulo")
agora = datetime.datetime.now(BR)

# User-Agent de browser real para desbloquear feeds que rejeitam bots
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

def parse_feed(url):
    """Faz parse do feed com User-Agent de browser."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml,application/xml,text/xml,*/*"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read()
        feed = feedparser.parse(content)
        return feed
    except Exception:
        return feedparser.FeedParserDict(entries=[])

FEEDS = {
    "Valor": [
        "https://valor.globo.com/rss/",
        "https://valor.globo.com/ultimas-noticias/rss/",
        "https://www.valor.com.br/rss",
    ],
    "Folha": [
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
        "https://feeds.folha.uol.com.br/poder/rss091.xml",
        "https://feeds.folha.uol.com.br/mercado/rss091.xml",
    ],
    "Globo": [
        "https://g1.globo.com/rss/g1/",
        "https://g1.globo.com/rss/g1/economia/noticia/rss.xml",
        "https://oglobo.globo.com/rss.xml",
    ],
    "Estadao": [
        "https://www.estadao.com.br/rss/ultimas.xml",
        "https://politica.estadao.com.br/rss/ultimas",
        "https://economia.estadao.com.br/rss/ultimas",
    ],
    "CNN Brasil": [
        "https://www.cnnbrasil.com.br/feed/",
    ],
    "Metropoles": [
        "https://www.metropoles.com/feed",
    ],
    "UOL": [
        "https://noticias.uol.com.br/ultnot/reuters/index.xml",
        "https://rss.uol.com.br/feed/noticias.xml",
    ],
    "BrazilJournal": [
        "https://braziljournal.com/feed",
    ],
}

LIMITE_HORAS = 12
noticias = []

for veiculo, urls in FEEDS.items():
    coletado = False
    for url in urls:
        if coletado:
            break
        try:
            feed = parse_feed(url)
            entradas = []
            for entry in feed.entries[:30]:
                titulo = html.escape(entry.get("title", "").strip())
                link = entry.get("link", "#")
                pub = entry.get("published_parsed") or entry.get("updated_parsed")
                if pub:
                    dt = datetime.datetime(*pub[:6], tzinfo=pytz.utc).astimezone(BR)
                    diff = agora - dt
                    if diff.total_seconds() > LIMITE_HORAS * 3600:
                        continue
                    hora_str = dt.strftime("%d/%m %H:%M")
                else:
                    hora_str = ""
                if titulo and link:
                    entradas.append({
                        "veiculo": veiculo,
                        "titulo": titulo,
                        "link": link,
                        "hora": hora_str,
                        "dt": pub or (0,),
                    })
            if entradas:
                noticias.extend(entradas)
                coletado = True
                print(f"OK: {veiculo} via {url} ({len(entradas)} noticias)")
        except Exception as e:
            print(f"ERRO: {veiculo} via {url}: {e}")
            continue
    if not coletado:
        print(f"FALHOU: {veiculo} - nenhum feed funcionou")

noticias.sort(key=lambda x: x["dt"], reverse=True)

vistos = set()
noticias_unicas = []
for n in noticias:
    if n["titulo"] not in vistos:
        vistos.add(n["titulo"])
        noticias_unicas.append(n)

veiculos_presentes = [v for v in FEEDS.keys() if any(n["veiculo"] == v for n in noticias_unicas)]

def montar_itens(lst):
    if not lst:
        return "<li>Nenhuma noticia encontrada.</li>"
    linhas = []
    for n in lst:
        hora = f'<span class="hora">{n["hora"]}</span>' if n["hora"] else ""
        linhas.append(
            f'<li data-veiculo="{n["veiculo"]}" data-titulo="{n["titulo"].lower()}">'
            f'<strong>[{html.escape(n["veiculo"])}]</strong> '
            f'<a href="{n["link"]}" target="_blank">{n["titulo"]}</a> '
            f'{hora}</li>'
        )
    return "\n".join(linhas)

itens_html = montar_itens(noticias_unicas)
botoes = '<button class="filtro ativo" onclick="filtrarVeiculo(this, \'Todos\')">Todos</button>\n'
for v in veiculos_presentes:
    botoes += f'<button class="filtro" onclick="filtrarVeiculo(this, \'{v}\')">{v}</button>\n'

total = len(noticias_unicas)
hora_atualizacao = agora.strftime("%d/%m %H:%M")

HTML = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Clipping de Noticias</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: Arial, sans-serif; background: #fff8f6; color: #222; margin: 40px; line-height: 1.7; }}
  h1 {{ font-size: 1.6em; margin-bottom: 4px; }}
  .meta {{ color: #888; font-size: 0.9em; margin-bottom: 16px; display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }}
  .btn-atualizar {{
    background: #fff; border: 1px solid #ccc; border-radius: 20px;
    padding: 4px 14px; font-size: 0.85em; cursor: pointer;
    display: inline-flex; align-items: center; gap: 5px;
    transition: all 0.15s; color: #444;
  }}
  .btn-atualizar:hover {{ background: #f0f0f0; border-color: #999; }}
  .btn-atualizar.girando svg {{ animation: girar 0.8s linear infinite; }}
  @keyframes girar {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
  .filtros {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; align-items: center; }}
  .filtro {{ background: #fff; border: 1px solid #ccc; border-radius: 20px; padding: 5px 14px; font-size: 0.85em; cursor: pointer; transition: all 0.15s; }}
  .filtro:hover {{ background: #f0e8e5; }}
  .filtro.ativo {{ background: #333; color: #fff; border-color: #333; }}
  ul {{ list-style: disc; padding-left: 20px; }}
  li {{ margin-bottom: 6px; font-size: 0.95em; }}
  a {{ color: #1a0dab; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
  .hora {{ color: #999; font-size: 0.82em; margin-left: 4px; }}
  strong {{ color: #444; }}
  .total {{ color: #888; font-size: 0.85em; margin-bottom: 10px; }}
  .gear-btn {{ background: none; border: none; cursor: pointer; font-size: 1.3em; padding: 4px 8px; border-radius: 50%; transition: transform 0.3s; color: #666; line-height: 1; }}
  .gear-btn:hover {{ transform: rotate(45deg); color: #333; }}
  .kw-panel {{ display: none; background: #fff; border: 1px solid #ddd; border-radius: 10px; padding: 16px; margin-bottom: 20px; max-width: 500px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
  .kw-panel.aberto {{ display: block; }}
  .kw-panel h3 {{ font-size: 0.95em; margin-bottom: 10px; color: #444; }}
  .kw-input-row {{ display: flex; gap: 8px; margin-bottom: 10px; }}
  .kw-input {{ flex: 1; padding: 6px 10px; border: 1px solid #ccc; border-radius: 20px; font-size: 0.9em; outline: none; }}
  .kw-input:focus {{ border-color: #999; }}
  .kw-add-btn {{ background: #333; color: #fff; border: none; border-radius: 20px; padding: 6px 14px; font-size: 0.85em; cursor: pointer; }}
  .kw-add-btn:hover {{ background: #555; }}
  .kw-tags {{ display: flex; flex-wrap: wrap; gap: 6px; }}
  .kw-tag {{ background: #f0e8e5; border: 1px solid #e0c8c0; border-radius: 20px; padding: 3px 10px; font-size: 0.82em; display: flex; align-items: center; gap: 5px; }}
  .kw-tag .remove {{ cursor: pointer; color: #999; font-size: 1em; }}
  .kw-tag .remove:hover {{ color: #c00; }}
  .kw-hint {{ font-size: 0.8em; color: #aaa; margin-top: 8px; }}
  .kw-active-badge {{ background: #e8f4e8; border: 1px solid #b0d9b0; color: #2a7a2a; border-radius: 20px; padding: 3px 10px; font-size: 0.8em; }}
</style>
</head>
<body>
<h1>Noticias Brasil - Filtradas</h1>
<div class="meta">
  <span>Atualizado em <strong id="hora-label">{hora_atualizacao}</strong> | {total} noticias (ultimas {LIMITE_HORAS}h)</span>
  <button class="btn-atualizar" onclick="recarregar(this)" title="Buscar atualizacoes">
    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <polyline points="1 4 1 10 7 10"></polyline>
      <path d="M3.51 15a9 9 0 1 0 .49-4.36"></path>
    </svg>
    Atualizar
  </button>
</div>

<div class="filtros">
{botoes}
  <button class="gear-btn" onclick="togglePainel(this)" title="Filtrar por palavras-chave">&#9881;</button>
  <span id="kw-badge" class="kw-active-badge" style="display:none"></span>
</div>

<div class="kw-panel" id="kwPanel">
  <h3>&#128269; Filtrar por palavras-chave</h3>
  <div class="kw-input-row">
    <input class="kw-input" id="kwInput" type="text" placeholder="Ex: Lula, dolar, STF..." onkeydown="if(event.key==='Enter') adicionarKw()">
    <button class="kw-add-btn" onclick="adicionarKw()">Adicionar</button>
  </div>
  <div class="kw-tags" id="kwTags"></div>
  <p class="kw-hint">So aparecem noticias com pelo menos uma das palavras. Deixe vazio para ver tudo.</p>
</div>

<p class="total" id="contagem">{total} noticias exibidas</p>

<ul id="lista">
{itens_html}
</ul>

<script>
let veiculoAtivo = 'Todos';
let keywords = JSON.parse(localStorage.getItem('clipping_kw') || '[]');

function salvarKw() {{ localStorage.setItem('clipping_kw', JSON.stringify(keywords)); }}

function renderTags() {{
  const container = document.getElementById('kwTags');
  container.innerHTML = keywords.map((kw, i) =>
    `<span class="kw-tag">${{kw}}<span class="remove" onclick="removerKw(${{i}})">&#10005;</span></span>`
  ).join('');
  const badge = document.getElementById('kw-badge');
  if (keywords.length > 0) {{
    badge.style.display = '';
    badge.textContent = keywords.length === 1 ? '1 palavra-chave ativa' : keywords.length + ' palavras-chave ativas';
  }} else {{
    badge.style.display = 'none';
  }}
}}

function adicionarKw() {{
  const input = document.getElementById('kwInput');
  const val = input.value.trim().toLowerCase();
  if (val && !keywords.includes(val)) {{
    keywords.push(val);
    salvarKw();
    renderTags();
    aplicarFiltros();
  }}
  input.value = '';
  input.focus();
}}

function removerKw(i) {{
  keywords.splice(i, 1);
  salvarKw();
  renderTags();
  aplicarFiltros();
}}

function togglePainel(btn) {{
  const painel = document.getElementById('kwPanel');
  painel.classList.toggle('aberto');
  btn.style.transform = painel.classList.contains('aberto') ? 'rotate(90deg)' : '';
}}

function filtrarVeiculo(btn, veiculo) {{
  document.querySelectorAll('.filtro').forEach(b => b.classList.remove('ativo'));
  btn.classList.add('ativo');
  veiculoAtivo = veiculo;
  aplicarFiltros();
}}

function aplicarFiltros() {{
  const itens = document.querySelectorAll('#lista li');
  let count = 0;
  itens.forEach(li => {{
    const okVeiculo = veiculoAtivo === 'Todos' || li.dataset.veiculo === veiculoAtivo;
    const titulo = li.dataset.titulo || '';
    const okKw = keywords.length === 0 || keywords.some(kw => titulo.includes(kw));
    const mostrar = okVeiculo && okKw;
    li.style.display = mostrar ? '' : 'none';
    if (mostrar) count++;
  }});
  document.getElementById('contagem').textContent = count + ' noticias exibidas';
}}

function recarregar(btn) {{
  btn.classList.add('girando');
  btn.disabled = true;
  const url = location.href.split('?')[0] + '?t=' + Date.now();
  location.replace(url);
}}

renderTags();
aplicarFiltros();
</script>
</body>
</html>"""

import os
output_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"Clipping gerado: {total} noticias - {hora_atualizacao}")
