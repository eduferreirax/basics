#1008 

X = int(input())
Y = int(input())
Z = float(input())

NUMBER = X

SALARY = Y * Z

print(f"NUMBER = {NUMBER}")
print(f"SALARY = U$ {SALARY:.2f}")

#1009

name = str(input())
salary = float(input())
total_sold = float(input())

bonus = total_sold * 0.15

total = salary + bonus

print(f"TOTAL = R$ {total:.2f}")


#1040

N1, N2, N3, N4 = map(float, input().split())

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    N5 = float(input())
    print(f"Nota do exame: {N5:.1f}")

    media_final = (media + N5) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_final:.1f}")