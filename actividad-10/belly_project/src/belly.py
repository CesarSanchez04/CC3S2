# src/belly.py
class Belly:
    def __init__(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def reset(self):
        self.pepinos_comidos = 0
        self.tiempo_esperado = 0

    def comer(self, pepinos):
        self.pepinos_comidos += pepinos

    def esperar(self, tiempo_en_horas):
        if tiempo_en_horas < 0:
            raise ValueError("El tiempo de espera no puede ser negativo.")
        self.tiempo_esperado += tiempo_en_horas


    def esta_gruñendo(self):
        # Nueva validación: no debería gruñir si se han comido menos de 5 pepinos
        if self.tiempo_esperado >= 1.5 and self.pepinos_comidos > 10:
            return True
        return False

