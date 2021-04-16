from flask import Flask, redirect, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.kawalcorona.com/indonesia"
    req = requests.get(url)
    jeson = json.loads(req.text)

    for hasil in jeson:
        sembuh = hasil["sembuh"]
        wafat = hasil["meninggal"]
        positif = hasil["positif"]
    
    return render_template("index.html",sembuh = sembuh, death = wafat, positip = positif)

@app.route("/global")
def data_global():
    url = "https://api.kawalcorona.com/"
    req = requests.get(url)
    jeson = json.loads(req.text)

    return render_template("global.html",jeson = jeson)

@app.route("/provinsi")
def provinsi():
    url = "https://api.kawalcorona.com/indonesia/provinsi/"
    req = requests.get(url)
    jeson = json.loads(req.text)

    return render_template("provinsi.html",jeson = jeson)

if __name__ == "__main__":
    app.run(debug = True)
