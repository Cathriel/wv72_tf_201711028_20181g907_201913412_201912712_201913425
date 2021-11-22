#Para esta segunda versión del algoritmo de Dijkstra para darle una solución al VRP, se han contabilizado los puntos de de entrega y puntos de distribución (inicio) que se encuentran en el 
#área designada para así encontrar el camino más óptimo para llegar de estos almacenes a los puntos de entrega más cercanos a estos.
import heapq as hq
import math



def dijkstra(G, s):
  
  #Inicalización del algoritmo
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  
  # Contamos la cantidad de puntos de entrega del área asignada
  puntosEntrega = 0
  for u in range(len(G)):
    for v in range(len(G)):
      if G[u][v] == 2: #Puntos de entrega representados por "2"
        puntosEntrega += 1
  
    # Contamos la cantidad de puntos de entrega del área asignada
  almacenes = 0
  for u in range(len(G)):
    for v in range(len(G)):
      if G[u][v] == 3: #Puntos de entrega representados por "3"
        almacenes += 1
  
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))

  #De momento sólo se tomará en cuenta el path, en nuestro caso el cost será omitido al tratarde de calles perfectas.
  return path, cost
