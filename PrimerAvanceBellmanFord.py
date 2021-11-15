def bellmanFord(G, s):
  n = len(G)

  # Iniciamos los valores iniciales de los arcos (calles), asi como los predecesores de cada nodo.
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n

  # Relajamos para sacar el camino con menos peso.
  for _ in range (n-1): 
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          path[v] = u

  #Verificamos que no haya ciclos negaivos.
  for u in range(n):
    for v, w in G[u]:
      if cost[u] + w < cost[v]:
        return None, None
  
  return path, cost
