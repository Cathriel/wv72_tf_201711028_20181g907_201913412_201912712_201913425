#Para este segundo avance, se modificó el código, de manera que cada punto de entrega encuentre de manera individual su camino hasta el punto de almacén, 
#revisando sus nodos adyacentes. El nodo adyacente que esté más cerca al punto de almacén será elegido como padre, y así se iría aproximando nodo por nodo 
#hasta llegar finalmente al punto de almacén.

def dyc(G,g):
  n=len(G)
  puntosEntrega=[]
  resta=None
  contador=0
  puntoAlmacen=0
  nodoAdyacente=0
  path=[-1]*n

  for n in range (len(g)):
    if(G[n][-2]==1):
      puntosEntrega.append(G[n])
    if(G[n][-2]==2):
      puntoAlmacen=G[n][-1]

  for n in puntosEntrega[:1]:
    while(resta!=0)
      if(puntoAlmacen>n[-1])
        for u in range(len(n)-2):
          if(resta is None):
              nodoAdyacente=n[u]
              resta=puntoAlmacen-nodoAdyacente
          elif(resta>puntoAlmacen-n[u]):
            resta=puntoAlmacen-n[u]
            nodoAdyacente=n[u]
      else:
        for u in range(len(n)-2):
          if(resta is None):
              nodoAdyacente=n[u]
              resta=nodoAdyacente-puntoAlmacen
          elif(resta>n[u]-puntoAlmacen):
            resta=n[u]-puntoAlmacen
            nodoAdyacente=n[u]

      path[n[-1]]=nodoAdyacente
      n=G[nodoAdyacente]
