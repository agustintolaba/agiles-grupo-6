from flask import Flask, render_template, request, redirect, url_for, session
from assignWord import Ahorcado

app = Flask(__name__)
app.secret_key = "your_secret_key"

juego = Ahorcado()  # Crear una instancia del juego-



@app.route("/")
def ingresar_palabra():
    return render_template("inicio.html")


@app.route("/guardar_nombre", methods=["POST"])
def guardar_nombre():
    palabra_secreta = request.form["nombre"]
    session["palabra_secreta"] = palabra_secreta

    return redirect(url_for("inicio")) #juego

@app.route("/inicio/")
def inicio():

    palabra_secreta = session.get("palabra_secreta")
    
    juego.iniciar_juego(palabra_secreta)
    return render_template(
        "juego.html",
        palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
        intentos_restantes=juego.vidas_restantes,
        letras_usadas=juego.letras_arriesgada,
        juego_finalizado=juego.partida_concluida,
        palabra_adivinada=juego.palabra_secreta,
        img=juego.img,
    )

@app.route("/segundo/")
def segundo():
    
    palabra_secreta = session.get("palabra_secreta")
    
    juego.fin_juego()
    return render_template(
        "juego.html",
        palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
        intentos_restantes=juego.vidas_restantes,
        letras_usadas=juego.letras_arriesgada,
        juego_finalizado=juego.partida_concluida,
        palabra_adivinada=juego.palabra_secreta,
        img=juego.img,
        pal_arriesgada=juego.palabra_vacia,
    )

@app.route("/intentar", methods=["POST"])
def intentar():
    letra = request.form["letra"].lower()
    print(juego.partida_concluida)
    if not juego.partida_concluida:
        juego.intento(letra)
        juego.se_termino_el_juego()
    else:
        juego.fin_juego()
    return redirect(url_for("segundo"))


@app.route("/intentarP", methods=["POST"])
def intentarP():
    palabraA = request.form["palabraA"].lower()
    
    juego.intentoP(palabraA)
    juego.se_termino_el_juego()
    if juego.palabra_secreta[0].replace(" ", "") == palabraA.replace(" ", ""):
        juego.palabra_a_mostrar = juego.palabra_secreta[0]
    else:
        juego.palabra_a_mostrar = palabraA
    return redirect(url_for("segundo"))


@app.route("/reiniciar")
def reiniciar():
    return render_template("inicio.html")


"""if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)"""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)


