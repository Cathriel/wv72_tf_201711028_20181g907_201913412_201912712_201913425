#Como primera propuesta, se ha pensando en dividir el arreglo de nodos en 4, tomando como punto central el almacén 
#(arriba-derecha del almacén,arriba-izquierda del almacén,abajo-derecha del almacén,abajo-izquierda del almacén).

def dyc(G,almacen):
  ur=[]
  ul=[]
  dr=[]
  dl=[]
  nodoAlmacen=almacen[-1]


  for v in range(len(G)):
    if(G[v][-1]>nodoAlmacen):
      n=G[v][-1]-G[v][-1]%1000
      n=nodoAlmacen%1000+n
      if(G[v][-1]<n):
        ul.append(G[v])
      else:
        ur.append(G[v])
        
    else:
      n=G[v][-1]-G[v][-1]%1000
      n=nodoAlmacen%1000+n
      if(G[v][-1]<n):
        dl.append(G[v])
      else:
        dr.append(G[v])
