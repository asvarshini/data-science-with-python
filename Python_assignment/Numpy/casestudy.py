import numpy as np
arr=np.full((3,3),5)
print("Array which takes the tuple and arguments is \n",arr)
print("******ACCEPTING N ARRAY AND RETURNING SUM *******")
def sum_arrays(*arrays):
    return np.sum(arrays,axis=0)
a=np.array([1,2,3])
b=np.array([4,5,5])
c=np.array([6,7,8])
print("sum =",sum_arrays(a,b,c))
print("****************")
def top_left(arr3,n,m):
    return arr3[:2,:2]
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Top left of sub_matrix is \n",top_left(arr3,3,3))
print("*************************")
def solution(arr):
    return {
        'mean':float(np.mean(arr)),
        'std_dev':float(np.std(arr))
    }
print(solution(np.array([1,1,1])))
