"""
def displayMsg(name):
    print("enter the name?",name)
    print("hi "+name)
displayMsg(name="jhon")
"""
"""
def add(a,b):
    print("the first value:",a)
    print("the second value:",b)
    print("added value:",a+b)
def min(a,b):
    print("the first value:",a)
    print("the second value:",b)
    print("minus value:",a-b)
def mul(b,a):
    print("the first value:",b)
    print("the second value:",a)
    print("multiple value:",b*a)
def div(a,b):
    print("divisible value:",int(a/b))
add(10,10)
min(10,5)
div(10,2)
mul(100,10)"""

class calci:
    def __init__(self,a,b):
        self.avalue=a
        self.bvalue=b
        print("inbuilt method")
    def add(self):
        print("the added value is: ",self.avalue+self.bvalue)
    def min(self):
        print("the minus value is : ",self.avalue-self.bvalue)
s1=calci(200,25)
s1.add()
s1.min()
