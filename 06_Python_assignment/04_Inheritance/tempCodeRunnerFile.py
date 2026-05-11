# Parent class
class Parent:
    def fun1(self):
        print("This is fun1 from Parent")

# Child1 inherits from Parent
class Child1(Parent):
    def fun2(self):
        print("This is fun2 from Child1")

# Child2 inherits from Parent
class Child2(Parent):
    def fun3(self):
        print("This is fun3 from Child2")

# Hybrid class inherits from Child1 and Child2 (multiple + multilevel)
class Hybrid(Child1, Child2):
    def fun4(self):
        print("This is fun4 from Hybrid")

# Object of Hybrid
obj = Hybrid()

obj.fun1()  # from Parent (via Child1 or Child2)
obj.fun2()  # from Child1
obj.fun3()  # from Child2
obj.fun4()  # from Hybrids