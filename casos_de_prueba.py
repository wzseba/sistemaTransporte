import networkx as nx
import matplotlib.pyplot as plt
from reversion import Circuito_Ebike

#-----------------------------------------------------------#
#                          Grafo 1                          #
#-----------------------------------------------------------#

edificios_importantes = ["Casa Rosada","Catedral","Cabildo","Congreso","Teatro Colón","Edificio Kavanagh"]

lugares_secundarios = ["Casa1","Casa2","Casa3","Plaza de Mayo","Av de Mayo","Plaza San Martín"]

                
rutas = [("Casa Rosada","Cabildo",3,True),
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
           ("Av de Mayo","Congreso",6,True),
           ("Casa3","Plaza de Mayo",7,True)]

circuito1 = Circuito_Ebike(edificios_importantes,lugares_secundarios,rutas)



#caso_ruta_segura_para _e-bikes
#Objetivo: Encontrar la ruta mas corta entre el Planetario y la Facultad de Derecho, usando solo aristas marcadas como segura.

"""
print(circuito1.caminoMinimoAlumno("Planetario Galileo Galilei", "Facultad de Derecho"))
"""

#caso_peso_de_aristas_negativo
#Objetivo: Detectar un error al usar valores negativos en el peso de las aristas.

"""
circuito1.agregar_ruta("Casa1", "Congreso", -10, True)
"""

#caso_nodos_inexistentes
#Objetivo: Detectar un error al agregar aristas con nodos que no existen.

"""
circuito1.agregar_arista("Mar del Plata", "Casa Rosada", 5, False)
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

lugares_secundarios = [
    "Calle Corrientes", 
    "Avenida Santa Fe", 
    "Plaza Italia", 
    "Plaza Lavalle", 
    "Avenida Figueroa Alcorta",
    "Puerto Madero",
    "Parque Centenario"
]

rutas = [
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



circuito2 = Circuito_Ebike(edificios_importantes,lugares_secundarios,rutas)




#caso_agregar_nuevo_lugar
#Objetivo: Agregar un nuevo edificio a la lista de edificios principales y asegurarse de que siempre tenga una ruta

"""
circuito2.visualizar_circuito()
circuito2.agregar_ruta_y_edificio_principal("Teatro San Martín", "Facultad de C.Exactas", 4, True)
circuito2.visualizar_circuito()
"""

#caso_calcular_ruta_camion
#Objetivo: Calcular el camino mas corto que pase por todos los edificios principales
"""
print(circuito2.calcularRutaCamion())
"""

#caso_eliminar_lugar
#Objetivo: Verificar que el lugar se elimine correctamente
""""
circuito2.visualizar_circuito()
circuito2.eliminar_lugar("Teatro San Martín")
circuito2.visualizar_circuito()
"""





