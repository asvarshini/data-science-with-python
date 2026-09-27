print("***MULTIPLICATION TABEL *****")
n=int(input("Enter the number you want to multiplication tabel with "))
limt=int(input("Enter the limt you want "))
print(f"Multipliction table for number {n}")
print('*' *30)
for i in range(1,limt+1):
    
    print(f"{n } * {i} ={n*i}")
#or you will get in list
x=[n*i for i in range(1,limt+1) ]
print(x)