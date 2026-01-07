N = int(input())
print(N)

Notas = [100,50,20,10,5,2,1]

resto = N

for nota in Notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")