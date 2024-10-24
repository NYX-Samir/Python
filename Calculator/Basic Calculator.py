operation = input("-----Menu-----\n1.+\n2.-\n3.*\n4./\nAns: ")
num1=int(input("Enter Your First number : "))
num2=int(input("Enter Your Second number : "))

if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("Invalid Operation")