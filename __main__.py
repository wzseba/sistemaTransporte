import networkx as nx
import matplotlib.pyplot as plt
from reversion import Grafo
nodosPrincipales = ["A", "B", "C", "D", "Z"]
nodosSecundarios = [1, 2, 3, 4, 5, 6]
Aristas = ([("A", "Z", 3,True), ("A", 3, 2,True), ("Z", 2, 5,True), (2, "C", 5,True), (3, 2, 1,True), (
    3, 4, 1,True), (4, 1, 7,True), (1, 5, 8, False), (5, "D", 3,True), ("D", 6, 2,True), (6, "B", 8,True), ("B", "C", 4,True), (1, "C", 5,True)])

circuito1 = Grafo(nodosPrincipales, nodosSecundarios, Aristas)
circuito1.visualizar_circuito()
print(circuito1.calcularRutaCamion())
print(circuito1.caminoMinimoAlumno(3, "D"))

#circuito1.agregar_nodo_principal("X")
#print(circuito1.caminoMinimoAlumno(3, "D"))
#circuito1.visualizar_circuito()
#circuito1.agregar_arista("X", "B", 2, False)
#print(circuito1.calcularRutaCamion())
#circuito1.eliminar_nodo("X")
#circuito1.visualizar_circuito()
#print(circuito1.calcularRutaCamion())
