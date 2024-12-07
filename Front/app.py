from flask import Flask, render_template, request, redirect, url_for, session
from assignWord import Ahorcado

app = Flask(__name__)
app.secret_key = "your_secret_key"

juego = Ahorcado('pepe')



@app.route("/")
def ingresar_palabra():
    return render_template("inicio.html")


@app.route("/guardar_nombre", methods=["POST"])
def guardar_nombre():
    palabra_secreta = request.form["nombre"]
    session["palabra_secreta"] = palabra_secreta
    #juego = Ahorcado(palabra_secreta)  # Crear una instancia del juego-
    return redirect(url_for("inicio")) #juego


'''@app.route("/elegir_dificultad")
def elegir_dificultad():
    if "nombre" not in session:
        return redirect(url_for("ingresar_nombre"))
    return render_template("inicio.html")'''


'''@app.route("/inicio/<nivel>")
def iniciar_juego(nivel):
    if "nombre" not in session:
        return redirect(url_for("ingresar_nombre"))
    ahorcado.iniciar_juego(nivel_dificultad=nivel)
    return redirect(url_for("inicio"))'''


@app.route("/inicio/")
def inicio():
    palabra_secreta = request.args.get("palabra_secreta")
    '''
    pista = request.args.get("pista")
    nivel = request.args.get("nivel")
    if "nombre" not in session:
        return redirect(url_for("ingresar_nombre"))
    if pala and pista:'''
    #ahorcado.iniciar_juego(nivel_dificultad=nivel, palabra=pala, pista=pista)
    juego.iniciar_juego(palabra=palabra_secreta)
    return render_template(
        "juego.html",
        palabra_a_mostrar=" ".join(juego.palabra_a_mostrar),
        intentos_restantes=juego.vidas_restantes,
        letras_usadas=juego.letras_arriesgada,
        juego_finalizado=juego.partida_concluida,
        #palabra_adivinada=juego.palabra_a_adivinar[0],
        img=juego.img,
        #pal_arriesgada=juego.palabra_vacia,
        #nombre_usuario=session.get("nombre"),
    )


@app.route("/intentar", methods=["POST"])
def intentar():
    letra = request.form["letra"].lower()
   
    if not juego.partida_concluida:
        juego.adivinando(juego.palabra_secreta,letra)
        juego.se_termino_el_juego()
    else:
        juego.fin_juego()
    return redirect(url_for("inicio"))


@app.route("/intentarP", methods=["POST"])
def intentarP():
    palabraA = request.form["palabraA"].lower()
    
    juego.arriesgaPalabra(juego.palabra_secreta,palabraA)
    juego.se_termino_el_juego()
    if juego.palabra_secreta[0].replace(" ", "") == palabraA.replace(" ", ""):
        juego.palabra_a_mostrar = juego.palabra_secreta[0]
    else:
        juego.palabra_a_mostrar = palabraA
    return redirect(url_for("inicio"))


'''@app.route("/reiniciar")
def reiniciar():
    ahorcado.reiniciar_juego()
    return redirect(url_for("elegir_dificultad"))'''


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
