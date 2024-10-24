#the if-else statement is used for decision-making, allowing the program to execute certain code based on whether a condition is True or False.elif

age = int(input("Enter Your age :"))
if age>=18:
    print("You can Vote")
elif age==0:
    print("Invalid age")
elif age<=0:
        print("Invalid age")
else:
    print("You cannot Vote")