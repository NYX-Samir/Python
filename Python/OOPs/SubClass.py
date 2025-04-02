class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
        
    def Type(self):
        return print(f'{self.type}')
    
class Dog(Animal):
    def Legs(self):
        print("4 Legs")

class Kangaroo(Animal):
    def Legs(self):
        print("2 Legs")
        
        
dog = Dog('Tony','Land')
kangaroo = Kangaroo('Boxer','Land')
print(dog.name,dog.type)
print(kangaroo.name,kangaroo.type)
dog.Legs()
kangaroo.Legs()
