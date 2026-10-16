class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        for i in nums:
            if i in d:
                d[i] +=1
            else:
                d[i]=1
        a=sorted(d, key=d.get,reverse=True)
        return a[:k]
nu =input("Enter the number :")
nums =list(map(int,nu.split()))
k=int(input("Enter the values of elemnt to return :"))
ob =Solution()
print(ob.topKFrequent(nums,k))