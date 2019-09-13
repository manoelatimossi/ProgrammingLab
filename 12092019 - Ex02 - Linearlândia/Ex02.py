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
  for keys in grafo.keys():
    for j in grafo[keys]:
        pesos_caminho[count] = grafo[keys][j]
        count = count + 1
  print(pesos_caminho)
  valor = 0
  x = 0
  for i in range(len(pesos_caminho)):
    valor = valor + pesos_caminho[x]
    x = x + 1
  return valor
print(caminho(linearlandia, '1'))
