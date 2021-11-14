# Iterar una lista con ciclo for
lenguajes = ["python", "java", "javascript", "golang"]
for elemento in lenguajes:
    print(elemento)


# Iterar una lista con ciclo for, usando range() y len()
lenguajes = ["python", "java", "javascript", "golang"]
for index in range(len(lenguajes)):
    print("Index:", index)
    print("Element:", lenguajes[index])


# Iterar una lista con ciclo while
lenguajes = ["python", "java", "javascript", "golang"]
i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1
