from heapq import heappop, heappush
from collections import defaultdict
INFTO = 20000000

def dijkstra(valor):
    dist[valor] = 0
    Fila= [(0, valor)]
    while Fila:

        custo, u = heappop(Fila)
        for i in range(len(vizinho[u])):
            viz = vizinho[u][i][0]
            peso = vizinho[u][i][1]
            if dist[viz] > dist[u] + peso:
                dist[v] = dist[u] + peso
                heappush(Fila, (dist[viz], viz))

V, E = map(int, input().split())
dist = [INFTO] * V
vizinho = defaultdict(list)

for _ in range(E):
    u, v, peso= map(int, input().split())
    u -= 1
    v -= 1
    vizinho[u].append((v, peso))
    vizinho[v].append((u, peso))

server = int(input()) - 1
dijkstra(server)
menor = INFTO
maior = -1

for u in range(len(dist)):
    d = dist[u]
    print(u+1, dist[u])
    if d != 0:
        menor = min(menor, d)
    if d != INFTO:
        maior = max(maior, d)

print(maior - menor)