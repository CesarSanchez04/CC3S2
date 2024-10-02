from behave import given, when, then
from src.belly import Belly
import re

# Crear una instancia de Belly
belly = Belly()

numeros_extendido = {
        "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "veinte": 20, "treinta": 30, "cuarenta": 40, "cincuenta": 50,
        "sesenta": 60, "setenta": 70, "ochenta": 80, "noventa": 90
}
# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    return numeros_extendido.get(palabra, 0)  # Retornar 0 si la palabra no está en el diccionario

# Dado que he comido {cukes:d} pepinos
@given('he comido {cantidad} pepinos')
def step_given_eaten_cukes(context, cantidad):
    if cantidad.isdigit():
        cukes = int(cantidad)
    else:
        cukes = convertir_palabra_a_numero(cantidad) if cantidad in numeros_extendido else 0
    belly.comer(cukes)

# Cuando espero "{time_description}"
@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    # Expresión regular para encontrar horas y minutos en una descripción con palabras o números
    pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?')
    match = pattern.match(time_description.lower())

    # Si se encuentra coincidencia, convertir palabras o números a horas y minutos
    if match:
        hours_word = match.group(1) if match.group(1) else "0"
        minutes_word = match.group(2) if match.group(2) else "0"
        hours = convertir_palabra_a_numero(hours_word)
        minutes = convertir_palabra_a_numero(minutes_word)
        total_time_in_hours = hours + (minutes / 60)
        print(total_time_in_hours)
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

