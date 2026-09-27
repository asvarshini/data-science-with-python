print("================= CHECKING EVEN OR ODD ==========")
n =int(input("How many nuberes you want to check "))
numbers=[]
even=[]
odd=[]
for i in range(n):
    num=int(input("Enter the numers "))
    numbers.append(num)
    if num %2==0:
        even.append(num)
    else:
        odd.append(num)
print("Numbers =",numbers)
print("Even num ",even)
print("Odd num ",odd)
print(len(even))
print(len(odd))