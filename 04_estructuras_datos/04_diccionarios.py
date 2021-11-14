# Declarar un diccionario
lenguaje = {
    "nombre": "python",
    "creador": "Guido Van Rossum"
}
print(lenguaje["nombre"])

# Añadir nuevas llaves y valores
lenguaje["año_lanzamiento"] = 1991
print(lenguaje)

# Sobreescribir el valor de una llave
lenguaje["año_lanzamiento"] = 1999
print(lenguaje)

lenguaje["caracteristicas"] = ["sencillo" , "facil", "genial"]

# items() retorna una lista de tuplas (llave, valor)
print(lenguaje.items())

# keys() retorna una lista de las llaves del diccionario
print(lenguaje.keys())

# values() retorna una lista de los valores del diccionario
print(lenguaje.values())
