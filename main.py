from flask import Flask, request
from models import Source
from provider import Provider

app = Flask(__name__)

provider = Provider()

logger = app.logger


@app.get("/")
def health():
    return "OK", 200


@app.post("/crawler/start")
def start_crawler():
    body = request.get_json()
    sources = [Source(**source) for source in body]
    provider.start_crawling(sources)
    return "OK", 200
