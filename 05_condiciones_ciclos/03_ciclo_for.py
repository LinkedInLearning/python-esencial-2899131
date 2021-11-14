# Iterar un string
for letra in "Texto":
    print(letra)


# Iterar una lista
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)


# La instrucción break rompe el ciclo
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)
    break


# Instrucción break dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        break
print(elemento)


# Instrucción continue dentro de una condición
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    if elemento == "javascript":
        continue
print(elemento)


# Función range()
for element in range(1, 6):
    print(element)
