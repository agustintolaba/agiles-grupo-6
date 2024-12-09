Feature: Ingresar Palabra a Adivinar 
  Scenario: Usuario arriesga una palabra
    Given que estoy en la página de ingreso de nombre
    When jugador 1 ingresa la palabra a Adivinar "perro"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de juego
    When arriesgo la palabra "perro"
    Then la palabra "perro" debería ser registrada como adivinada
  

  Scenario: Usuario arriesga letras
    Given que estoy en la página de ingreso de nombre
    When jugador 1 ingresa la palabra a Adivinar "perro"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de juego
    When arriesgo la letra "p"
    Then la letra "p" debería ser registrada como usada
    When arriesgo la letra "e"
    Then la letra "e" debería ser registrada como usada
    When arriesgo la letra "r"
    Then la letra "r" debería ser registrada como usada
    When arriesgo la letra "o"
    Then la letra "o" debería ser registrada como usada  
    Then la palabra "perro" debería ser registrada como adivinada
