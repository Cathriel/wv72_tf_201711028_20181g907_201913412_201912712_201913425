# **Trabajo Final - Complejidad Algorítmica**

## **Universidad Peruana de Ciencias Aplicadas**

![Logo UPC](https://i.pinimg.com/474x/b8/8f/bd/b88fbdf185b322fb2e85757229192ff6--luis-christ.jpg)

### Integrantes:
- Heredia Moscoso, Lucía U20181G907
- Kawamura Solis, Jorge U201913425
- Sánchez Chávez, Joaquín U201912712
- Santillán Ávila, Daniel U201913412
- Vásquez Solis, Luis U201711028

### **Introducción**

Como parte del curso de Complejidad Algorítmica se ha desarrollado el trabajo final con el propósito de poner en práctica los conocimientos adquiridos en el curso así como las competencias generales y específicas del mismo.

El trabajo ha sido desarrollado tanto de forma grupal, para lo cual se contado con la participación de todos los integrantes, así como también una parte individual en la cual se evidencia el conocimiento del integrante en la elaboración de un algoritmo aprendido en clase como parte de la solución para el problema propuesto en el trabajo final.

### **Descripción del Problema**

Este trabajo consiste en resolver el problema de enrutamiento de vehículos, más conocido como VRP, en su versión para múltiples puntos de distribución. A menudo, este suele ser un problema bastante común en las empresas de reparto  de bienes y productos, pues lo que éstas buscan es encontrar la ruta de entrega más óptima tomando en cuenta diversos factores tales como el lugar de sus almacenes, la distancia entre sus almacenes hacia los diferentes puntos de entrega, así como también ciertos recursos como los vehículos a usar, el combustible, tiempo, etc.

Es por ello que este es un problema que, de ser resuelto, puede ser muy beneficioso para una empresa con estas características. Para este curso, se tratará de resolver este problema usando diferentes algoritmos aprendidos en clase.

Requisitos:

- Deben existir entre 50 y 100 puntos de almacenes.
- Deben haber entre 2500 y 5000 puntos de entrega.
- La cantidad de vehículos es ilimitada
- Cada almacén y cada punto de entrega debe estar referenciado por una posición X y Y.

### **Desarrollo del problema**

Desde el primer hito del trabajo final comenzamos a trabajar para determinar nuestro grafo, así como los almacenes, puntos de entrega y los puntos extras que no representan ni almacenes ni puntos de entrega.

Creación de nuestros almacenes y puntos de entrega:

![code](https://i.imgur.com/HSrUXFE.png)

Representación gráfica de nuestro grafo, se aprecian los almacenes (rojo), puntos de entrega (azul) y puntos extras (verde):

![code](https://i.imgur.com/ChkwPD5.png)

División de grafos según cada punto de almacén:

![code](https://i.imgur.com/UEjCZy3.png)

Repartición de grafos en base al grafo general para cada uno de los integrantes del grupo:

![code](https://i.imgur.com/9pbb0XI.png)

En nuestro video de exposición se podrá explicar con mayor detalle, todo el proceso que hemos realizado para el desarrollo de nuestro trabajo final.

### **Trabajo compartido por Hitos**

Para la culminación del trabajo final, fueron realizados hitos constantes, los cuales serán detallados a continuación. En el primer hito, se creó el grafo para la ciudad de 1000x1000 cuadras. Además, establecimos dos arreglos que contengan todos los puntos de entrega y almacenes. En el segundo hito, se implementó el algoritmo BFS desde cada almacén a cada punto de entrega. Para el tercer hito, separamos el grafo en áreas, donde cada área tendría su propio almacén y varios puntos de entrega, según criterio de cercanía. Asimismo, se implementó el BFS, esta vez solo a los puntos cercanos de un almacén. Finalmente, se elaboró individualmente el algoritmo BFS, DFS, Backtracking, Divide y Vencerás y Dijkstra, los cuales tendrían el objetivo de encontrar un camino desde cada punto de entrega hacia su respectivo almacén.

### **Trabajo colaborativo evidenciado**

Para gestionar correctamente nuestro trabajo grupal se usó la plataforma de GitHub. En ella, nuestro trabajo está separado por milestones y estos a su vez por issues, los cuales fueron asignados a cada uno de los integrantes del grupo según la responsabilidad designada para cada uno. Esto contribuyó a desarrollar nuestra ética profesional y al trabajo colaborativo de forma ordenada y profesional.

![code](https://i.imgur.com/3dDu4Vn.png)

### **Conclusiones**

Con la realización del trabajo final del curso, el grupo llegó a las siguientes conclusiones:
- Este trabajo final ha sido de mucha utilidad para nuestro desarrollo como profesionales, y no solo en la parte del aprendizaje teórico y práctico, sino también en el aspecto del trabajo en equipo y la ética profesional.
- El desarrollo del problema propuesto ha sido importante para poner en práctica la capacidad de razonamiento cuantitativo, en donde se emitieron juicios de forma grupal, así como se tomaron decisiones trascendentales para el éxito del equipo. 
- Sabemos que este curso será de mucha utilidad en el futuro, tanto de nuestra carrera como en el campo laboral, por lo que se le ha puesto el interés necesario y eso se evidencia en el trabajo final.
- La programación se basa enteramente en práctica, y eso se ve reflejado conforme ha ido avanzando el proyecto; puesto que la complejidad de este ha ido aumentando.

### **Vídeo exposición**

Vídeo de la exposición grupal [aquí](https://youtu.be/gNImQSJ-7x4) 




