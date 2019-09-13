linearlandia ={
                "1": {"2":10},
                "2": {"3":11},
                "3": {"4":12},
                "4": {"3":12},
                }
def caminho(grafo, inicio):
  visitado =[inicio]
  pilha = [inicio]
  while pilha:
      inicio = pilha[-1]
      if inicio not in visitado:
        visitado.append(inicio)
      remover = True
      for ver in grafo[inicio]:
       if ver not in visitado:
          pilha.append(ver)
          remover = False
          break
      if remover:
        pilha.pop()
  pesos_caminho = visitado
  count = 0
  print(pesos_caminho)
  for keys in grafo.keys():
    pesos_caminho[count] = grafo[keys].values()
    count = count +1
  return pesos_caminho
print(caminho(linearlandia, '1'))