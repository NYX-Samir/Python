# class Father: 
#     def Hair(self):
#         print("From Dad")

# class Mother:    
#     def Eyes(self):
#         print(f"From Mom")
        
# class Child(Father,Mother):
#     pass
#     #def Eyes(self):
#         #print("My OWN")
        

# child = Child()
# child.Hair()
# child.Eyes()

class Father: 
    def Hair(self):
        print("From Dad")

    def show(self):
        print("I m Dad's Child")

class Mother:    
    def Eyes(self):
        print(f"From Mom")
        
    def show(self):
        print("I m Mom's Child")
        
class Child(Father,Mother): # first parent class show it output
    pass
    #def Eyes(self):
        #print("My OWN")
        

child = Child()
child.Hair()
child.Eyes()
child.show() 
        