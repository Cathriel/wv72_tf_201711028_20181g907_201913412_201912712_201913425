# Version individual de BFS, que recibe como parametro el arreglo de todos los nodos, el arreglo individual que contiene el grupo de nodos
# y el punto de partida (almacen)
# La caracteristica principal de esta version de BFS es su llamado a una funcion externa, la cual como su nombre indica, verifica si el nodo
# al cual debe ir se encuentra dentro del arreglo individual de nodos.
def bfsIndividual(G,g, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [s]
  visited[s] = True

  while queue:
    u = queue.pop(0)
    for v in range(len(G[u])-2):
      if not checkIfIsThere(g,G[u][v]):
        continue
      if not visited[G[u][v]]:
        visited[G[u][v]] = True
        parent[G[u][v]] = u
        queue.append(G[u][v])
        
  return parent

def checkIfIsThere(nodesArray,node):
  for i in range(len(nodesArray)):
    if node==nodesArray[i][-1]:
      return True
  return False
