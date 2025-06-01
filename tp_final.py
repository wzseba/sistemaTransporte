import networkx as nx
#coment, intento de modificacion
class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()

        """
        Agrega un nodo al grafo con un nombre y tipo especificados.
        
        :param nombre: Nombre del nodo a agregar.
        :param tipo: Tipo del nodo (por ejemplo, 'principal', 'secundario')
        """
    def agregar_nodo(self, nombre, tipo):
        self.grafo.add_node(nombre, tipo=tipo)

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una arista entre dos nodos.
        :param origen: Nodo de inicio
        :param destino: Nodo de fin
        :param peso: Costo del recorrido
        """
        self.grafo.add_edge(origen, destino, weight=peso)

    def caminoMinimoAlumno(self, origen, destino):
        """
        Calcula el camino mínimo entre dos nodos.
        :param origen: Nodo de inicio
        :param destino: Nodo de fin
        :return: Lista de nodos en el camino mínimo
        """
    
    def calcularRutaCamion(self, origen, destino):
        """
        Calcula la ruta óptima para un camión entre dos nodos.
        :param origen: Nodo de inicio
        :param destino: Nodo de fin
        :return: ?
        """
    def eliminar_nodo(self, nombre):
        """
        Elimina un nodo del grafo.
        :param nombre: Nombre del nodo a eliminar
        """
        self.grafo.remove_node(nombre)