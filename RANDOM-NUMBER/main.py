import random


def guess(number):

    random_number = random.randint(1, number)
    x = 0
    attempts = 0

    while (x != random_number):

        x = int(input(f"choose a number between 1 and {number}: "))

        if(x < random_number):
            print("you are under the number")
            attempts +=1

        elif(x > random_number):
            print("you are above the number")
            attempts += 1

    print(f"congratulations you already find the number , attempts {attempts}")


guess(10)