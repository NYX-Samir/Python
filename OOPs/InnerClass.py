class UG:
    def __init__(self):
        self.name = "UG"
        self.tec=self.Technology()
        self.med=self.Medical()
        self.degree="UG"
        
    def show(self):
        return print(f'Degree:{self.degree}')
    
    class Technology:
        def __init__(self):
            self.name="Abdul Samir"
            self.degree="UG"
            self.course ="B.Tech"
            
        def Display(self):
            print("Name:",self.name)
            print("Degree:",self.degree)
            print("Course:",self.course)
        
        
    class Medical:
        def __init__(self):
            self.name="Ankita Bhattacharya"
            self.degree="UG"
            self.course ="MBBS"
            
        def Display(self):
            print("Name:",self.name)
            print("Degree:",self.degree)
            print("Course:",self.course)

Education = UG()
Education.show()

Ed1 = Education.tec
Ed1.Display()

Ed2 = Education.med
Ed2.Display()

        