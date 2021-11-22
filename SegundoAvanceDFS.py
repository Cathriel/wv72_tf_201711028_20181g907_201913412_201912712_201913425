#Se implementara DFS en su forma base tiniendo como parametro la parte del 
#grafo que lleva consigo 1 almacen y sus puntos de entrega respectivos, y en
#segundo parametro el nodo padre la coordenada del almacen el cual lo sacaremos
#con su valor de '2' que representa que el tipo de punto es almacen
def dfs(G, s):
  n = len(G)
  visited = [False]*n
  parent = [None]*n

  def _dfs(u):
    visited[u] = True
    for v in G[u]:
      if not visited[v]:
        parent[v] = u
        _dfs(v)

  _dfs(s)

  return parent
