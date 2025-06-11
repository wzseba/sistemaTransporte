import networkx as nx
import matplotlib.pyplot as plt
from reversion import Grafo

#-----------------------------------------------------------#
#                          Grafo 1                          #
#-----------------------------------------------------------#

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

grafo1 = Grafo(edificios_importantes,nodos_secundarios,aristas)


#Prueba 1: Caso base
#Objetivo: ?.

"""
grafo1.visualizar_circuito()
"""


#Prueba 2: Ruta segura para e-bikes (caminoMinimoAlumno)
#Objetivo: Encontrar la ruta mas corta entre el Planetario y la Facultad de Derecho, usando solo aristas marcadas como segura.

"""
print(grafo1.caminoMinimoAlumno("Planetario Galileo Galilei", "Facultad de Derecho"))
grafo1.visualizar_circuito()
"""

#Prueba 3: Peso de aristas negativo
#Objetivo: Detectar un error al usar valores negativos en el peso de las aristas.

"""
grafo1.agregar_arista("Casa1", "Congreso", -1, True)
grafo1.visualizar_circuito()
"""

#Prueba 4: Nodos no existentes
#Objetivo: Detectar un error al agregar aristas con nodos que no existen.

"""
grafo1.agregar_arista("Mar del Plata", "Casa Rosada", 5, False)
grafo1.visualizar_circuito()
"""




#-----------------------------------------------------------#
#                          Grafo 2                          #   
#-----------------------------------------------------------#           
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



grafo2 = Grafo(edificios_importantes,nodos_secundarios,aristas)

#Prueba 1: Caso base
#Objetivo: ?.
"""

"""

#Prueba 2: Ruta segura para e-bikes (caminoMinimoAlumno)
#Objetivo: Encontrar la ruta mas corta entre el Planetario y la Facultad de Derecho, usando solo aristas marcadas como segura.

"""
print(grafo2.caminoMinimoAlumno("Planetario Galileo Galilei", "Facultad de Derecho"))
grafo2.visualizar_circuito()
"""


#Prueba 3: Peso de aristas negativo
#Objetivo: Detectar un error al usar valores negativos en el peso de las aristas.

"""
grafo2.agregar_arista("Teatro San Martín", "Facultad de Derecho", -1, True)
grafo2.visualizar_circuito()
"""


#Prueba 4: Nodos no existentes
#Objetivo: Detectar un error al agregar aristas con nodos que no existen.

"""
grafo2.agregar_arista("Facultad de Derecho", "Costa Salgero", 1, True)
grafo2.visualizar_circuito()
"""




