list=[10,23,4,26,475,24,54,44]
#using while loop feching even numbers
i=0
while i<len(list):
    if list[i]%2==0:  #if u only takes i then it do operation on index value
        print(f"{list[i]} present in the list is even")
    i=i+1
