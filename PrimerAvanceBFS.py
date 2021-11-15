#Como primera version del algoritmo BFS se tiene el utilizado para el Issue 25 con unas pequeñas alteraciones

#Se ha propuesto este como primera versión, pero se quiere cambiar puesto que no es para nada eficiente
#teniendo en cuenta todos los pasos que hay que hacer anteriormente para realizarlo

def bfsForGroups(G,pos,qPuntosEntrega):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [pos]
  visited[pos] = True
  contador = 0

  while queue:
    u = queue.pop(0)
    for v in range(len(G[u])):
      if v<(len(G[u])-2) and not visited[G[u][v]]:
        visited[G[u][v]] = True
        parent[G[u][v]] = u
        a = G[u][v] 
        if G[a][-2] == 1:
          contador +=1
        if contador==qPuntosEntrega:
          return parent
        queue.append(G[u][v])

  return parent
