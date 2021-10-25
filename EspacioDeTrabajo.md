# Representación del espacio de trabajo:

Para definir el espacio de trabajo primero se hizo uso de la función random.randint de la librería numpy para que así nos de un entero al azar entre extremos indicados por nosotros, entre 50 y 100 para los almacenes y entre 2500 y 5000 para los puntos de entrega.
Con estos valores creamos arreglos de puntos haciendo uso de la misma función.

Posteriormente con el método DeleteEqualsAndSort el cual recibe como parámetro un arreglo, eliminamos los puntos repetidos en ambas listas (lista con puntos de entrega y lista con puntos de almacen)

Luego creamos una lista con todos los puntos llamada extraPoints, desde el (0,0) al (199,199) (en caso se haya establecido como numero de filas y columnas 200). Así mismo, se crea el método DeleteEqualsInExtraPoints, el cual se va a encargar de eliminar los elementos iguales en las listas anteriormente mencionadas y haciendo uso de la misma función procedemos a crear el arreglo de nodos.

## Arreglo de nodos
Para el arreglo de nodos se tomó en cuenta lo siguiente, el nodo 0 va a ser el punto (0,0) y va a ir contando desde izquierda a derecha. Para definir el número de nodo, hacemos uso de la siguiente función:

Número de nodo = (Fila en la que se encuentra) *(Numero de filas) + (Columna en la que se encuentra)

Otra regla que se cumple en los nodos es que estos están representados en una lista de adyacencia, donde el último elemento en esta nos indica que tipo de punto es:

- Punto cualquiera representado por un 0
- Punto de entrega representado por un 1
- Punto de almacén representado por un 2
