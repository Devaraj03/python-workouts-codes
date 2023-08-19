#check odd or even number
"""input=int(input("enter the input from user:\n"))
for input in value():
    if input%2==0:
          print(" it is even number...!")
    else:
          print(" it is a odd number...!")
"""
#check vowels
"""
c=input("enter the sentences:\n")
print(c)
if c=='a' or c=='e' or c=="i" or c=="o" or c=="u" or c=="A" or c=="E" or c=="I" or c=="O" or c=="U":
    print("this is a vowels char...!")
else:
    print("this is a normal char...!")"""
#check three number which is bigger
"""a=int(input("enter the first value: "))
b=int(input("enter the second value: "))
c=int(input("enter the third value: "))
if a>b and a>c:
    print("a is big")
elif b>a and b>c:
    print("b is big")
else:
    print("c is big")"""

#check three number which is small
def main():
    a=int(input("enter the first value: "))
    b=int(input("enter the second value: "))
    c=int(input("enter the third value: "))
    if a<b and a<c:
        print("a is small")
    elif b<a and b<c:
        print("b is small")
    else:

        print("c is small")
    repeat=input("do you want repeat again:\n")
    if repeat == "yes":
        main()
    else:
        print("bye")
        exit()
main()
# 1 2 3 4 5 6 7 8 9 
"""f=10
n=1+f
for i in range(1,n):
    print(i)"""
"""n=5
for i in range(n):
    print("",end="")
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(n):
    print("",end="")
    for j in range(n-i):
        print("*",end="")
    print()"""
"""for i in range(n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("")
for i in range(n):
    for k in range(i+2):
        print(" ",end=" ")
    for y in range(n-1-i):
        print("*",end=" ")
    print("")"""
#calculator
"""
def main():
   a=int(input("enter the first num:\n"))
   b=int(input("enter the second num:\n"))
   operator=input("selet operator(+,-,*,/):\n")
   if operator =="+":
      c=a+b
      print("add: ",c)
   elif operator =="-":
      c=a-b
      print("minus: ",c)
   elif operator == "*":
      c=a*b
      print("multiply: ",c)
   elif operator == "/":
      c=a/b
      print("division: ",c)
   repeat=input("yes(1) or no(0):\n")
   if repeat=="1":
      main()
   else:
       exit()
main()"""

"""list=[1,2,3,4,5,6]
list.append(2)
list.remove(2)
remove.list[2]
print(list)"""
#def basic addition
"""def main(a,b):
   sum=a+b
   return sum
a=int(input("the first value is:\n"))
b=int(input("the secon value is:\n"))
print("the addition value is: ",main(a,b))"""

"""n="uidjwijdewd"
for i in (n):
   print(i,end="")"""
class student:
   def __init__(self,name,age):
      self.name=name
      self.age=age
      print("inside constructor")
      print("constructor")
   def show(self):
      print("hello my name is ",self.name)
   def sefa(self):
      print("safe the place",self.age)

s1=student("deva",28)
s1.show()
s1.sefa()
del s1



         
