try:
    num=int(input("Enter Integer number : " ))    
except ValueError:
    print("Invalid Integer Num")
else:
    print("Integer Accepted")
finally:
    print("I will Always Excute")