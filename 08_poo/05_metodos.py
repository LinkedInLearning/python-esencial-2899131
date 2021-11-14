class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def cumplir_anios(self):
        self.edad += 1
        print(f"Feliz Cumpleaños #{self.edad}")


paco = Persona(nombre="Paco", edad=20)
paco.cumplir_anios()
