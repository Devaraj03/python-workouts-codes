n=5
for i in range(n):
    for j in range(i+1):
        print(i+1,end=" ")
    print("\n")
for i in range(n,0,-1):
    for j in range(i):
        print(i,end=" ")
    print("\n")
for i in range(n):
    for j in range(i,n):
        print(i,end=" ")
    print("\n")
