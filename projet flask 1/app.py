from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("ZoroConnexion.html")


@app.route("/index2/")
def acceuil():
    return render_template("index2.html")


@app.route("/index3/")
def index3():
    return render_template("index3.html")



@app.route("/modifier/")
def modifier():
    return render_template("modifier.html")

@app.route("/index4/")
def index4():
    return render_template("index4.html")



@app.route("/index5/")
def index5():
    return render_template("index5.html")

@app.route("/valider/")
def valider():
    return render_template("valider.html")

@app.route("/supprime/")
def supprime():
    return render_template("supprime.html")

@app.route("/dernier/")
def dernier():
    return render_template("dernier.html")

@app.route("/produit/")
def produit():
    return render_template("produit.html")


@app.route("/modproduit/")
def modproduit():
    return render_template("modproduit.html")


@app.route("/ajouterproduit/")
def ajouterproduit():
    return render_template("ajouterproduit.html")

@app.route("/valideproduit/")
def valideproduit():
    return render_template("valideproduit.html")


@app.route("/base/")
def base():
    return render_template("base.html")


if __name__=="__main__":
    app.run()

