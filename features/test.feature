Feature: Ingresar Palabra a Adivinar 
  Scenario: Usuario arriesga una palabra correcta
    Given que estoy en la página de ingreso de nombre
    When jugador 1 ingresa la palabra a Adivinar "perro"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de juego
    When arriesgo la palabra "perro"
    Then El juego se ha ganado
    When hago clic en el botón "Reiniciar
    Given que estoy en la página de ingreso de nombre

  Scenario: Usuario arriesga una palabra incorrecta
    Given que estoy en la página de ingreso de nombre
    When jugador 1 ingresa la palabra a Adivinar "perro"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de juego
    When arriesgo la palabra "gato"
    Then El juego se ha perdido
    When hago clic en el botón "Reiniciar
    Given que estoy en la página de ingreso de nombre

  Scenario: Usuario arriesga letras correctamente
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
    Then El juego se ha ganado  
    When hago clic en el botón "Reiniciar
    Given que estoy en la página de ingreso de nombre

  Scenario: Usuario arriesga letras incorrectamente
    Given que estoy en la página de ingreso de nombre
    When jugador 1 ingresa la palabra a Adivinar "perro"
    And hago clic en el botón "Siguiente"
    Then debo ser redirigido a la página de juego
    When arriesgo la letra "w"
    Then la letra "w" debería ser registrada como usada
    When arriesgo la letra "q"
    Then la letra "q" debería ser registrada como usada
    When arriesgo la letra "n"
    Then la letra "n" debería ser registrada como usada
    When arriesgo la letra "t"
    Then la letra "t" debería ser registrada como usada
    When arriesgo la letra "z"
    Then la letra "z" debería ser registrada como usada
    Then El juego se ha perdido
    When hago clic en el botón "Reiniciar
    Given que estoy en la página de ingreso de nombre