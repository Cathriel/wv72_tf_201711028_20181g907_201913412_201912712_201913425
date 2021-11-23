<h1 align="center"> Estrategia para Diferenciar los tipos de Nodos en el grafo</h1>
</br>

Para la realización de nuestro proyecto, usaremos 3 tipos de nodos que estarán repartidos dentro de la representación gráfica de nuestra matriz.
  - Nodo de intersección cualquiera
  - Nodo de entrega
  - Nodo de distribución o almacenes

<img align="center" src="https://c8.alamy.com/compes/rp3b1r/monton-de-bolas-de-colores-como-telon-de-fondo-el-sustrato-divertido-juguete-para-ninos-fondo-multicolor-rp3b1r.jpg" width="500px">

La estrategia a usar para poder diferenciar estos 3 tipos de nodos será usar una lista de adyacencia, la cual nos permitirá no solo ubicar la posición 
de los nodos sino también asignarle un valor que corresponda al tipo de nodo que este representa según el caso.

```
%%file points.exmp
1|2 2|1

0|1 2|1

0|1 1|3

```

Donde el primer valor refiere a donde se dirige al arista, miestras que el segundo valor define el tipo de nodo que representa. Por ejemplo, 0: nodo de intersección cualquiera,
1: nodo de entrega y 2: nodo de distribución o almacén.

Comnsideramos también que podemos mejorar la propueta a medida que implementemos el código, pero que hasta el momento ya tenemos una idea clara de como representar 
gráficamente nuestro grafo.
