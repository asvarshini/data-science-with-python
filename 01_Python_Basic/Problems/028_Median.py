
q=input("Enter the list  :")
arr=list(map(int,q.split()))
m=0
        
arr.sort()
n=len(arr)

if n %2 !=0:
    m = arr[n //2]
else:
    m = (arr[n //2 -1]  + arr[n//2])/2
print(m)

