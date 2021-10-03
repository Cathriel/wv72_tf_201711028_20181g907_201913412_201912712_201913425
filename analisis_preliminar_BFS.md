# Análisis preliminar de algoritmo BFS (Breadth First Search)

Uno de los algoritmos propuestos para la posible solución del problema es el BFS o búsqueda en profundidad. Primero se identifica el punto del cual parte el camión, el cual es mostrado como el punto inicial en el espacio de búsqueda. Este punto es el más cercano al origen (0,0), así mismo es acertado mencionar que el algoritmo BFS no va a ser el más eficiente para el problema debido a su consumo de memoria

Teniendo en cuenta el punto de origen y las reglas establecidas por los camiones se procede a elaborar el algoritmo.

![](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/blob/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/BFS.png?raw=true)

## Análisis asintótico:

Teniendo en cuenta el estado más básico del algoritmo BFS, un while que termina cuando la cola de nodos este vacía, un for por cada nodo y un if que en caso un nodo no este visitado, este será agregado a la cola anteriormente mencionada.

Tanto la memoria como el tiempo son exponenciales a la profundidad de la solución O(b^n), siendo n la profundidad.

Así mismo se puede llegar a la conclusión que, este algoritmos nos puede ser beneficioso para encontrar los puntos en los cuales se encuentren los almacenes ya que buscamos en una misma profundidad.
Sin embargo, cuando se requiera llegar a los puntos de entrega más profunos, debido a temas de memoria el algoritmos no será muy eficaz.

![](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/blob/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/EstadoFinal.png?raw=true)
