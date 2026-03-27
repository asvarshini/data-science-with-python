class A:
    def __init__(self):
        global name,age
        self.name="Python"
        self.age=10
    def details(self):
        return name
class B:
    def __init__(self):
        global name,id
        self.name="Languag"
        self.id=33
    def details(self):
        return name
class C(A,B):#Inherit
    def __init__(self):
        A.__init__(self) #call the constructor A
    def get_details(self):
        return self.name
ob =C()
print(ob.get_details())
        
