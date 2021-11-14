def validar_x(x):
    if x < 0.5:
        raise Exception("La variable x  debe ser mayor a 0.5")


x = 0.3
resultado = validar_x(x)
print(resultado)
