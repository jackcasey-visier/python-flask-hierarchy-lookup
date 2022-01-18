import logging

from lookup.entrypoint import search

from flask import Flask
from flask import request

app = Flask(__name__)

logging.basicConfig(level = logging.DEBUG)

@app.route("/")
def health():
    return {"health": "imok"}

@app.route("/<string:key>")
def lookup(key):
    return {key: search(key, request.args.to_dict())}
