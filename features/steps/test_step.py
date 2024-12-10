from behave import *
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:5000/"


@given("que estoy en la página de ingreso de nombre")
def step_given_en_pagina_ingreso_nombre(context):
    context.browser.get(f"{BASE_URL}/")
    time.sleep(1)


@when('jugador 1 ingresa la palabra a adivinar "{palabraAdivinar}"')
def step_when_ingreso_palabraAdivinar(context, palabraAdivinar):
    input_palabraAdivinar = context.browser.find_element(By.NAME, "nombre")
    input_palabraAdivinar.send_keys(palabraAdivinar)
    time.sleep(1)


@when('hago clic en el botón "Siguiente"')
def step_when_hago_clic_en_guardar(context):
    boton_siguiente = context.browser.find_element(
        By.CSS_SELECTOR, 'form button[type="submit"]'
    )
    boton_siguiente.click()
    time.sleep(1)

@then("debo ser redirigido a la página de juego")
def step_then_redirigido_a_pagina_de_juego(context):
    time.sleep(1)
    assert "inicio" in context.browser.current_url


@when('arriesgo la letra "{letra}"')
def step_when_arriesgo_letra(context, letra):
    input_letra = context.browser.find_element(By.ID, "letra")
    input_letra.send_keys(letra)
    wait = WebDriverWait(context.browser, 10)
    boton_enviar = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Arriesgar Letra']"))
    )
    boton_enviar.click()
    time.sleep(1)


@then('la letra "{letra}" debería ser registrada como usada')
def step_then_letra_registrada(context, letra):
    wait = WebDriverWait(context.browser, 10)
    # Seleccionar el elemento <p> que contiene el texto "Letras usadas:"
    letras_usadas_elemento = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[strong[contains(text(), 'Letras usadas:')]]")
        )
    )
    letras_usadas_texto = letras_usadas_elemento.text
    print(f"Contenido actual de letras usadas: {letras_usadas_texto}")
    # Asegurarse de que la letra esté en el texto después de "Letras usadas: "
    letras_usadas_texto = letras_usadas_texto.replace("Letras usadas: ", "")
    assert (
        letra in letras_usadas_texto
    ), f"La letra {letra} no está registrada como usada."


@when('arriesgo la palabra "{palabra}"')
def step_when_arriesgo_palabra(context, palabra):
    wait = WebDriverWait(context.browser, 10)
    input_palabra = wait.until(EC.presence_of_element_located((By.ID, "palabraA")))
    input_palabra.send_keys(palabra)
    boton_enviar = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Arriesgar Palabra']"))
    )
    boton_enviar.click()
    time.sleep(1)

@then('El juego se ha ganado')
def step_juego_ganado(context):
    wait = WebDriverWait(context.browser, 10)
    texto_ganador = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='mensaje-final']"))    
    ).text
    assert (
        texto_ganador == "¡Felicidades has ganado!"
    )


@then('El juego se ha perdido')
def step_juego_perdido(context):
    wait = WebDriverWait(context.browser, 10)
    texto_ganador = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='mensaje-final']"))    
    ).text
    assert (
        texto_ganador == "Lo siento, has perdido."
    )

@when('hago clic en el botón "Reiniciar')
def step_when_hago_clic_en_reiniciar(context):
    boton_reiniciar = context.browser.find_element(By.LINK_TEXT, "Reiniciar")
    boton_reiniciar.click()
    time.sleep(1)