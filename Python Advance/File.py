f = open("myfile.txt","w")
Fruits = ["Mango","Apple","Melon","Banana","Lichi"]
for Fruit in Fruits:
    f.writelines(Fruit+"\n")
f.close()
f = open('myfile.txt', 'r')
while True:
    Fruit = f.readline()
    if not Fruit:
        break
    print(Fruit)