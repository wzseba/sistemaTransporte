import networkx as nx
import matplotlib.pyplot as plt
from reversion import Grafo

#Caso base

edificios_importantes = ["Casa Rosada","Catedral","Cabildo","Congreso","Teatro Colón","Edificio Kavanagh"]

nodos_secundarios = ["Casa1","Casa2","Plaza de Mayo","Av de Mayo","Plaza San Martín"]


aristas = [("Casa Rosada","Cabildo",3,True),
           ("Casa Rosada","Casa1",1,True),
           ("Catedral","Casa2",1,True),
           ("Catedral","Plaza de Mayo",1,True),
           ("Catedral","Cabildo",3,True),
           ("Plaza de Mayo","Cabildo",1,True),
           ("Congreso","Av de Mayo",9,True),
           ("Av de Mayo","Teatro Colón",4,True),
           ("Edificio Kavanagh","Congreso",2,True),
           ("Edificio Kavanagh","Plaza San Martín",4,True),
           ("Plaza de Mayo","Teatro Colón",5,True),
           ("Teatro Colón","Edificio Kavanagh",2,True),
           ("Av de Mayo","Congreso",6,True),]


#grafo vacio
"""
grafo = Grafo()
grafo.visualizar_circuito()
print(grafo.calcularRutaCamion())
"""

#grafo1 = Grafo(edificios_importantes,nodos_secundarios,aristas)
#print(grafo1.calcularRutaCamion())
#grafo1.visualizar_circuito()

#------------------------------------------#
# Grafo 2
#------------------------------------------#
edificios_importantes = [
    "Obelisco", 
    "Palacio Barolo", 
    "Planetario Galileo Galilei", 
    "Biblioteca Nacional", 
    "Facultad de Derecho", 
    "Teatro San Martín",
    "Museo Nacional de Bellas Artes",
    "Centro Cultural Kirchner"
]

nodos_secundarios = [
    "Calle Corrientes", 
    "Avenida Santa Fe", 
    "Plaza Italia", 
    "Plaza Lavalle", 
    "Avenida Figueroa Alcorta",
    "Puerto Madero",
    "Parque Centenario"
]

aristas = [
    ("Obelisco", "Palacio Barolo", 3, True),
    ("Obelisco", "Calle Corrientes", 1, False),
    ("Planetario Galileo Galilei", "Avenida Figueroa Alcorta", 1, True),
    ("Planetario Galileo Galilei", "Plaza Italia", 1, False),
    ("Planetario Galileo Galilei", "Facultad de Derecho", 3, True),
    ("Plaza Italia", "Facultad de Derecho", 1, False),
    ("Biblioteca Nacional", "Avenida Santa Fe", 9, True),
    ("Avenida Santa Fe", "Teatro San Martín", 4, False),
    ("Teatro San Martín", "Biblioteca Nacional", 2, True),
    ("Teatro San Martín", "Plaza Lavalle", 4, True),
    ("Plaza Italia", "Teatro San Martín", 5, True),
    ("Teatro San Martín", "Obelisco", 2, False),
    ("Avenida Santa Fe", "Biblioteca Nacional", 6, True),
    ("Museo Nacional de Bellas Artes", "Facultad de Derecho", 1, True),
    ("Centro Cultural Kirchner", "Puerto Madero", 2, False),
    ("Centro Cultural Kirchner", "Obelisco", 5, False),
    ("Parque Centenario", "Planetario Galileo Galilei", 6, True),
]

"""
Prueba 1: Ruta segura para e-bikes (caminoMinimoAlumno)
Objetivo: Encontrar la ruta mas corta entre el Planetario y la Facultad de Derecho, usando solo aristas marcadas como segura.
"""
grafo2 = Grafo(edificios_importantes,nodos_secundarios,aristas)
print(grafo2.caminoMinimoAlumno("Planetario Galileo Galilei", "Facultad de Derecho"))
grafo2.visualizar_circuito()
