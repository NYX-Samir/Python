#  F = C * (9/5) + 32 Celsius to Fahrenheit
# C = (F - 32) * 5/9 Fahrenheit to Celsius

convert=input("Menu\n1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius\nAns: ")
if convert=="1":
    C=int(input("Enter the temperature in Celsius : "))
    F = C * (9/5) + 32
    print(F)
elif convert=="2":
    F=int(input("Enter the temperature in Fahrenheit : "))
    C = (F - 32) * 5/9
    print(C)
else:
    print("Invalid Input")