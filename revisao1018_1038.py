#1018

N = int(input())
print(N)

Notas = [100,50,20,10,5,2,1]

resto = N

for nota in Notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")

#1019

N = int(input())

hora = N // 3600
resto = N % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{hora}:{minutos}:{segundos}")

#1020

N = int(input())

ano = N // 365
resto = N % 365
mes = resto // 30
dia = resto % 30

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")

#1021

N = float(input())

resto = int(round(N * 100))

Notas = [10000,5000,2000,1000,500,200]

Moedas = [100,50,25,10,5,1]

print("NOTAS:")
for nota in Notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
    
print("MOEDAS:")
for moeda in Moedas:
    qtd = resto // moeda
    resto = resto % moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")

#1035
