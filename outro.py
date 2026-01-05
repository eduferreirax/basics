#REVISAO DIA 05/01/2026

# Read a value of floating point with two decimal places. This represents  
# a monetary value. 
# After this, 
# calculate the smallest 
# possible number of notes and coins on which the value can be decomposed. 
# The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. 
# Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” 
# followed by the list of coins.

# Input
# The input file contains a value of floating point N (0 ≤ N ≤ 1000000.00).

# Output
# Print the minimum quantity of banknotes and coins necessary to change the initial value, as the given example.

# Input Sample	Output Sample
# 576.73

# #NOTAS:
# #5 nota(s) de R$ 100.00
# 1 nota(s) de R$ 50.00
# 1 nota(s) de R$ 20.00
# 0 nota(s) de R$ 10.00
# 1 nota(s) de R$ 5.00
# 0 nota(s) de R$ 2.00
# MOEDAS:
# 1 moeda(s) de R$ 1.00
# 1 moeda(s) de R$ 0.50
# 0 moeda(s) de R$ 0.25
# 2 moeda(s) de R$ 0.10
# 0 moeda(s) de R$ 0.05
# 3 moeda(s) de R$ 0.01

# N = float(input())
# valor = int(round(N * 100))

# Notas = [10000,5000,2000,1000,500,200]
# Moedas = [100,50,25,10,5,1]

# print("NOTAS:")
# for nota in Notas:
#     qtd = valor // nota
#     valor = valor % nota
#     print(f"{qtd} nota(s) de R$ {nota/100:.2f}")
# print("MOEDAS:")
# for moeda in Moedas:
#     qtd1 = valor // moeda
#     valor = valor % moeda
#     print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")


# A, B, C, D = map(int, input())

# if (B > C) and (D > A) and ((C + D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0):
#     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")


    #A, B, C, D = map(int, input().split())
#A, B, C, D = [int(input()) for _ in range(4)]

N = float(input())

valor = int(round(N * 100))

NOTAS = [10000,5000,2000,1000,500,200]

MOEDAS = [100,50,25,10,5,1]

print("NOTAS:")
for nota in NOTAS:
    qtd = valor // nota
    valor = valor % nota
    print(f"{qtd} nota(s) de R$ {nota/100:.2f}")

print("MOEDAS:")
for moeda in MOEDAS:
    qtd = valor // moeda
    valor = valor % moeda
    print(f"{qtd} moeda(s) de R$ {moeda/100:.2f}")