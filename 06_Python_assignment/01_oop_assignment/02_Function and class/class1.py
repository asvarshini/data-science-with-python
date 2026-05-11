class student:
    def fun1(self,value):
        self.value=value
        return self.value
    def message(self):
        print("Value of a =",self.value )
n=int(input("Input any number :"))
ob =student()
ob.fun1(n)
ob.message()
#usage of lambda function
'''
* Basically lambda id small function[like we use compharsevie for if else ststment] 
8 it is used for small function escpsially when def need not to be used
*syntax variable =lambda arguments:operation
'''
#ex 1
add=lambda a,b:a+b
print(add(3,4))
print((lambda a,b:a+b)(9,9))
#lambda ussed in map()function
list=[1,2,3,4,5]
result=list(map())
