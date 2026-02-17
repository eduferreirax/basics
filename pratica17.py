#1035

A,B,C,D = map(int, input().split())

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

#1066

even = 0
odd = 0
pos = 0
neg = 0

for i in range(5):
    n = int(input())
    if n % 2 == 0:
        even += 1
    if n % 2 != 0:
        odd += 1
    if n > 0:
        pos += 1
    if n < 0:
        neg += 1

print(f"{even} valor(es) par(es)")
print(f"{odd} valor(es) impar(es)")
print(f"{pos} valor(es) positivo(s)")
print(f"{neg} valor(es) negativo(s)")