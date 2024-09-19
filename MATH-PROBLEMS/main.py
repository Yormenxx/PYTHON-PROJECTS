"""  PROYECTO QUE PERMITE REALIZAR CON EJERCICIOS MATEMATICOS ALEATORIOS"""
import random
import time

print("----------------------")
input("Press enter to start!")
print("----------------------")

MAX_VALUE = 20
MIN_VALUE = 1
OPERATORS = ["+", "-", "*"]
PROBLEMS = 2

def problemQuestions():


    leftStatement = random.randint(MIN_VALUE, MAX_VALUE)
    rightStatement = random.randint(MIN_VALUE, MAX_VALUE)
    operator = random.choice(OPERATORS)

    expression = str(leftStatement) + " " + operator + " " + str(rightStatement)

    answer = eval(expression)

    return expression ,answer

wrong = 0



start_time= time.time();

for i in range(PROBLEMS):

    expression, answer = problemQuestions()

    while True:

        guess = input("Problem # " + str(i + 1) + ": " + expression + " " + " = ")


        if guess == str(answer):
            break

        else:
            wrong += 1

print("total wrong = " , wrong)

end_time = time.time()

total_time = end_time + start_time





