# Análisis preliminar de algoritmo Divide y Vencerás

Para la solución de este problema, se propone el algoritmo Divide y Vencerás. 
Para ello, primero se deberá tener en cuenta la capacidad de carga del camión, ya que cada tipo de camión podrá realizar un monto máximo de entregas distinta, 
lo que significa que recorrerán diferentes cantidades de puntos de entrega. Según ello, se analizarán los diversos caminos posibles desde el punto de origen del camión, 
teniendo en cuenta las distancias que cada uno implica, y aplicando el algoritmo para conseguir la ruta más óptima hasta lograr realizar todas las entregas.

## Análisis asintótico:

Para este caso, será necesario utilizar el Teorema Maestro, donde "a" vendría a ser el número de subproblemas por llamada recursivas, y "b" el tamaño de cada subproblema.

![](https://github.com/Cathriel/wv72_tf_201711028_20181g907_201913412_201912712_201913425/blob/main/Espacio%20de%20B%C3%BAsqueda%20Im%C3%A1genes/Master%20Theorem.png?raw=true)

Dependiendo de la manera en cómo se aborde el algoritmo Divide y Vencerás, el tiempo resultante sería O(n log n) o en todo caso, O(n).
