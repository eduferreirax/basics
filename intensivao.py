#1041

x, y = map(float, input().split())

if x == 0 and y == 0:
    print("Origem")
elif x > 0 and y > 0:
    print("Q1")
elif x > 0 and y < 0:
    print("Q4")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x != 0 and y == 0:
    print("Eixo X")
elif x == 0 and y != 0:
    print("Eixo Y")
    

#1042 

x, y , z = map(int, input().split())

input_original = [x, y, z]

input_ordenado = sorted(input_original)

for v in input_ordenado:
    print(v)

print()

for v in input_original:
    print(v)