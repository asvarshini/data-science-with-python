arr=[]
n=int(input("Enter the size of the array "))
i=0
while i<n:
    num=int(input("Enter the number "))
    arr.append(num)
    i=i+1
print(arr)
for num in arr:
    if num>1:
        for j in range(2,num):
            if num %j==0:
                print(f"{num} it is not a prime number")
                break
        else:
            print(f"{num} is a prime numbers")
    else:
     print(f"{num} it is not prime numbers")
    