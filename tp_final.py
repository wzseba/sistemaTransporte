import networkx as nx

class Grafo:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodosPrincipales = []

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
        
        #controlamos que el peso de las arista no sea negativo y que los nodos existan
        if(peso < 1):
            raise ValueError("El peso de la arista no puede ser negativo")
        if(not(origen in self.nodosPrincipales or origen in self.nodosSecundarios)):
            raise ValueError("El origen no es uno de los nodos previstos")
        elif(not(destino in self.nodosPrincipales or destino in self.nodosSecundarios)):
            raise ValueError("El destino no es uno de los nodos previstos")
        
        self.grafo.add_edge(origen, destino, weight=peso)

    def caminoMinimoAlumno(self, origen, destino):
        """
        Calcula el camino mínimo entre dos nodos.
        :param origen: Nodo de inicio
        :param destino: Nodo de fin
        :return: Lista de nodos en el camino mínimo
        """
        camino_minimo = nx.dijkstra_path(self.grafo, origen,destino)
        return camino_minimo
        
    def calcularRutaCamion(self, origen, destino):
        """
        Calcula la ruta óptima para un camión entre dos nodos.
        :param origen: Nodo de inicio
        :param destino: Nodo de fin
        :return: Devuelve
        """
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
    """
    Elimina un nodo del grafo.
    param nombre: Nombre del nodo a eliminar
    """
    self.grafo.remove_node(nombre)