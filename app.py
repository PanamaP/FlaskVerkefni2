import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def default():
    return render_template("default.html")

@app.route('/a')
def heim():
    return render_template('layout.html')

@app.route('/kt-sida/<kt>')
def ktsida(kt):
    summa = 0
    for tala in kt:
        summa += int(tala)
    return render_template('kt-sum.html', kt=kt, summa=summa)

fretta_titill = [
    "Irma veldur usla á Flórída",
    "Veiðin er dræm þetta haustið",
    "Ólafía stendur sig vel",
    "Ísland dottið úr leik"
]
frettir = [
    "Það er bara helv... vesen á Irmu í Flórída. Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...",
    "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...",
    "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...",
    "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli. Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum.."
]

myndir = [
    "0.jpg", "1.jpg", "2.jpg", "3.jpg"
]

@app.route("/b")
def lidurb():
    return render_template("frettir.html", frettir=frettir)

@app.route("/frett/<int:nr>")
def frettsida(nr):
    titill = fretta_titill[nr]
    frett = frettir[nr]
    mynd = myndir[nr]
    return render_template("frettir_id.html", frett = frett, titill = titill, mynd = mynd)


@app.errorhandler(404)
def pagenotfound(error):
    return render_template('404villa.html'), 404


if __name__ == "__main__":
    app.run(debug=True)