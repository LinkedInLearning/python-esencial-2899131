def perimetro_cuadrado(lado):
    """Calcula el perimetro de un cuadrado."""

    perimetro = lado * 4
    return perimetro


def area_cuadrado(lado):
    """Calculo del area de un cuadrado.

    Esta función recibe el valor de un lado de un cuadrado y a partir
    de este calcula y retorna su área.

    Args:
        lado (int): medida del lado del cuadrado
    
    Returns:
        area (int): area del cuadrado
    """

    area = lado * lado
    return area
