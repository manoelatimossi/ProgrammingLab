grafo = {'a': {'b': 8, 'c': 5}, 'b': {'c': 2, 'd': 1}, 'c': {'b': 6, 'd': 10, 'e': 2}, 'd': {'e': 9}, 'e': {'d': 12}}


def dijkstra(grafo, comeco, fim):
    menor_distancia = {}
    anterior  = {}
    nao_visitados = grafo
    infinito = float('inf')
    caminho = []
    for ver in nao_visitados:
        menor_distancia[ver] = infinito
    menor_distancia[comeco] = 0

    while nao_visitados:
        menor_vertice = None
        for ver in nao_visitados:
            if menor_vertice is None:
                menor_vertice = ver
            elif menor_distancia[ver] < menor_distancia[menor_vertice]:
                menor_vertice = ver

        for ver_filho, peso in grafo[menor_vertice].items():
            if peso + menor_distancia[menor_vertice] < menor_distancia[ver_filho]:
                menor_distancia[ver_filho] = peso + menor_distancia[menor_vertice]
                anterior[ver_filho] = menor_vertice
        nao_visitados.pop(menor_vertice)

    atual = fim
    while atual != comeco:
            caminho.insert(0, atual)
            atual = anterior[atual]

    caminho.insert(0, comeco)
    if menor_distancia[fim] != infinito:
        print('Menor caminho: ' + str(menor_distancia[fim]))
        print('E o caminho é:' + str(caminho))
dijkstra(grafo, 'c', 'd')
