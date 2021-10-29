#Desde cada coordenada de almacen se hara un BFS a todos los puntos de entrega

#Esto se realizara desde con la ayuda de un for
#Ya que, tenemos las coordenadas de los almacenes

for i in almacenes:
  print('Desde el nodo: ', i)
  bfs(nodos, i)

#Lo que sucedera es que el for recorrera las coordenadas de cada almacen
#realizando su respectivo BFS otorgando la lista de 'parents' de cada nodo
#de la ciudad
