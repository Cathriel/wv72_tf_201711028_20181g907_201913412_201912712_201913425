## Análisis preliminar de la complejidad del algoritmo Dijkstra.

Una posible solución al problema planteado de VRP, sería aplicar el algoritmo de Dijkstra para una entrega eficiente de los productos a todos los puntos correspondientes. 
Lo que hace el Algoritmo de Dijkstra es buscar el camino más corto según el peso de las aristas, o lo que vendría siendo en este caso, la distancia entre puntos de entrega para elegir cuál sería el siguiente punto de entrega para un camión repartidor en específico. Se obvia el hecho de que primero se tiene que determinar si el punto a ir ya fue visitado por otro camión repartidor o no, para evitar trabajo de visitar todas las aristas y hacer más eficiente el algoritmo.

##Análisis asintótico

Para el análisis asintótico de este algoritmo, se recurrió al Teorema Maestro para hallar el tiempo de ejecución en caso se aplique Dijkstra como solución al problema. El Teorema Maestro vendría a ser:

![](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/raw/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/Master%20Theorem.png?raw=true)

Aplicando este a Dijkstra, daría un tiempo asintótico de O(n^2).
