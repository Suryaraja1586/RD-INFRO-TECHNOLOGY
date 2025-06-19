def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def exp(a,b):
    return a**b
def mod(a,b):
    return a%b
def floorDiv(a,b):
    return a//b
def main():
    while True:
        print("************Basic Arithmetic Operations**************")
        print("1.Add Two Numbers")
        print("2.Substract Two Numbers")
        print("3.Multiply Two Numbers")
        print("4.Divide Two Numbers")
        print("5.Floor Divide Two Numbers")
        print("6.Exponentiation of Two Numbers")
        print("7.Modulus of Two Numbers.")
        choice=int(input("Enter Your Choice(1-7):"))
        if choice==1:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Addition is :",add(a,b))
        elif choice==2:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Substraction is :",sub(a,b))
        elif choice==3:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Multiplication  is :",mul(a,b))
        elif choice==4:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            if b==0:
                print("Number can't be divided by Zero!!")
            else:
                print("The Division  is :",div(a,b))
        elif choice==5:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Floor Division is :",floorDiv(a,b))
        elif choice==6:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Exponentiation is :",exp(a,b))
        elif choice==7:
            a=int(input("Enter No1:"))
            b=int(input("Enter No2:"))
            print("The Modulus is :",mod(a,b))
        else:
            print("Please Enter a Number between 1 to 7.")
if __name__=="__main__":
    main()
    