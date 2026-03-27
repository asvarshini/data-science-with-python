class Sub1:
    def first(self):
        print("Thise is the first function from fun1")
class sub2:
    def second(self):
        print("Thise is the second function from the Sub 2 class")
class Super(Sub1,sub2):
    def final(self):
        
        print("Thise message is from the Super clas")
ob= Super()
ob.first()
ob.second()
ob.final()