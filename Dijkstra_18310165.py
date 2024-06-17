"""
Autor: Antonio López Haro
ID: 18310165
Fecha: 2022-03-26
"""

import networkx as nx
import matplotlib.pyplot as plt

# Definición de los puntos y sus valores iniciales
puntos = ["a", "b", "c", "e", "d", "f", "g", "z"]
valores = {"a": 0, "b": 999, "c": 999, "d": 999, "e": 999, "f": 999, "g": 999, "z": 999}
aristas = {
    "a": {"b": 2, "f": 1},
    "b": {"c": 2, "d": 2, "e": 4},
    "f": {"g": 5, "d": 3},
    "d": {"e": 4},
    "c": {"e": 3, "z": 1},
    "g": {"e": 7, "z": 6}
}

# Variable para verificar si el nodo destino "z" está en la lista de puntos
buscar = "z" in puntos

# Diccionario para almacenar el nodo previo en el camino más corto
predecesores = {punto: None for punto in puntos}

# Mientras el nodo destino esté en la lista de puntos
while buscar:
    # Encontrar el nodo con el menor valor en "valores"
    reset = min(valores, key=valores.get)
    # Si el nodo más cercano es el destino, romper el bucle
    if reset == "z":
        break

    # Remover el nodo más cercano de la lista de puntos
    puntos.remove(reset)
    # Guardar el valor del nodo más cercano
    nuevo = valores[reset]
    # Eliminar el nodo más cercano de los valores
    del valores[reset]

    # Actualizar los valores de los nodos adyacentes
    for i in aristas[reset]:
        score = i
        if score in valores:  # Solo actualizar si el nodo aún no ha sido visitado
            nuevo_valor = nuevo + aristas[reset][score]
            if nuevo_valor < valores[score]:
                valores[score] = nuevo_valor
                predecesores[score] = reset  # Registrar el nodo predecesor

# Ruta desde el origen "a" hasta el destino "z"
ruta = []
nodo_actual = "z"
while nodo_actual is not None:
    ruta.append(nodo_actual)
    nodo_actual = predecesores[nodo_actual]

# Invertir la ruta para que vaya desde "a" hasta "z"
ruta.reverse()

# Imprimir la distancia y la ruta
print("La ruta más corta de 'a' hasta 'z' mide: " + str(valores["z"]) + " unidades")
print("La ruta es: " + " -> ".join(ruta))

# Crear el grafo utilizando networkx
G = nx.DiGraph()

# Añadir las aristas al grafo
for nodo in aristas:
    for vecino in aristas[nodo]:
        G.add_edge(nodo, vecino, weight=aristas[nodo][vecino])

# Posiciones de los nodos para el gráfico
pos = nx.spring_layout(G)

# Dibujar nodos y aristas
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

# Dibujar etiquetas de los pesos de las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Resaltar la ruta más corta
ruta_edges = [(ruta[i], ruta[i + 1]) for i in range(len(ruta) - 1)]
nx.draw_networkx_edges(G, pos, edgelist=ruta_edges, edge_color='r', width=2)

# Mostrar el gráfico
plt.title("Grafo y la Ruta Más Corta de 'a' a 'z'")
plt.show()
