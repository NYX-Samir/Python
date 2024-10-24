#the if-else statement is used for decision-making, allowing the program to execute certain code based on whether a condition is True or False.elif

age=int(input("Enter Your Age : "))
if age>=18:
    print("You can Vote")
elif age==0:
    print("Imposible")
elif age<=0:
    print("Invalid Age")
else:
    print("You cannot Vote")