import pyttsx3
import time

ShoutOut=["Ankita","Pratyush","Arnab","Nibedita","Mamoni","Sumit"]
Awaz=pyttsx3.init()
for name in ShoutOut:
    Awaz.say("Choot Marani Bar Bar "+name)
    Awaz.runAndWait()
    time.sleep(1)