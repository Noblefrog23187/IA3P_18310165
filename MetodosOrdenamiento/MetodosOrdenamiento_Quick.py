""" Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""

def quick(array):
    # Caso base: si el arreglo tiene uno o cero elementos, ya está ordenado
    if len(array) <= 1:
        return array
    else:
        pivote = array[len(array) // 2]  # Elegir el pivote como el elemento medio
        # Dividir el arreglo en tres partes
        left = [x for x in array if x < pivote]  # Elementos menores que el pivote
        middle = [x for x in array if x == pivote]  # Elementos iguales al pivote
        right = [x for x in array if x > pivote]  # Elementos mayores que el pivote
        # Ordenar recursivamente las sublistas y combinarlas
        return quick(left) + middle + quick(right)

Data = [3, 6, 8, 10, 1, 2, 1, 9]
print("Información ordenada:", quick(Data))