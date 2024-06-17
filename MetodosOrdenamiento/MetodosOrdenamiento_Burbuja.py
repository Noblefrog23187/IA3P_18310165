"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""

def bubble(array):
    n = len(array)# Obtener la longitud del arreglo
    for i in range(n):     # Bucle para hacer iteraciones
        for j in range(0, n-i-1):     # Bucle para comparar e intercambiar elementos
            if array[j] > array[j+1]:  # Si el elemento actual es mayor que el siguiente, intercambiar posiciones
                array[j], array[j+1] = array[j+1], array[j]
    return array

Data = [64, 34, 25, 12, 22, 11, 90]
print("Información ordenada:", bubble(Data))