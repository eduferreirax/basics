N = int(input())
print(N)

notas = [100,50,20,10,5,2,1]

resto = N

for nota in notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")

    #round2 01/04/2026

N = int(input())

hora = N // 3600
resto = N % 3600
minuto = resto // 60
segundo = resto % 60

print(f"{hora}:{minuto}:{segundo}")
