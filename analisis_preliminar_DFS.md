# Análisis preliminar de algoritmo DFS

¿Que cual es la definición de DFS?, su definición es ‘Depth First Search’.

Para abarcar el problema presentado en el espacio de búsqueda propuesto, primero tenemos que identificar qué tipo de camión está saliendo del almacén, si es un camión de tipo A o B porque según esta información obtenida definiremos cuantos puntos de entrega alrededor del almacén va a cubrir el camión. Además, de obtener el costo por los puntos de entrega cubiertos.
Una vez se tenga el tipo de camión y los puntos de entrega que va a recorrer el camión se puede crear el grafo o grupo de nodos que recorrerá el algoritmo DFS (también conocido como búsqueda a profundidad).

![Grafo](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/blob/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/Grafo.png)

Luego se aplicará a DFS al grafo creado tomando como nodo de inicio el almacén, además, se guardará la distancia entre nodo y nodo utilizando las coordenadas ‘X’ y ‘Y’. Esta información ira junto al orden de retorno del algoritmo con el fin de obtener el costo por cubrir los puntos de entrega del grafo.

![Resultado final](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/blob/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/Analisis-DFS.png)

Logrando el objetivo final, que todos los puntos de entrega estén de color verde, significando que un camión paso por el punto y realizo la entrega.
