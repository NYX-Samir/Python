#Parent
class Parent:
    def __init__(self):
        self.value="INSIDE PARENT"
        
    def show(self):
        print(f"{self.value}")
        
#child
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value="INSIDE CHILD"
        
    def show(self):
        print(f"{self.value}")
        
        
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()