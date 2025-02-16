class Animal:
    def speak(self):
        print("Animal Speak")
        
class Mammal(Animal):
    def birth(self):
        print("Mammal Give Birth")
        
class Bird(Animal):
    def Lays(self):
        print("Bird Lays Eggs")
        
class Dog(Mammal,Bird):
    pass
        
pet1 = Dog()
pet1.speak()
pet1.birth()
pet1.Lays()