import sys
ingresados=["a","b","c"]
lista=[]
permutacion=[]
permutaciones=[]
permutacionesf=[]
veces=[]

if len(lista)==1:
  print([[1]])
  sys.exit(0)
  
for i in range(len(ingresados)):
  lista.append(i+1)
for i in range(len(lista)):
  permutacion.append(1)
  
for a in range(len(lista)**len(lista)):
  permutacion = permutacion[:]
  permutacion[len(lista)-1]+=1
  
  while max(lista)+1 in permutacion:
    for b in permutacion:
      if b>max(lista):
        indice=permutacion.index(b)
        permutacion[indice]=1
        permutacion[indice-1]+=1
  
  for c in permutacion:
    veces.append(permutacion.count(c))
  
  if sum(veces)==len(lista):
    if permutacion not in permutacionesf:
      permutacionesf.append(permutacion)
  veces=[]

for d in range(len(permutacionesf)):
  for e in permutacionesf[d]:
    indice=permutacionesf[d].index(e)
    permutacionesf[d][indice]=ingresados[lista.index(e)]
    
print(permutacionesf)
