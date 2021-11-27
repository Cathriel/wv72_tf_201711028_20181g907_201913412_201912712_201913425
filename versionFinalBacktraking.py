# Se utilizó la estrategia de recorrer los nodos priorizando los que están en el mismo nivel, para luego seguir bajando en profundidad.
# Además, se tomaron en cuenta algunas características de otros algoritmos aprendidos en clase
# En el peor de los casos, estaríamos hablando de un costo de O(n^2)


def backTraking(G, init):
  n = len(G)
  visited = [False]*n
  visited[init] = True
  parent = [None]*n
  cola = [init]

  pEntrega = 0
  # Se verifica la cantidad de puntos de entrega del grafo actual en donde se está trabajando
  for u in range(len(G)) :
    for v in range(len(G[u])) :
      if G[u][v] == 2 :
        pEntrega += 1
  cont = 0

  while cola:
    u = cola.pop(0)
    for v in range(len(G[u])):
      nod = G[u][v]
      if v < (len(G[u]) - 2) and not visited[nod]:
        visited[nod] = True
        parent[nod] = u 
        cola.append(G[u][v])
        if G[nod][-2] == 1 :
          cont += 1
      # Se comprueba si efectivamente se han recorrido todos los puntos de entrega
      if cont == pEntrega:
        return parent
      else :
        backTraking(G, G[u][v])
  return parent
