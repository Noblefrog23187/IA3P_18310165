"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""

def insercion(array):
    # Empezar desde el segundo elemento hasta el final del arreglo
    for i in range(1, len(array)):
        key = array[i]  # Guardar el valor actual
        j = i - 1  # Empezar a comparar con los elementos anteriores
        while j >= 0 and key < array[j]:  # Desplazar los elementos mayores hacia adelante
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key  # Insertar el elemento en su posición correcta
    return array  # Retornar el arreglo ordenado


# Ejemplo de uso
Data = [12, 11, 13, 5, 6]
print("Información ordenada: ", insercion(Data))
