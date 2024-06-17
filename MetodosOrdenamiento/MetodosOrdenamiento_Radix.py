""" Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""


def counting(array, exp):
    n = len(array)  # Obtener la longitud del arreglo
    output = [0] * n  # Arreglo de salida
    count = [0] * 10  # Contador para los dígitos (base 10)

    # Contar ocurrencias de dígitos
    for i in range(n):
        index = (array[i] // exp) % 10
        count[index] += 1

    # Cambiar count[i] para que contenga la posición real de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construir el arreglo de salida
    for i in range(n - 1, -1, -1):
        index = (array[i] // exp) % 10
        output[count[index] - 1] = array[i]
        count[index] -= 1

    # Copiar el arreglo de salida a arr, para que arr contenga los números ordenados por dígitos actuales
    for i in range(n):
        array[i] = output[i]

def radix_sort(array):
    # Encontrar el número máximo para saber el número de dígitos
    max1 = max(array)

    # Hacer counting sort para cada dígito. exp es 10^i, donde i es el dígito actual
    exp = 1
    while max1 // exp > 0:
        counting(array, exp)
        exp *= 10

    return array  # Retornar el arreglo ordenado

# Ejemplo de uso
Data = [170, 45, 75, 90, 802, 24, 2, 66]
print("Información ordenada:", radix_sort(Data))