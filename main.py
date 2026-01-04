#Beecrowd day 01

#Begginner 1000

print("Hello World!")

#End of code

#Begginer 1001

A = int(input())
B = int(input())

X = A + B

print(f"X = {X}")

#End of code

#Python 03/01/2026

A = int(input("Qual o primeiro numero?"))
B = int(input("e o segundo?"))

if A > B:
    print("A é Maior!")

elif A < B:
    print("B é Maior!")

else:
    print("Sao iguais!")

#02

A = int(input())

if A % 2 == 0:
    print("A eh par!")
else:
    print("A eh impar!")

#03

# -*- coding: utf-8 -*-

n=input().split()

A=int(n[0])
B=int(n[1])
C=int(n[2])
D=int(n[3])

if (((B>C) and (D>A)) and ((C+D)>(A+B)) and ((C>0) and (D>0)) and (A % 2==0)):
     print("Valores aceitos")
else:
     print("Valores nao aceitos")

#day 04/01/2026
A = int(input())
B = int(input())
   
Distancia = (A * B)
litros = (Distancia / 12)
print(f"{litros:.3f}")

#02 Loops

N = int(input())
print(N)

notas = [100,50,20,10,5,2,1]

resto = N

for nota in notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")

