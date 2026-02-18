#1073

n = int(input())

for i in range(2, n+1, 2):
    print(f"{i}^2 = {i*i}")

#1074

n = int(input())

for i in range(n):
    x = int(input())
    
    if x == 0:
        print("NULL")
    
    elif x % 2 == 0:
        if x < 0:
            print("EVEN NEGATIVE")
        else:
            print("EVEN POSITIVE")
        
    else:
        if x > 0:
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")