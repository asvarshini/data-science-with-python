class parent_class:
    global num
    num =10
class child_class(parent_class):
    def display(self):
        print("num=",num)
ob=child_class()
ob.display()