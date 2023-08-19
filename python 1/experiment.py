def main():
    print("WELCOME TO THE CALCULATOR...!")
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    select=input("Enter the operator (+,-,*,/): ")
    if select=="+":
        add=x+y
        print("The added value is: ",add)
        print("\n")
        return main()
    elif select=="-":
        min=x-y
        print("the minus value is: ",min)
        print("\n")
        return main()
    elif select=="*":
        mul=x*y
        print("the muliply value is:",mul)
        print("\n")
        return main()
    else:
        div=x/y
        print("the division value is: ",div)
        print("\n")
        return main()
main()