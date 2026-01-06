#revisao 01/06/2026


N = int(input())

ano = N // 365
resto = N % 365
mes = resto // 30
resto = resto % 30
dia = resto 

print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{dia} dia(s)")

#codigo novo hoje 01/06 beecrowd Snacks:

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



