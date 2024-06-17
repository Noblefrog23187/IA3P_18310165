"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""

def seleccion(array):
    n = len(array)  # Obtener la longitud del arreglo
    # Bucle para recorrer todo el arreglo
    for i in range(n):
        nuevo_min = i  # Asumir el primer elemento no ordenado como el mínimo
        # Encontrar el mínimo en la sublista no ordenada
        for j in range(i+1, n):
            if array[j] < array[nuevo_min]:
                nuevo_min = j  # Actualizar el nuevo mínimo
        # Intercambiar el elemento mínimo con el primer elemento no ordenado
        array[i], array[nuevo_min] = array[nuevo_min], array[i]
    return array


Data = [45,22,11,55,88,66,33,-3]
print("Información ordenada:", seleccion(Data))