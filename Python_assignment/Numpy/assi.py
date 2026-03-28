import numpy as np
a=np.arange(2,11)
arr=a.reshape(3,3)
print("array with (3,3)from range (2,10) \n", arr)
convert_float=arr.astype(float)
print("int to float array=",convert_float)
original=[10,20,30]
original.extend([40,50,60,70,80,90])
print("added to orginal aray \n",original)
arr1=[1,2,3,4]
arr2=[5,6,7,8]
sum_array=arr1+arr2
print("sum array =\n",sum_array)
a2=np.arange(10,100,10)
arr2=a2.reshape(3,3)
print("array with (3,3)from range (10,90) \n", arr2)
print("First row in array is : \n ",arr2[0,:])
print(" last element in array : \n",arr2[2:3,2:3])
