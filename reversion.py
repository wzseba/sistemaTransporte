import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def __init__(self, Principales=[], Secundarios=[], Aristas=[]):
        self.grafo = nx.Graph()
        self.nodosPrincipales = Principales
        self.nodosSecundarios = Secundarios
        self.grafo.add_nodes_from(Principales)
        self.grafo.add_nodes_from(Secundarios)
        self.grafo.add_weighted_edges_from(Aristas)

    def agregar_nodo_principal(self, nombre):
        self.grafo.add_node(nombre)
        self.nodosPrincipales.append(nombre)

    def agregar_nodo_secundario(self, nombre):
        self.grafo.add_node(nombre)
        self.nodosSecundarios.append(nombre)

    def agregar_arista(self, origen, destino, peso):
        self.grafo.add_edge(origen, destino, weight=peso)

    def caminoMinimoAlumno(self, origen, destino):
        camino_minimo = nx.dijkstra_path(self.grafo, origen, destino)
        return camino_minimo

    def calcularRutaCamion(self):
        caminofinal = []  # lista que contendrá el recorrido a devolver

        # copia la lista de nodos principales, sin afectar el original
        principal = self.nodosPrincipales.copy()

        agregar = []  # lista que contiene el camino más corto y se agrega a la lista final en cada iteración

        for i in range(len(principal)-1):

            # defino el origen como el primer nodo de la lista principal
            Origen = principal[0]

            # defino el destino como el segundo nodo de la lista principal
            Destino = principal[1]

            # será el valor por default para comparar los caminos y poder luego encontrar el minimo
            aux = nx.dijkstra_path_length(self.grafo, Origen, Destino)

            nuevoOrigen = Destino

            agregar = nx.dijkstra_path(self.grafo, Origen, Destino)
            # iteracion que buscará con dijkstra el camino mas corto, arranca en la posición 2
            for j in principal[2:]:
                Destino = j
                # compara el nuevo valor de dijkstra con el valor por default
                costo = nx.dijkstra_path_length(self.grafo, Origen, Destino)
                if (costo < aux):
                    aux = costo
                    nuevoOrigen = Destino
                    agregar = nx.dijkstra_path(self.grafo, Origen, Destino)

            if (caminofinal):  # si existe un camino previo se agregará el camino siguiente pero sin el origen (asi no se repiten nodos)
                caminofinal.extend(agregar[1:])
            else:
                # solo en la primera iteracion se agrega el camino completo
                caminofinal.extend(agregar)

            principal.remove(Origen)
            principal.remove(nuevoOrigen)
            principal.insert(0, nuevoOrigen)

        return caminofinal  # devuelve la lista con el recorrido

    def eliminar_nodo(self, nombre):
        self.grafo.remove_node(nombre)
        if nombre in self.nodosPrincipales:
            self.nodosPrincipales.remove(nombre)
        elif nombre in self.nodosSecundarios:
            self.nodosSecundarios.remove(nombre)

    def visualizar_circuito(self):
        layout = nx.spring_layout(self.grafo)  # diseño del grafo
        labels = nx.get_edge_attributes(self.grafo, 'weight')  # obtiene los pesos

    # Dibuja el grafo
        nx.draw(self.grafo, pos=nx.circular_layout(self.grafo), with_labels=True,
            node_color='lightblue', edge_color='gray',
            node_size=1000, font_size=7, font_color='black', font_weight="bold")

    # Dibuja los pesos más cercanos a las aristas
        nx.draw_networkx_edge_labels(self.grafo,
                                 pos=nx.circular_layout(self.grafo),
                                 edge_labels=labels,
                                 label_pos=0.4,  # ajusta la posición a lo largo de la arista
                                 font_size=10,
                                 font_color='blue')  # opcional: cambiar color para mejor visibilidad

        plt.show()

