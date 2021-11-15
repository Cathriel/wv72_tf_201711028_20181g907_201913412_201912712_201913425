## Análisis preliminar de la complejidad del algoritmo Bellman-Ford.

Una posible solución al problema planteado de VRP, sería aplicar el algoritmo de Bellman-Ford para una entrega eficiente de los productos a todos los puntos correspondientes. 
Este algoritmo calcula el camino más corto de un nodo de origen (el punto del almacén) hasta los nodos de destino (los puntos de entrega) a través de los arcos que unen a los nodos en el camino (las calles), evitando ciclos negativos, que vendrían a representar calles de un solo sentido que enbuclan el camino del camión repartidor.

## Análisis asintótico
Para el análisis asíntotico de este algoritmo se tuvo que analizar el algoritmo implementado para poder así calcular el coste de tiempo de este. 

![](https://i.imgur.com/cbXH1L4.png)

El Algoritmo de Bellman-Ford es un algoritmo que relaja todas las aristas, y lo hace la cantidad de vértices presentes en el grafo menos 1, lo que daría un tiempo asintótico de O(ve).
