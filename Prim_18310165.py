"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2023-03-16"""

G = {
    '1': {'2': 4, '3': 2, '5': 3},
    '2': {'1': 4, '4': 5},
    '3': {'1': 2, '4': 1, '5': 6, '6': 3},
    '4': {'2': 5, '3': 1, '6': 6},
    '5': {'1': 3, '3': 6, '6': 2},
    '6': {'3': 3, '4': 6, '5': 2}
}


def prim(g, inicio):
    num = len(G)  # Número de nodos en el grafo
    s = inicio  # Nodo inicial
    vertices = {}  # Diccionario para verificar si un nodo está en el MST
    for nodo in g:
        vertices[nodo] = 0  # Inicialmente, ningún nodo está en el MST
    vertices[s] = 1  # El nodo inicial sí está en el MST
    E = []  # Lista de aristas del MST

    for m in range(num - 1):
        minimo = float('inf')  # Inicializamos el mínimo como infinito
        for j in g:
            if vertices[j] == 1:  # Si el nodo j está en el MST
                for k in g:
                    # Si el nodo k no está en el MST y la arista (j, k) tiene menor peso que el mínimo actual
                    if vertices[k] == 0 and w(g, j, k) < minimo:
                        agrega = k  # Nodo a agregar al MST
                        e = [j, k]  # Arista a agregar al MST
                        minimo = w(g, j, k)  # Actualizamos el mínimo
        vertices[agrega] = 1  # Marcamos el nodo agregado como parte del MST
        E.append(e)  # Agregamos la arista al MST

    return E


def w(g, m, j):
    if j in g[m]:
        return g[m][j]  # Retornamos el peso de la arista (m, j) si existe
    else:
        return float('inf')  # Retornamos infinito si no existe la arista


print(prim(G, '1'))