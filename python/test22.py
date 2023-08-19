list1=["suresh",28]
list2=["rahman",27]
list3=[0]
list3[0]=list1[1]
list1[1]=list2[1]
list2[1]=list3[0]
print(list1)
print(list2)
def main():
     res=input(("enter 0 or 1: \n"))
     if res=="1":
         print(list1)
     elif res=="0":
         print(list2)
     repeat=input("do you want repeat again press 1 or 0: \n")
     if repeat =="1":
        print("OK")
        return main()
     else:
        print("bye")
        exit()
main()
 
