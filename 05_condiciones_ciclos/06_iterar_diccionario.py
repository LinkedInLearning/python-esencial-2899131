lenguaje = {
    "nombre": "python",
    "creador": "Guido Van Rossum"
}


# Iterar un diccionario
for llave in lenguaje:
    print(llave)
    print(lenguaje[llave])


# Iterar un diccionario usando keys()
for valor in lenguaje.keys():
    print(valor)


# Iterar un diccionario usando values()
for valor in lenguaje.values():
    print(valor)


# Iterar un diccionario usando items()
for llave, valor in lenguaje.items():
    print(llave, valor)
