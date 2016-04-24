from flask import Flask, jsonify, render_template as render
from lxml.html import fromstring as html, tostring as tos
from requests import get
import xmltodict
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render('index.html')

@app.route("/apa.json")
def apa():
    base_url = 'http://vermont.craigslist.org'
    full_url = 'http://vermont.craigslist.org/search/apa?query=burlington'
    return jsonify(
        base_url=base_url,
        full_url=full_url,
        apts=([xmltodict.parse(tos(el)) for el in html(get(full_url).text).xpath("//p[@class='row']")])
    )

if __name__=='__main__':
    app.run(debug=True)
