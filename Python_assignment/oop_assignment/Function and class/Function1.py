#Factorial
def factor(n):
    if n==0:
        return 1
    else:
        return n*factor(n-1)
n =int(input("Enter the number you need to find the factor :"))
print(f"factorial of {n} is {factor(n)}")
#checkstring
def check_string(string):
    choice=int(input("Enter 1.with index postion know \n 2. without index postion is know"))
    if choice==1:
        i=0
        while i<len(string):
            if string[i]=='s':
                print(f"String contains letter s at position {i}")
                return
            i=i+1
        print("String does not contain letter S")
    elif choice ==2:
        if "s" in string:
            print("letter S is present in String")
        else:
            print("S is not present in string")
    else:
        print("Invalid input")
string=input("Enter the string :")
check_string(string)
#use lambda fun to double the number
num=[1,8,5]
double_num=list(map(lambda x:x*2,num))
print(double_num)
#check string is paalidrome or not
def pali(str):
    str= str.strip()
    rev_string=str[::-1]
    if str==rev_string:
        print("The given String is palidrome")
    else:
        print("The givem string is not palidrome")
n =input("Enter the  and string to check it is palidrome or not")
pali(n)