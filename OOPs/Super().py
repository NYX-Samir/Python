class Employee:
    def __init__(self,Id,Name,Age):
        self.id=Id
        self.name=Name
        self.age=Age
        
    def detail(self):
        print(f'EmpId:{self.id}\nName:{self.name}\nAge:{self.age}\nEmail:{self.email}')
        
class Freelance(Employee):
    def __init__(self, Id, Name, Age,Email):
        super().__init__(Id, Name, Age)
        self.email=Email
        
Emp1 = Freelance(2033123,"Abdul Samir",23,"abdulsamir0786@gmail.com")
Emp1.detail()

