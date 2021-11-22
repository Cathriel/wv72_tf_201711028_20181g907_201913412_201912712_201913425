def backTraking(G, init):
  
  visited = [False]*n
  visited[init] = True
  parent = [None]*n
  cola = [init]

  while cola:
    u = cola.pop(0)
    for v in range(len(G[u])):
      nod = G[u][v]
      if v < (len(G[u]) - 2) and not visited[nod]:
        visited[nod] = True
        parent[nod] = u
        
        cola.append(G[u][v])

  return parent
