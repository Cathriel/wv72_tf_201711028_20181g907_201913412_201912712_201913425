# **Trabajo Final - Complejidad Algorítmica**

## **Universidad Peruana de Ciencias Aplicadas**

![Logo UPC](https://i.pinimg.com/474x/b8/8f/bd/b88fbdf185b322fb2e85757229192ff6--luis-christ.jpg)

### Integrantes:
- Heredia Moscoso, Lucía
- Kawamura Solis, Jorge
- Sánchez Chávez, Joaquín
- Santillán Ávila, Daniel

### **Descripción del problema**

Este trabajo consiste en resolver el problema de enrutamiento de vehículos, más conocido como VRP, en su versión para múltiples puntos de distribución. A menudo, este suele ser un problema bastante común en las empresas de reparto  de bienes y productos, pues lo que éstas buscan es encontrar la ruta de entrega más óptima tomando en cuenta diversos factores tales como el lugar de sus almacenes, la distancia entre sus almacenes hacia los diferentes puntos de entrega, así como también ciertos recursos como los vehículos a usar, el combustible, tiempo, etc.

Es por ello que este es un problema que, de ser resuelto, puede ser muy beneficioso para una empresa con estas características. Para este curso, se tratará de resolver este problema usando diferentes algoritmos aprendidos en clase.

Requerimientos:

Deben existir entre 50 y 100 puntos de entrega.
Deben haber entre 2500 y 5000 puntos de entrega.
La cantidad de vehículos es ilimitada
Cada almacén y cada punto de entrega debe estar referenciado por una posición X y Y.

Para la culminación del trabajo final, fueron realizados hitos constantes, los cuales serán detallados a continuación. En el primer hito, se creó el grafo para la ciudad de 1000x1000 cuadras. Además, establecimos dos arreglos que contengan todos los puntos de entrega y almacenes. En el segundo hito, se implementó el algoritmo BFS desde cada almacén a cada punto de entrega. Para el tercer hito, separamos el grafo en áreas, donde cada área tendría su propio almacén y varios puntos de entrega, según criterio de cercanía. Asimismo, se implementó el BFS, esta vez solo a los puntos cercanos de un almacén. Finalmente, se elaboró individualmente el algoritmo BFS, DFS, Backtracking, Divide y Vencerás y Dijkstra, los cuales tendrían el objetivo de encontrar un camino desde cada punto de entrega hacia su respectivo almacén.

