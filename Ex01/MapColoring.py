
grafo = {'a':['b','c','d'], 'b':['a','f'], 'c':['a'], 'd':['a','e'], 'e':['d','f'], 'f':['e','b']}



def color_nodes(graph):
  #Ordenar os vértices por ordem decrescente.
  vertices = sorted((graph.keys()), key=lambda x: len(graph[x]), reverse=True)
  colorido = {}

  for ver in vertices:
    cores_disponiveis = [True] * len(vertices) #Cria uma lista com todos os valores true do tamanho grafo
    for vizinho in grafo[ver]:
      if vizinho in colorido:
        cor = colorido[vizinho]
        print(cor)
        cores_disponiveis[cor] = False
    for cor, disponivel in enumerate(cores_disponiveis):
      if disponivel:
        colorido[ver] = cor
        break

  return colorido

print(color_nodes(grafo))