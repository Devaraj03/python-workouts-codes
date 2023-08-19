n=5
for i in range(n):
    for k in range(n-i):
        print("",end="  ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for k in range(i+2):
        print("",end="  ")
    for j in range(4-i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(-5,-i-1):
        print("*",end=" ")
    print()

