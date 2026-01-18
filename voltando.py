#1018

N = int(input())
print(N)

notas = [100,50,20,10,5,2,1]

resto = N

for nota in notas:
    qtd = resto // nota
    resto = resto % nota
    print(f"{qtd} nota(s) de R$ {nota},00")