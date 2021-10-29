
def bfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True
  contador = 0

  while queue:
    u = queue.pop(0)
    for v in range(len(G[u])):
      if v<(len(G[u])-1) and not visited[G[u][v]]:
        visited[G[u][v]] = True
        parent[G[u][v]] = u
        a = G[u][v] 
        if G[a][-1] == 1:
          contador +=1
        queue.append(G[u][v])
      if contador== cantidadPuntosEntrega:
        return parent

  return parent
  
  
 #En el algoritmo, tenemos un contador, el cual va a aumentar hasta haber visitado todos los puntos de entrega y luego retornará la lista con los respectivos padres.
