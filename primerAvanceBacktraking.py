# Para esta entrega se ha empleado el uso del algoritmo backtraking en versión básica. Primero identificamos la cantidad de todas los puntos de entrega para optimizar el proceso.
# Seguidamente recorremos el alegro, para ello elegí el criterio de recorrerlo entre nodos hermanos, tomando todas las posibilidades posibles.

def backTraking(G, init):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  colaP = [init]
  visited[init] = True

  pEntrega = 0

  for u in range(len(G)) :
    for v in range(len(G)) :
      if G[u][v] == 2 :
        pEntrega += 1

  cont = 0

  while colaP:
    u = colaP.pop(0)
    if 
    for v in G[u]:
      if not visited[v]:
        visited[v] = True
        parent[v] = u
        colaP.append(v)
        point = G[u][v]
        if G[point][-2] == 1 :
          cont += 1
      if cont == pEntrega:
        return parent

  return parent
