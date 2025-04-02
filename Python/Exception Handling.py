try: 
    num1 = int(input("Enter Num 1 : "))
    num2 = int(input("Enter Num 2 : "))
    result = num1/num2
    print(result)
except ValueError:
    print( "Enter Valid Number")
    
except ZeroDivisionError:
    print("Num 2 Cannot be 0")
