#1042

x, y, z = map(int, input().split())

lista_original = x, y, z

lista_ordenada = sorted(lista_original)

for v in lista_ordenada:
    print(v)

print()

for v in lista_original:
    print(v)

#1041

x, y = map(float, input().split())

if x == 0 and y == 0:
    print("Origem")
if x > 0 and y > 0:
    print("Q1")
if x > 0 and y < 0:
    print("Q4")
if x < 0 and y > 0:
    print("Q2")
if x < 0 and y < 0:
    print("Q3")
    
if x != 0 and y == 0:
    print("Eixo X")
if x == 0 and y != 0:
    print("Eixo Y")