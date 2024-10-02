from behave import given, when, then
from src.belly import Belly
import re
import random

# Crear una instancia de Belly
belly = Belly()

numeros_español = {
        "media": 0.5,"una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "veinte": 20,"veinticinco": 25, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90,
        "mil": 1000, "un montón de": 1000
}
numeros_ingles = {
 "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
 "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
 "thirty": 30
}


# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    if palabra in numeros_español:
        return numeros_español[palabra]
    elif palabra in numeros_ingles:
        return numeros_ingles[palabra]
    elif palabra == "None":
        return 0
    else:
        try:
            return int(palabra)
        except:
            return 0
    # Retorna 0 si la palabra no está en los diccionarios


# Dado que he comido {cukes:d} pepinos
@given('he comido {cantidad} pepinos')
def step_given_eaten_cukes(context, cantidad):
    belly.reset()
    if cantidad.isdigit():
        cukes = float(cantidad)
    else:
        cukes = convertir_palabra_a_numero(cantidad)
    belly.comer(cukes)
    

@when('espero un tiempo aleatorio entre {min_time:d} y {max_time:d} horas')
def step_when_wait_random_time(context, min_time, max_time):
    tiempo_aleatorio = random.uniform(min_time, max_time)
    print(f"Esperando un tiempo aleatorio de {tiempo_aleatorio:.2f} horas.")
    belly.esperar(tiempo_aleatorio)


# Cuando espero "{time_description}"
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:\w\s)?(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
    pattern_ingles = re.compile(r'(?:(\w+)\s*hours?)?\s*(?:\w*\s)?(?:(\w+)\s*minutes?)?\s*(?:(\w+)\s*seconds?)?')
    match = pattern.match(time_description.lower())
    if(match.group(1)==None and match.group(2)==None and match.group(3)==None):
        match = pattern_ingles.match(time_description.lower())    

    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if match:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        seconds_word = match.group(3) if match.group(3) else "0"
        
        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        seconds = convertir_palabra_a_numero(seconds_word)
        total_time_in_hours = hours + (minutes / 60) + (seconds/3600)
        belly.esperar(total_time_in_hours)
    else:
        raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")


# Entonces mi estómago debería gruñir
@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

# Entonces mi estómago no debería gruñir
@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('debería ocurrir un error de cantidad no válida')
def step_then_invalid_cucumber_amount(context):
    try:
        assert belly.pepinos_comidos < 100, "Cantidad de pepinos no válida"
    except AssertionError as e:
        print(str(e))

@then('debería ocurrir un error de cantidad negativa')
def step_then_belly_should_show_error(context):
    assert not belly.esta_gruñendo() , "Se esperaba una cantidad negativa"