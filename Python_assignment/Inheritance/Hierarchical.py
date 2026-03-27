# Parent class
class Parent:
    def fun1(self):
        print("This is the message from the Parent class")

# Child1 inherits from Parent
class Child1(Parent):
    def fun2(self):
        print("This is the message from Child1")

# Child2 also inherits from Parent
class Child2(Parent):
    def fun3(self):
        print("This is the message from Child2")
# Objects of Child1 and Child2
obj1 = Child1()
obj2 = Child2()

obj1.fun1()  # inherited from Parent
obj1.fun2()  # own method

obj2.fun1()  # inherited from Parent
obj2.fun3()  # own method