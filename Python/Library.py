class libraryManagement:
    def __init__(self,library=None):
        if library is None:
            self.library=[]
        else:
            self.library=library
    def display(self):
        if not self.library:
            print("Library is empty!")
        else:
            print("-----Library Books-----")
            for i in self.library:
                print(i)
    def addOn(self,book):
        self.library.append(book)
    def noOfBooks(self):
        print(len(self.library))
    
Lib = libraryManagement()
try:
    while True:
        print("----------library Management----------")
        print("0 For adding new book")
        print("1 For check how many books are in library")
        print("2 For check which books are available")
        print("3 For Exit")
        UserBook=int(input("Choose : "))
        if UserBook==0:
            BookName=str(input("Enter Your Book Name : "))
            Lib.addOn(BookName)
        elif UserBook==1:
            Lib.noOfBooks()
        elif UserBook==2:
            Lib.display()
        elif UserBook==3:
            break
        else:
            print("Invalid choice! Please enter a valid option (0-3).")

except ValueError:
    print("Invalid input! Please enter a number.")