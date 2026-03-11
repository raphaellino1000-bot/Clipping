import feedparser
import datetime
import pytz
import html
import os


BR = pytz.timezone("America/Sao_Paulo")
agora = datetime.datetime.now(BR)


# URLs testadas e confirmadas como funcionais
FEEDS = {
    "Valor": [
        "https://pox.globo.com/rss/valor/",           # funciona
        "https://www.valor.com.br/rss",               # fallback
    ],
    "Folha": [
        "https://feeds.folha.uol.com.br/emcimadahora/rss091.xml",
        "https://feeds.folha.uol.com.br/poder/rss091.xml",
        "https://feeds.folha.uol.com.br/mercado/rss091.xml",
    ],
    "Globo": [
        "https://pox.globo.com/rss/oglobo/",          # funciona
        "https://pox.globo.com/rss/g1/economia/noticia/",  # fallback G1
    ],
    "Estadao": [
        "https://www.estadao.com.br/arc/outboundfeeds/rss/?outputType=xml",  # funciona
        "https://economia.estadao.com.br/rss/ultimas",  # fallback
    ],
    "CNN Brasil": [
        "https://www.cnnbrasil.com.br/feed/",
    ],
    "Metropoles": [
        "https://www.metropoles.com/feed",
    ],
    "UOL": [
        "https://noticias.uol.com.br/ultnot/reuters/index.xml",
