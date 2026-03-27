class Super:
    def fun1(self):
        print("Thise is the func1 in superclass")
class modified_superclass(Super):
    def fun1(self):
        super().fun1()
        print("thise fun1 from modified_superclass")
    def fun2(self):
        print("Thise is fun2 from Modified super class")
    def hello1(self,n):
       print("Thise function is only have one argument")
    def sum(self, *num):# * it is used to accepet mutiple argument
        total = 0
        for i in num:
            total += i
        return total
ob=modified_superclass()

ob.fun1()
ob.hello1(1)
print("total :",ob.sum(10,20,30))
class Encapsulation:
    def __init__(self):
        self.a=10
    def value(self):
        return self.a
    def set_value(self,new_value):
        self.newvalue=self.a
        return self.newvalue
obb=Encapsulation()
print("valuse returng from value method",obb.value())
print("valuse returng from set_value method",obb.set_value(3))

