# Parent class
class Parent:
    def fun1(self):
        print("This is the message from the fun1")

# Child1 inherits from Parent
class Child1(Parent):
    def fun2(self):
        print("This is the message from the fun2 ")

# Child2 inherits from Child1
class Child2(Child1):
    def fun3(self):
        print("This is the message from the fun3")
# Create object of Child2
obj = Child2()

# Call fun1 from Parent using Child2 object
obj.fun1()  # Inherited from Parent
obj.fun2()  # Inherited from Child1
obj.fun3()  # Defined in Child2