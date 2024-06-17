"""Autor: Antonio López Haro
ID: 18310165
Fecha: 2023-03-16"""


import networkx as nx
import matplotlib.pyplot as plt

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


print(prim(G, '1))

# Definir el grafo original usando networkx
G_nx = nx.Graph()
for nodo in G:
    for vecino, peso in G[nodo].items():
        G_nx.add_edge(nodo, vecino, weight=peso)

# Ejecutar el algoritmo de Prim y obtener el MST
mst_edges = prim(G, '1')

# Definir el MST usando networkx
MST_nx = nx.Graph()
for edge in mst_edges:
    MST_nx.add_edge(edge[0], edge[1], weight=G[edge[0]][edge[1]])

# Dibujar el grafo original y el MST
plt.figure(figsize=(14, 7))

# Subplot para el grafo original
plt.subplot(121)
pos = nx.spring_layout(G_nx)
nx.draw(G_nx, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=14)
labels = nx.get_edge_attributes(G_nx, 'weight')
nx.draw_networkx_edge_labels(G_nx, pos, edge_labels=labels)
plt.title("Grafo Original")

# Subplot para el MST
plt.subplot(122)
pos = nx.spring_layout(MST_nx)
nx.draw(MST_nx, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=14)
labels = nx.get_edge_attributes(MST_nx, 'weight')
nx.draw_networkx_edge_labels(MST_nx, pos, edge_labels=labels)
plt.title("Árbol de Expansión Mínima (MST)")

plt.show()
