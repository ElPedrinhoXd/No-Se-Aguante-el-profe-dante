from flask import Flask, render_template, redirect, request, url_for
import random

app = Flask(__name__)

contador = 0
sumador = 1
costo_mejora = 15

@app.route("/")
def principal():
    return render_template(
        "index.html",
        contador=contador,
        sumador=sumador,
        costo_mejora=costo_mejora,
        mostrar_chaman=False,
        mostrar_numero=False,
        numero=None
    )

@app.route("/sumar", methods=["POST"])
def sumar():
    global contador, sumador
    contador += sumador
    return redirect("/")

@app.route("/mejorarBoton", methods=["POST"])
def mejorar_boton():
    global contador, sumador, costo_mejora
    if contador >= costo_mejora:
        sumador += 1
        contador -= costo_mejora
        costo_mejora += 1
    return redirect("/")

@app.route("/AdvinoTuNumero", methods=["GET", "POST"])
def advino_tu_numero():
    if request.method == "POST":
        numero = request.form.get("numero")
        return redirect(url_for('mostrar_numero', numero=numero))
    return render_template("adivinador.html")

@app.route("/mostrarNumero")
def mostrar_numero():
    numero = request.args.get("numero")
    if not numero:
        return redirect(url_for('advino_tu_numero'))
    return render_template("mostrar_numero.html", numero=numero)


@app.route("/loteria")
def loteria():
    global contador
    numdeloteria = random.randint(1, 100)
    numelegido = 20

    if numdeloteria == numelegido:
        contador += 100
        return "GANASTE 100 MONEDAS GG BROOO"
    return f"Tengo {contador} monedas."

@app.route("/messi")
def messi():
    texto = "Hola, tu nombre es: Pedro y "
    texto += "Pedro y " * 499
    texto += "Pedro."
    return texto

if __name__ == "__main__":
    app.run(debug=True)
