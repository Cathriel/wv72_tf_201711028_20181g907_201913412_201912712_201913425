def DBP(a,b):
  x1, y1=a
  x2, y2=b
  return abs(x1-x2)+ abs(y1-y2)

group = [-1]*len(pointsEntrega)
group2 = [-1]*len(extraPoints)

for i in range(len(pointsEntrega)):
  m=0
  d = DBP(pointsEntrega[i],pointsAlmacenes[0])
  for j in range(len(pointsAlmacenes)):
    d2 = DBP(pointsEntrega[i],pointsAlmacenes[j])
    if d2 <d:
      d = d2
      m = j
  group[i]=m

for i in range(len(extraPoints)):
  m=0
  d = DBP(extraPoints[i],pointsAlmacenes[0])
  for j in range(len(pointsAlmacenes)):
    d2 = DBP(extraPoints[i],pointsAlmacenes[j])
    if d2 <d:
      d = d2
      m = j
  group2[i]=m
  
  
  nodesGroups = list()
for i in range(len(pointsAlmacenes)):
  toAdd=list()
  for j in range(len(group)):
    if group[j]==i:
      entrega = pointsEntrega[j][0]+pointsEntrega[j][1]*nFilas
      toAdd.append(nodos[entrega])
  for j in range(len(group2)):
    if group2[j]==i:
      entrega = extraPoints[j][0]+extraPoints[j][1]*nFilas
      toAdd.append(nodos[entrega])
  nodesGroups.append(toAdd)
