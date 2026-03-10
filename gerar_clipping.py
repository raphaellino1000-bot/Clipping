import feedparser
import datetime
import pytz
import html
import os

# Fuso horario de Brasilia
BR = pytz.timezone("America/Sao_Paulo")
agora = datetime.datetime.now(BR)

# Feeds RSS dos veiculos
FEEDS = {
    "Valor": [
        "https://valor.globo.com/rss/valor-economico",
        "https://www.valor.com.br/rss",
    ],
    "Folha": [
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
        "https://feeds.folha.uol.com.br/poder/rss091.xml",
        "https://feeds.folha.uol.com.br/mercado/rss091.xml",
    ],
    "Globo": [
        "https://oglobo.globo.com/rss.xml",
        "https://g1.globo.com/rss/g1/",
    ],
    "Estadao": [
        "https://www.estadao.com.br/rss/ultimas.xml",
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
    for url in urls:
        try:
            feed = feedparser.parse(url)
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
                    noticias.append({
                        "veiculo": veiculo,
                        "titulo": titulo,
                        "link": link,
                        "hora": hora_str,
                        "dt": pub or (0,),
                    })
            break
        except Exception:
            continue

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
            f'<li data-veiculo="{n["veiculo"]}">'
            f'<strong>[{html.escape(n["veiculo"])}]</strong> '
            f'<a href="{n["link"]}" target="_blank">{n["titulo"]}</a> '
            f'{hora}</li>'
        )
    return "\n".join(linhas)

itens_html = montar_itens(noticias_unicas)
botoes = '<button class="filtro ativo" onclick="filtrar(this, \'Todos\')">Todos</button>\n'
for v in veiculos_presentes:
    botoes += f'<button class="filtro" onclick="filtrar(this, \'{v}\')">{v}</button>\n'

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
  .meta {{ color: #888; font-size: 0.9em; margin-bottom: 20px; }}
  .filtros {{ display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 24px; }}
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
</style>
</head>
<body>
<h1>Noticias Brasil - Filtradas</h1>
<div class="meta">Atualizado em {hora_atualizacao} | {total} noticias (ultimas {LIMITE_HORAS}h)</div>
<div class="filtros">
{botoes}
</div>
<p class="total" id="contagem">{total} noticias exibidas</p>
<ul id="lista">
{itens_html}
</ul>
<script>
function filtrar(btn, veiculo) {{
  document.querySelectorAll('.filtro').forEach(b => b.classList.remove('ativo'));
  btn.classList.add('ativo');
  const itens = document.querySelectorAll('#lista li');
  let count = 0;
  itens.forEach(li => {{
    const mostrar = veiculo === 'Todos' || li.dataset.veiculo === veiculo;
    li.style.display = mostrar ? '' : 'none';
    if (mostrar) count++;
  }});
  document.getElementById('contagem').textContent = count + ' noticias exibidas';
}}
</script>
</body>
</html>"""

import os
output_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(HTML)

print(f"Clipping gerado: {total} noticias - {hora_atualizacao}")
