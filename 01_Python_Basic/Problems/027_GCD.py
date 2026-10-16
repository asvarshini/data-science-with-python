a=int(input("Enter the value of a :"))
b=int(input("Enter the value of b :"))
while b!=0:
    a,b =b,a%b
print(a)