
class student:

    def  __init__(self,n,a):
        self.full_name=n
        self.age=a
    def get_age(self):
        return self.age
q=student("deva",21)
print(q.full_name)
print(q.get_age())
print(hasattr(q,"full_name"))
print(hasattr(q,"get_age"))
print(getattr(q,"get_age")())
"""
def name(n):
     print("hello i'm ",n)
name("deva")"""
    
        
