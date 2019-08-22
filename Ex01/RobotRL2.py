

print("Type 1 for walk forward, 0 to walk backward and type E to exit")
list = []
while(1):
 v = input()
 if v == 'E':
     break
 else:
  list.append(v)

print(len(list))

B = list.count('0')
F = list.count('1')
print(F - B)







