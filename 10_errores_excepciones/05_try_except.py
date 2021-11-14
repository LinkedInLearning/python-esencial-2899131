def calcular_promedio(lista):
    assert len(lista) > 0, "La lista está vacía"
    return sum(lista) / len(lista)


try:
    promedio = calcular_promedio(["texto"])
    print(promedio)
except AssertionError as assert_error:
    print("La función no fue ejecutada")
    print("Excepción:", assert_error)
except Exception as e:
    print("Excepción:", e)

print("Ya no estoy en el bloque try-except")
