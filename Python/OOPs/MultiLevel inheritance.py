class Parent:
    def __init__(self):
        self.value="I m Parent"
    
    def show(self):
        print(f"{self.value}")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.value="I m Child"
        
class GrandChild(Child):
    def __init__(self):
        super().__init__()
        self.value="I m GrandChild"
        
grand=GrandChild()
grand.show()