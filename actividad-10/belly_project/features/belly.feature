Feature: Característica del Estómago

  Scenario: comer muchos pepinos y gruñir
    Given he comido 42 pepinos
    When espero 2 horas
    Then mi estómago debería gruñir

  Scenario: comer pocos pepinos y no gruñir
    Given he comido 10 pepinos
    When espero 2 horas
    Then mi estómago no debería gruñir

  Scenario: comer muchos pepinos y esperar menos de una hora
    Given he comido 50 pepinos
    When espero media hora
    Then mi estómago no debería gruñir

  Scenario: comer pepinos y esperar en minutos
    Given he comido 30 pepinos
    When espero 90 minutos
    Then mi estómago debería gruñir

  Scenario: comer pepinos y esperar en diferentes formatos
    Given he comido 25 pepinos
    When espero "dos horas y treinta minutos"
    Then mi estómago debería gruñir

  Scenario: Comer diferentes cantidades de pepinos en varios tiempos
    Given he comido 30 pepinos
    When espero "una hora y treinta minutos"
    Then mi estómago debería gruñir

  Scenario: Comer pepinos sin especificar cantidad exacta
    Given he comido "un montón" de pepinos
    When espero 3 horas
    Then mi estómago debería gruñir

  Scenario: Comer pepinos y esperar un tiempo exacto en minutos
    Given he comido 20 pepinos
    When espero 120 minutos
    Then mi estómago debería gruñir

  Scenario: Comer pepinos en palabras y tiempo en minutos
    Given he comido "veinticinco pepinos"
    When espero "noventa minutos"
    Then mi estómago debería gruñir
  
  Scenario: Comer una cantidad no válida de pepinos
    Given he comido "mil pepinos"
    When espero 2 horas
    Then debería ocurrir un error de cantidad no válida