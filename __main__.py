import networkx as nx
import matplotlib.pyplot as plt
from reversion import Grafo
nodosPrincipales = ["A", "B", "C", "D", "Z"]
nodosSecundarios = [1, 2, 3, 4, 5, 6]
Aristas = ([("A", "Z", 3), ("A", 3, 2), ("Z", 2, 5), (2, "C", 5), (3, 2, 1), (
    3, 4, 1), (4, 1, 7), (1, 5, 8), (5, "D", 3), ("D", 6, 2), (6, "B", 8), ("B", "C", 4), (1, "C", 5)])

circuito1 = Grafo(nodosPrincipales, nodosSecundarios, Aristas)
circuito1.visualizar_circuito()
print(circuito1.calcularRutaCamion())
print(circuito1.caminoMinimoAlumno(3, "D"))

circuito1.agregar_nodo_principal("X")
circuito1.agregar_arista("X", "B", 2)
circuito1.visualizar_circuito()
print(circuito1.calcularRutaCamion())

circuito1.eliminar_nodo("X")
circuito1.visualizar_circuito()
print(circuito1.calcularRutaCamion())
