# Declarar un set
set_a = {1, 2, 3}
print(type(set_a), set_a)

# Si hay elementos repetidos solo se conserva el elemento una vez
set_b = {1, 2, 3, 4, 5, 1}
print(set_b)

# Puede tener elementos de diferentes tipos
set_c = {1, 2, True, "texto"}
print(set_c)

# Añadir elementos al set
set_a .add(4)

# Actualizar un set
set_a.update([4, 5, 6])

# Tamaño de un set
len(set_a)

# Eliminar un elemento de un set
set_a.discard(2)
set_a.remove(2)

# Eliminar todos los elementos de un set
set_a.clear()
