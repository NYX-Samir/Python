# without walrus operator
# a= True           
# print(a=False)

#with walrus operator
a=True
print(a:=False)


# food=list()
# while (foo := input("What is Your Fav Food : ") !="quite"):
#     food.append(foo)

admin=["Me","Syntax"]

if Name := input("Enter Who Are You : ") in admin:
    print(f'Hello {Name}')
else:
    print("You Doesn't Have Access :[")    