Topic | Desc
-|-
Autor | Daniel Santillán
Técnica principal | Backtracking


<div align="center">
  <h1>POSIBLE ANÁLISIS ASÍNTOTÍCO - ALGORITMO BACKTRACKING</h1>
</div>

<p>
<div align="center">
  <img src="https://www.mdpi.com/algorithms/algorithms-12-00045/article_deploy/html/images/algorithms-12-00045-g001.png" alt="vrp" width="500" text-align="center"/>
</div>
</p>


Este algoritmo, también conocido como vuleta atrás, se usa con el objetivo de encontrar soluciones para algún problema en cuestión. Estas soluciones sulen darse de forma parcial a medida se progresa en el recorrido, en busca de la solución final. Para ello deberá comprobar, en cada paso, si los movimientos son correctos hasta que se detecta un fallo, entonces se regresa por el mismo camino en el que vino para seguir buscando la ruta adecuada.

Por lo general este algoritmo suele ser un poco ineficiente en ciertos casos, debido a que prueba todas las combinaciones posibles para llegar a la solución final. En la forma más básica de este algoritmo, su Big O es de O(n<sup>2</sup>)

A continuación un breve psudocódigo general del algoritmo backtracking:

  `Backtracking
  
    Backtracking (a, k)
      Si EsSolucion(a, k) entonces
        ProcesarSolución(a)
      Sino 
        Por cada EncontrarSoluciones(a, k) hacer
          Backtracking(a, k+1)
          
        
## Aplicando el Algoritmo de Backtracking a la solución propuesta    

1. Definir el grafo donde se va a trabajar con el algoritmo
2. Determinar los agentes que van a afectar el desarrollo del algoritmo
3. Implementar una primera versión del algoritmo a fin de precisar el coste de memoria y el análisis de tiempos
