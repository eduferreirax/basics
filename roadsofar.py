#1008

number = int(input())
hours = int(input())
money = float(input())

salary = hours * money

print(f"NUMBER = {number}")
print(f"SALARY = U$ {salary:.2f}")

#1009

name = str(input())
salary = float(input())
sales = float(input())

bonus = sales * 0.15
total = salary + bonus

print(f"TOTAL = R$ {total:.2f}")

#1010

p1, q1, v1 = (input().split())
p2, q2, v2 = (input().split())

total = int(q1) * float(v1) + int(q2) * float(v2)

print(f"VALOR A PAGAR: R$ {total:.2f}")

#1018

n = int(input())
print(n)

resto = n

notas = [100,50,20,10,5,2,1]

for v in notas:
    qtd = resto // v
    resto = resto % v
    print(f"{qtd} nota(s) de R$ {v},00")

#1019

N = int(input())

resto = N

hours = resto // 3600
resto = resto % 3600
minutes = resto // 60
seconds = resto % 60

print(f"{hours}:{minutes}:{seconds}")

#1021

N = float(input())

Notas = [10000, 5000, 2000, 1000, 500, 200]
Moedas = [100, 50, 25, 10, 5, 1]

valor = int(round(N * 100))

print("NOTAS:")
for nota in Notas:
    qtd = valor// nota
    valor = valor % nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
    
print("MOEDAS:")
for moeda in Moedas:
    qtd = valor // moeda
    valor = valor % moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")

