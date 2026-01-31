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

#1043

a, b, c = map(float, input().split())

soma1 = b + c
soma2 = a + b
soma3 = a + c

if(a < soma1 and b < soma3 and c < soma2):

    perimetro = a + b + c

    print("Perimetro = {0:.1f}".format(perimetro))

else:

    area = ((a + b) * c) / 2

    print("Area = {0:.1f}".format(area))

#1044 

A, B = map(int, input().split())

if (A % B == 0) or (B % A == 0):
    print("Sao Multiplos")
    
else:
    print("Nao sao Multiplos")

#1045

A, B, C = map(float, input().split())
a, b, c = sorted([A, B, C], reverse=True)

# 1) Primeiro: verifica se forma triângulo
if a >= b + c:
    print("NAO FORMA TRIANGULO")
else:
    # 2) Tipo pelo ângulo (usa quadrados)
    a2, b2, c2 = a*a, b*b, c*c

    if a2 == b2 + c2:
        print("TRIANGULO RETANGULO")
    elif a2 > b2 + c2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    # 3) Tipo pelos lados
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")
