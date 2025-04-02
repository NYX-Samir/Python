class Animal:
    def __init__(self,name):
        self.name=name
    
class Dog(Animal):
    def Display(self):
        print(f"Name:{self.name}")
        
class Cat(Animal):
    def Display(self):
        print(f"Name:{self.name}")
        
Pet1= Dog("Tony")
Pet1.Display()
print("")
Pet2= Cat("Billi")
Pet2.Display()


