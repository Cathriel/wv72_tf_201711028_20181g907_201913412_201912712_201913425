#El algoritmo divide y vencerás elaborado se encarga de que cada punto de entrega encuentre su camino hasta el punto de almacén, revisando sus nodos adyacentes. 
#El nodo adyacente que esté más cerca al punto de almacén sería elegido como padre, hasta llegar al punto de almacén.

#Para la versión final del algoritmo, se modificó el código, para que solo en el caso de que un nodo evaluado se encuentre una fila debajo de la fila del almacén,
#este pueda subir, a pesar de que la resta entre el punto de almacén y el nodo a evaluar sea negativa. De este modo, se evitaría un bucle infinito, y el nodo podría 
#encontrar su camino sin problema.

def dyc(G,g):
  n=len(G)
  puntosEntrega=[]
  resta=None
  puntoAlmacen=0
  nodoAdyacente=0

  filaAlmacen=0
  filaAdyacente=0

  for n in range (len(g)):
    if(g[n][-2]==1):
      puntosEntrega.append(g[n])
    if(g[n][-2]==2):
      puntoAlmacen=g[n][-1]
  
  filaAlmacen=(puntoAlmacen-(puntoAlmacen%nFilas))/nFilas

  for n in puntosEntrega:

    #print(n)
    
    resta = None
    
    while(resta!=0):
      
      if(puntoAlmacen>n[-1]):
        
        filaAdyacente=(n[-1]-(n[-1]%nFilas))/nFilas
        if(filaAlmacen-filaAdyacente==1):
          Path[n[-1]+nFilas]=n[-1]
          n=G[n[-1]+nFilas]
          continue
        
        for u in range(len(n)-2):
        

          if(resta is None):
            if(puntoAlmacen-n[u]<0):
              continue
            nodoAdyacente=n[u]
            resta=puntoAlmacen-nodoAdyacente

          elif(puntoAlmacen-n[u]<0):
            continue

          elif(resta>puntoAlmacen-n[u]):
            if(puntoAlmacen-n[u]<0):
              continue
            resta=puntoAlmacen-n[u]
            nodoAdyacente=n[u]
      else:

        filaAdyacente=(n[-1]-(n[-1]%nFilas))/nFilas
        if(filaAdyacente-filaAlmacen==1):
          Path[n[-1]-nFilas]=n[-1]
          n=G[n[-1]-nFilas]
          continue

        for u in range(len(n)-2):
          if(resta is None):
            if(n[u]-puntoAlmacen<0):
              continue
            nodoAdyacente=n[u]
            resta=nodoAdyacente-puntoAlmacen

          elif(n[u]-puntoAlmacen<0):
            continue

          elif(resta>n[u]-puntoAlmacen):
            if(n[u]-puntoAlmacen<0):
              continue
            resta=n[u]-puntoAlmacen
            nodoAdyacente=n[u]

      
      Path[n[-1]]=nodoAdyacente
      n=G[nodoAdyacente]
  print(puntoAlmacen)
