# 0 1 1 2 3 5 8 13

n1=0
n2=1
n=int(input("enter the range of number:"))
print(n1,n2,end=" ")
for i in range(2,n):
    sum=n1+n2
    n1=n2
    n2=sum
    print(sum,end=" ")
