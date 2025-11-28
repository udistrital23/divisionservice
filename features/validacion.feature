 # language: es
Característica: Division de dos numeros no negativos en base 10
  
  Escenario: Division exitosa de dos numeros positivos
    Dado los numeros 10 y 5
    Cuando realizo la division
    Entonces el resultado debe ser 2

  Escenario: Intento de division por cero
    Dado los numeros 10 y 0
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "No se puede dividir por cero"

  Escenario: Intento de division con dividendo negativo
    Dado los numeros -10 y 5
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "Los numeros deben ser positivos"

  Escenario: Intento de division con divisor negativo
    Dado los numeros 10 y -5
    Cuando intento realizar la division
    Entonces se lanza una excepcion de "Los numeros deben ser positivos"
