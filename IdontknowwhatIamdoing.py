from random import randint
from time import sleep
cheats = 0
points = 0
lives = 3
print("You entered a haunted house... ")
sleep(4)
print("if you chose the rong door were is a ghost ...")
sleep(5)
print("I think you know what they will do to you...")
sleep(5)
print("but if not they will kill you!")
sleep(4)
while lives > 0:
    doors = randint(1, 3)
    user = int(input(f"you have {lives}  lives choose the door: 1,2,3 "))
    if user == 1 or user == 2 or user == 3:
        if doors == user:
            lives -= 1
            if lives == 2:
                print("You lost your first life I know that you dont wont to open \
another door but if you will not the ghost will kill you anyway HA HA HA!")
                sleep(8)
            if lives == 1:
                print("Oh you lost another life you seriously do you understand that if you lost another live \
you will be deid but if you will be see you at hell HA HA HA HA  ")
                sleep(10)
            print(f"you lost one life you have {lives} lives")
        else:
            points += 1
            print(f"you won a point you have {points} points")
    else:

        cheats += 1
        if cheats == 2:
            print("you are deid ha ha ha")
            break
        print("if you will cheat another gain say by by to your life ")
