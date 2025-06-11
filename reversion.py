import networkx as nx
import matplotlib.pyplot as plt


class Circuito_Ebike:
    def __init__(self, edificios_principales=[], lugares_secundarios=[], Rutas=[]):
        self.grafo = nx.Graph()
        self.edificios_principales = edificios_principales
        self.lugares_secundarios = lugares_secundarios
        self.grafo.add_nodes_from(edificios_principales)
        self.grafo.add_nodes_from(lugares_secundarios)
        # self.grafo.add_weighted_edges_from(Aristas)
        
        for origen, destino, distancia, segura in Rutas:
            #Evita que se agregen nodos que no estan en ninguna de las listas
            if(not(origen in self.edificios_principales or origen in self.edificios_principales)):
                raise ValueError("El origen no es uno de los lugares previstos")
            elif(not(destino in self.edificios_principales or destino in self.lugares_secundarios)):
                raise ValueError("El destino no es uno de los lugares previstos")
            
            if(distancia < 0):
                raise ValueError("La distancia no puede ser negativa")
            
            self.grafo.add_edge(origen, destino, weight=distancia, segura_para_ebike=segura)


    def agregar_ruta_y_edificio_principal(self, edificio_existente, edificio_nuevo, distancia, segura):
        
        if (distancia < 0):
            raise ValueError("El distancia de la arista no puede ser negativo")
        if (edificio_nuevo in self.edificios_principales):
            raise ValueError("El nodo ya existe")
        elif (edificio_existente not in self.edificios_principales):
            raise ValueError("El nodo no existe")
        
        self.grafo.add_node(edificio_nuevo)
        self.edificios_principales.append(edificio_nuevo)
        
         
        self.grafo.add_edge(edificio_existente, edificio_nuevo, weight=distancia, segura_para_ebike=segura)
    
    def agregar_ruta_y_lugar_secundario(self, punto_existente, punto_nuevo, distancia, segura):
        
        if (distancia < 0):
            raise ValueError("La distancia no puede ser negativa")
        if (punto_nuevo in self.edificios_principales):
            raise ValueError("El nodo ya existe")
        elif (punto_existente not in self.edificios_principales):
            raise ValueError("El nodo no existe")
        
        self.grafo.add_node(punto_nuevo)
        self.lugares_secundarios.append(punto_nuevo)  
        
         
        self.grafo.add_edge(punto_existente, punto_nuevo, weight=distancia, segura_para_ebike=segura)
        
    def agregar_ruta(self, origen, destino, distancia, segura):
        
        if (distancia < 0):
            raise ValueError("El distancia de la arista no puede ser negativo")
        if (not(origen in self.edificios_principales or origen in self.lugares_secundarios)):
            raise ValueError("El origen no es uno de los nodos previstos")
        elif (not(destino in self.edificios_principales or destino in self.lugares_secundarios)):        
            raise ValueError("El destino no es uno de los nodos previstos")
        
        self.grafo.add_edge(origen, destino, weight=distancia, segura_para_ebike=segura)
        
    def caminoMinimoAlumno(self, origen, destino):
       # Función callback para Dijkstra
        def ebike_seguro(i, f, data):
            # Si la arista es segura para ebikes, devuelve su distancia.
            # De lo contrario, devuelve None para que la ignore.
            if data.get("segura_para_ebike", False):
                return data.get("weight", 1) # Asume 1 si no hay 'weight' explícito
            else:
                return None # Ignora esta arista
        
        # Intenta encontrar el camino más corto entre origen y destino
        try:
            camino_minimo = nx.dijkstra_path(self.grafo, origen, destino, weight=ebike_seguro)
            costo = nx.dijkstra_path_length(self.grafo, origen, destino, weight=ebike_seguro)
            return camino_minimo, costo
        except nx.NetworkXNoPath:
            return None, "No hay camino seguro para ebikes entre los nodos especificados."

    def calcularRutaCamion(self):
        distancia_total = 0
        caminofinal = []  # lista que contendrá el recorrido a devolver

        # copia la lista de nodos principales, sin afectar el original
        principal = self.edificios_principales.copy()

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

    def eliminar_lugar(self, nombre):
        self.grafo.remove_node(nombre)
        if nombre in self.edificios_principales:
            self.edificios_principales.remove(nombre)
        elif nombre in self.lugares_secundarios:
            self.lugares_secundarios.remove(nombre)
    

    def visualizar_circuito(self):
        layout = nx.spring_layout(self.grafo)  # diseño del grafo
        labels = nx.get_edge_attributes(self.grafo, 'weight')  # obtiene los distancias

    # Dibuja el grafo
        nx.draw(self.grafo, pos=nx.circular_layout(self.grafo), with_labels=True,
            node_color='lightblue', edge_color='gray',
            node_size=1000, font_size=7, font_color='black', font_weight="bold")

    # Dibuja los distancias más cercanos a las aristas
        nx.draw_networkx_edge_labels(self.grafo,
                                 pos=nx.circular_layout(self.grafo),
                                 edge_labels=labels,
                                 label_pos=0.4,  # ajusta la posición a lo largo de la arista
                                 font_size=10,
                                 font_color='blue')  # opcional: cambiar color para mejor visibilidad

        plt.show()
        
        
