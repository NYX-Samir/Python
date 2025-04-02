class Car:
    #class attribute
    Year = 2012;
    def __init__(self,brand,Price):
        #instance Attribute
        self.price=Price
        self.brand=brand
    
    def Display(self):
        return print(f'brand : {self.brand} & Price : {self.price}')

#Object 
Car1 = Car("TATA","1CR")
print(Car1.brand)
print(Car1.Year)
Car1.Display()
