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

Media = (N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1) / 4

if Media >= 7.0:
    print("Aluno aprovado.")
if Media < 5.0:
    print("Aluno reprovado.")
if Media > 5.0 and < 6.9:
    print("Aluno em exame.")
elif Media > 5.0 and < 6.9: