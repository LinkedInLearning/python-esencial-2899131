class Persona:
    atributo = 123

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


paco = Persona(nombre="Paco", edad=20)
print(paco.nombre)
print(paco.edad)
print(paco.atributo)
