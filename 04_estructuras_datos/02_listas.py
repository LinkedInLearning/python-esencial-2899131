# Declarar una lista
lenguajes = ["python", "java", "javascript", "golang"]
print(lenguajes)

# Las listas pueden contener elementos de diferentes tipos
lista_a = [True, 1, 2.0, "python", 1] 
print(lista_a)

# Usamos indices para extraer un elemento
print(lenguajes[0])

# La función len() devuelve el tamaño de la lista
print(len(lenguajes))

# Usamos índices negativos para obtener las posiciones de la
# lista desde el último hasta el primero
print(lenguajes[-1])

# Usamos slicing para obtener una sublista
print(lenguajes[1:3])

# Litas anidadas
programacion = [lenguajes, "dedicacion", "practica"]
print(programacion)
print(programacion[0][0])

# Modificamos una posición asignandole un nuevo valor
lenguajes[0] = "dart"
print(lenguajes)

# append() permite añadir elemertos al final de la lista
lenguajes.append("python")
print(lenguajes)

# extend() permite unir dos listas
otros_lenguajes = ["c++", "c#"]
lenguajes.extend(otros_lenguajes)
print(lenguajes)

# Eliminación de elementos de la lista
lenguajes.pop(2)
lenguajes.pop("python")
