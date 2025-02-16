#duck Typing

# def add(a,b):
#     return a + b


# print(add(3,4))
# print(add([2,4],[5,6]))
# print(add("Hello ","Everyone"))
# print(add("Hello ",1)) create Error due to datatype

class Shape:
    def area(self):
        return "Undefined"
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        result = self.length*self.width
        print(result)
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        result = self.radius*2*3.14
        print(result)

rect = Rectangle(4,5)
circle = Circle(5)

rect.area()
circle.area()