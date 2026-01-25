#1018

N = int(input())
print(N)

Notas = [100,50,20,10,5,2,1]

resto = N

for nota in Notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")

#1021

N = float(input())

Notas = [10000,5000,2000,1000,500,200]

Moedas = [100,50,25,10,5,1]

Valor = int(round(N * 100))

print("NOTAS:")
for nota in Notas:
    qtd = Valor // nota
    Valor = Valor % nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
    
print("MOEDAS:")
for moeda in Moedas:
    qtd = Valor // moeda
    Valor = Valor % moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")

#1038

x, y = map(int, input().split())

if x == 1:
    price = 4.00
elif x == 2:
    price = 4.50
elif x == 3:
    price = 5.00
elif x == 4:
    price = 2.00
elif x == 5:
    price = 1.50

total = price * y

print(f"Total: R$ {total:.2f}")

#reels

nums = [1,2,3,4,5,6]

for n in nums[:]:
    if n % 2 == 0:
        nums.remove(n)
print(nums)