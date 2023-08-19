def biggest(a,b,c):
    if a>b:
       if a>c:
        return a
       else:
        return c
    else:
        if b>c:
         return b
        else:
         return c
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the b value:"))
big=biggest(a,b,c)
print("the big number is:",big)

def lowest(a,b,c):
    if a<b:
       if a<c:
         return a
       else:
         return c
    else:
       if b<c:
         return b
       else:
         return c
a=int(input("enter the a value:"))
b=int(input("enter the b value:"))
c=int(input("enter the c value:"))
low= lowest(a,b,c)
print("the low number:",low)


