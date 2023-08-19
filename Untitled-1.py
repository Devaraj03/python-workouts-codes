n=5
for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(n-i):
        print("$",end=" ")
    print("\n")