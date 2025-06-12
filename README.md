# 📘 Informe del Trabajo Práctico Final – Programación Orientada a Objetos II

## 🎯 Objetivo del trabajo

El objetivo de este trabajo práctico es modelar un sistema de transporte con bicicletas eléctricas (e-bikes) en la Ciudad de Buenos Aires, usando grafos para representar las rutas y ubicaciones de interés. Se busca que los alumnos puedan viajar de forma segura entre edificios emblemáticos, puntos turísticos y sus hogares. Además, se contempla el uso de un camión de la UNO que redistribuye las bicicletas entre los edificios cuando es necesario.

## 🧩 Elementos del sistema

- **Nodos principales:** edificios históricos.
- **Nodos secundarios:** casas de alumnos y puntos turísticos.
- **Aristas:** caminos entre los nodos, con costo asociado y marcados como seguros o no para e-bikes.

## 🧠 Diseño e implementación

### 📦 Clase `Grafo`

Se creó una clase `Grafo` en Python, utilizando la librería `networkx`, para trabajar con estructuras de grafos y `matplotlib` para visualizar grafos.

#### 👷‍♂️ Atributos

- `edificios_principales`: lista de nodos considerados como edificios históricos.
- `lugares_secundarios`: lista de nodos secundarios como casas o puntos turísticos.
- `grafo`: objeto `Graph` de `networkx`.

#### 🔧 Métodos principales

- `agregar_nodo_principal(nombre)`: agrega un edificio histórico.
- `agregar_nodo_secundario(nombre)`: agrega un nodo turístico o casa.
- `agregar_arista(origen, destino, peso, segura)`: agrega un camino entre nodos con un costo y una marca de seguridad.
- `eliminar_nodo(nombre)`: elimina un nodo del grafo.
- `visualizar_circuito()`: genera una visualización del grafo con nodos, aristas y pesos.

---

### 🚴‍♂️ Ruta para alumnos (`caminoMinimoAlumno`)

Calcula la ruta más corta filtrando solo caminos seguros para e-bikes, mediante el algoritmo de Dijkstra. Si no hay ruta segura disponible, entonces se captura una excepcion NetworkXNoPath

---

### 🚛 Ruta del camión (`calcularRutaCamion`)

Se diseñó una solución que recorre todos los nodos principales (edificios) de forma eficiente teniendo en cuenta los nodos secundarios, lo que nos da como resultado un caminio minimo

---

## 🧪 Casos de prueba

La clase permite definir diferentes escenarios fácilmente, por ejemplo:

```python
g = Grafo(
    Principales=["Edificio A", "Edificio B", "Edificio C"],
    Secundarios=["Casa 1", "Turismo X"],
    Aristas=[
        ("Edificio A", "Edificio B", 5, True),
        ("Edificio B", "Edificio C", 4, True),
        ("Casa 1", "Edificio A", 3, False),
        ("Turismo X", "Edificio C", 2, True)
    ]
)

print(g.caminoMinimoAlumno("Casa 1", "Edificio C"))  # Ignora caminos inseguros
print(g.calcularRutaCamion())                        # Recorrido eficiente por edificios
g.visualizar_circuito()


```
