#tuple
tuple1=(1,2,3,4)
tuple2=(9,8,7,6)
#combing tuple
t_combine=tuple1+tuple2
print("After the combination of two tuples",t_combine)
#t_combine to  repeate for three times
for i in range(1,4):
    print(f"{i} time{t_combine}")
print("acessing 3rd element is ",t_combine[2])
print(f"First three elements are : {t_combine[:3]}")
print(f"last three elements are : {t_combine[-3:]}")
#list
my_list=[
    (1,2,3),
    ("a","b","c"),
    (True, False)  
        ]

my_list.append((1,'a,True'))
print(f"mylist after append tuple={ my_list}")
my_list.append(["varshini",123])
print(f"mylist after append list ={my_list}")
#dictnory
my_dict={
    'fruits' :["Banana ","Apple","Orange"],
    'cost':[20,100,60]
}
keys=[]
values=[]
for key in my_dict:
    keys.append(key)
    values.append(my_dict[key])

print(f"Keys={keys}")
print(f"values ={values}")

#easy metond to print key and values
print("Second method")
print("keys",list(my_dict.keys ()))
print("values= ",list(my_dict.values()))
#Set
my_set={1,1,"a","a",True,True} #1,and True consider as same in python

print(my_set)
