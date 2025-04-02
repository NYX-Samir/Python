class Overloading:
    def Print(self,name=None):
        if name:
            print(f"Hello {name}")
        else:
            print(f"Hello")
            
greet = Overloading()
greet.Print("Samir")
greet.Print()
