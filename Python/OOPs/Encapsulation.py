#Public
'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
    def details(self):
        print(f"Name:{self.name}")
        print(f"salary:{self.salary}")
        
        
Emp= Employee("Arnab",23000)
Emp.details()
'''
#protected
'''
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
        
    def details(self):
        print(f"Name:{self.name}")
        print(f"salary:{self._salary}")
        
        
Emp= Employee("Arnab",23000)
print(Emp._salary)
Emp.details()
'''
#private

class Employee:
    def __init__(self,name,salary):
        self.__name=name
        self.__salary=salary
        
    def details(self):
        print(f"Name:{self.__name}")
        print(f"salary:{self.__salary}")
        
        
Emp= Employee("Arnab",23000)
Emp.details()
print(Emp.__name)
print(Emp.__salary)