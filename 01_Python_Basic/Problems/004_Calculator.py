#simple calculator
print("WELCOME TO SIMPLE CALCULATOR")

a=int(input("Enter the first number:"))
b=int(input("Enter the Second number:"))

print(" 1.Addtion  \n 2. Subtract \n 3.Multiplication \n 4. Division \n 4.Exit")
choice=input("Enter Your option(1/2/3/4/5) :")
if(choice=="1"):
    print("Addition =",a+b)
elif(choice =="2"):
    print('Sbtraction =',a-b)
elif(choice=="3"):
    print("Multiplication =",a*b)
elif(choice== "4"):
    if(b!=0):
        print("Division =",a/b)
    else:
        print("Cannot divided by Zero")
else:
    print("Invalid")
      



