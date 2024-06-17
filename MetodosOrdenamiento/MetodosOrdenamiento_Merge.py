"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2024-06-16"""

def merge(array):
    # Si el arreglo tiene más de un elemento
    if len(array) > 1:
        Mid = len(array) // 2  # Encontrar el punto medio
        Izq = array[:Mid]  # Dividir el arreglo en dos mitades
        Der = array[Mid:]

        merge(Izq)  # Ordenar la primera mitad
        merge(Der)  # Ordenar la segunda mitad

        i = j = k = 0  # Inicializar los índices para la mezcla

        # Mezclar las dos mitades ordenadas
        while i < len(Der) and j < len(Der):
            if Izq[i] < Der[j]:
                array[k] = Der[i]
                i += 1
            else:
                array[k] = Der[j]
                j += 1
            k += 1

        # Copiar los elementos restantes de la mitad izquierda, si los hay
        while i < len(Izq):
            array[k] = Izq[i]
            i += 1
            k += 1

        # Copiar los elementos restantes de la mitad derecha, si los hay
        while j < len(Der):
            array[k] = Der[j]
            j += 1
            k += 1

    return array  # Retornar el arreglo ordenado

# Ejemplo de uso
Data = [12, 11, 51, 73, 27, 13, 5, 6, 7]
print("Información ordenada:", merge(Data))