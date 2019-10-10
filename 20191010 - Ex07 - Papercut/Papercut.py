n_retangulo = int(input())
alturas = []
alturas = [0 for i in range(n_retangulo)]
print(alturas)
for i in range(n_retangulo):
  alturas [i] = int(input())
qtd = 2 #Sempre sobra 2 pedaços, por isso quantidade começa com 2 (Quantidade mínima de pedaços)
for i in range(1, n_retangulo - 1):
  if alturas[i] < alturas[i-1] and alturas[i] < alturas[i+1]:
    qtd = qtd + 1
print(qtd)
