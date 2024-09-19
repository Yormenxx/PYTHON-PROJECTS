import random

def roll():

    decision = input("Roll the dice ? / Yes / Not \n")


    while decision.lower() == "Yes".lower():

        dice1=  random.randint(1,6)
        dice2=  random.randint(1,6)

        print(f"The dice 1 is: {dice1}, the dice 1 is : {dice2}")

        decision = input("Do you wanna do it again  ?  Yes / Not \n ")


roll()