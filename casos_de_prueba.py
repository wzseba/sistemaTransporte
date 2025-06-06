import networkx as nx
import matplotlib.pyplot as plt
from reversion import Grafo

#Caso base

edificios_importantes = ["Casa Rosada","Catedral","Cabildo","Congreso","Teatro Colón","Edificio Kavanagh"]

nodos_secundarios = ["Casa1","Casa2","Plaza de Mayo","Av de Mayo","Plaza San Martín"]


aristas = [("Casa Rosada","Cabildo",3),
           ("Casa Rosada","Casa1",1),
           ("Catedral","Casa2",1),
           ("Catedral","Plaza de Mayo",1),
           ("Catedral","Cabildo",3),
           ("Plaza de Mayo","Cabildo",1),
           ("Congreso","Av de Mayo",9),
           ("Av de Mayo","Teatro Colón",4),
           ("Edificio Kavanagh","Congreso",2),
           ("Edificio Kavanagh","Plaza San Martín",4),
           ("Plaza de Mayo","Teatro Colón",5),
           ("Teatro Colón","Edificio Kavanagh",2),
           ("Av de Mayo","Congreso",6),
           ("Plaza San Martín","nodo error2",30)]


#grafo vacio
"""
grafo = Grafo()
grafo.visualizar_circuito()
print(grafo.calcularRutaCamion())
"""

grafo1 = Grafo(edificios_importantes,nodos_secundarios,aristas)
print(grafo1.calcularRutaCamion())
grafo1.visualizar_circuito()