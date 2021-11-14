def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro


def area_cuadrado(lado):
    area = lado * lado
    return area


lado = 25
perimetro = perimetro_cuadrado(lado=lado)
area = area_cuadrado(lado=lado)

print(f"Area: {area}\nPerimetro: {perimetro}")


def no_return():
    pass

test = no_return()
print(test)


def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return perimetro, area


lado = 25
perimetro, area = calcular_cuadrado(lado)
print(f"Area: {area}\nPerimetro: {perimetro}")
