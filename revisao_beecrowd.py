#1038

x,y = map(int, input().split())
if x == 1:
    price = 4.00
if x == 2:
    price = 4.50
if x == 3:
    price = 5.00
if x == 4:
    price = 2.00
if x == 5:
    price = 1.50

Total = price * y

print(f"Total: R$ {Total:.2f}")