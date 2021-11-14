def calcular_promedio(lista):
    assert len(lista) > 0, "La lista está vacía"
    return sum(lista) / len(lista)


promedio = calcular_promedio(lista=[])
promedio = calcular_promedio(lista=[1, 2, 3])
print(promedio)
