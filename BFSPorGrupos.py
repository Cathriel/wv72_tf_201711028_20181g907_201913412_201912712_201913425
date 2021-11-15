#Por motivos de prueba, se ha elegido el grupo de menor tamaño y se ha colocado en el arreglo "groupSelected"
groupSelected = list()
for i in nodesGroups:
  if len(groupSelected)==0:
    groupSelected=i
  else:
    if len(groupSelected)>len(i):
      groupSelected=i
      
#Luego de esto, se ordena de menor a mayor los nodos
for i in range(len(groupSelected)):
  j=i
  nToCompare =groupSelected[i][-1]
  while j<len(groupSelected)-1:
    j+=1
    mToCompare =groupSelected[j][-1]
    if n<m:
      groupSelected[i],groupSelected[j]=groupSelected[j],groupSelected[i]
      
#Se ha tomado la decisión de cambiar los nodos por su posición en el arreglo
toReplaced = 0
for i in range(len(groupSelected)):
  toReplaced=groupSelected[i][-1]
  for j in range(len(groupSelected)):
    for k in range(len(groupSelected[j])):
      if (k==len(groupSelected[j])-2):
        break
      else:
        if(groupSelected[j][k]==toReplaced):
          groupSelected[j][k]=i
          
#Debido a que cabe la posibilidad de que para un nodo x, sus nodos cercanos no se encuetren en el mismo grupo, esto se eliminaran

for i in range(len(groupSelected)):
  j=0
  while j <len(groupSelected[i]):
    if j==len(groupSelected[i])-2:
      break
    else:
      if groupSelected[i][j]>=len(groupSelected):
        del groupSelected[i][j]
        j-=1
    j+=1
    
#Se procede a crear la nueva versión del algoritmo BFS para que vaya acorde a los cambios hechos en los grupos de nodos 

def bfsForGroups(G, s,pos):
  n = len(G)
  visited = [False]*n
  parent = [None]*n
  queue = [pos]
  visited[pos] = True

  while queue:
    u = queue.pop(0)
    for v in range(len(G[u])):
      if v<(len(G[u])-2) and not visited[G[u][v]]:
        visited[G[u][v]] = True
        parent[G[u][v]] = u
        a = G[u][v] 
        queue.append(G[u][v])

  return parent

#Finalmente se busca el almacen en el grupo y se manda su posición en el arreglo
almacen = list()
pos = 0
for i in range(len(groupSelected)):
  if groupSelected[i][-2]==2:
    almacen=groupSelected[i]
    pos = i
    break
print(bfsForGroups(groupSelected,almacen[-1],pos))
