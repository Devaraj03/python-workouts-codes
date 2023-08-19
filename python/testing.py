n=4
for i in range(n):
    for j in range(n):
       if i==0 or i==n-1 or j==0 or j==n-1 or i==n-3:
          print("*",end=" ")
       else:
          print(" ",end=" ")
    print()
print("======================")

for i in range(n):
    for j in range(i+1):
        if i==n-1 or j==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("======================")

for i in range(n):
    for j in range(i+1):
        if i==j :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()        
