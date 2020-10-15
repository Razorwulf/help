from flask import Flask, render_template
from random import choice
 
app = Flask(__name__)
#v produkci smazat!
app.debug = True

def nahodny():
    return choice(["kámen", "Nůžky", "Papír"])

def vyhra(hrac, pocitac):
    if hrac == "Kámen" and pocitac == "Nůžky":
        return "Výhra"
        
    if hrac == pocitac:
        return "Remíza"
    
    if hrac == "Nůžky" and pocitac == "Papír":
        return "Výhra"
    if hrac == "Papír" and pocitac == "Kámen":
        return "Výhra"
    return "Prohra"

@app.route("/")
def vyber():

    return render_template ("index.html")

@app.route('/papir')
def papir():
    hrac = "Papír"
    obrazek="Papír.jpg"
    pocitac = nahodny()
    obrazekpc = pocitac
    vyhra2 = vyhra(hrac,pocitac)
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, vyhra=vyhra2,obrazek=obrazek,obrazekpc=obrazekpc)




@app.route('/nuzky')
def nuzky():
    hrac = "Nůžky"
    obrazek="Nůžky.jpg"
    pocitac = nahodny()
    obrazekpc = pocitac
    vyhra2 = vyhra(hrac,pocitac)
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, vyhra=vyhra2,obrazek=obrazek,obrazekpc=obrazekpc)

@app.route('/kamen')
def kamen():
    hrac = "Kámen"
    obrazek="Kámen.jpg"
    pocitac = nahodny()
    obrazekpc = pocitac
    vyhra2 = vyhra(hrac,pocitac)
    return render_template ("hra.html", pocitac=pocitac, hrac=hrac, vyhra=vyhra2,obrazek=obrazek,obrazekpc=obrazekpc)





 

if __name__ == '__main__':
    app.run()