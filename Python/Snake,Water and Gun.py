import random
import math
print("---------------ROCK PAPER SISSOR------------------ ")
player = int(input("Enter \n0 FOR ROCK \n1 FOR PAPER \n2 FOR SISSOR : \n"))
p=-1
c=-1
#For Player
if player== 0:
    playerNum=0
    p="Rock"
elif player==1:
    playerNum=1
    p="Paper"
elif player==2:
    playerNum=2
    p="Sissor"
else:
    print("Invalid Input")
    
computer = math.floor((random.random()*100))
#FOR Computer
if computer<=34:
    compNum=0
    c="Rock"
elif computer>=34 and computer<=67:
    compNum=1
    c="Paper"
else:
    compNum=2
    c="Sissor" 
    
#Playing
if playerNum == compNum:
    print("Draw")
elif (playerNum==1 and  compNum==0):
    print("Winner")
elif playerNum==0 and compNum==1:
    print("Loser")
elif (playerNum==2 and  compNum==1):
    print("Winner")
elif playerNum==1 and compNum==2:
    print("Loser")
elif (playerNum==0 and  compNum==2):
    print("Winner")
elif playerNum==2 and compNum==0:
    print("Loser")    
print(f'YOU : {p} and Computer : {c}')