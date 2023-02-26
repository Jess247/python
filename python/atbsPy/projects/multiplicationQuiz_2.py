# This program will do the same as multiplication_Quiz.py without pyinputplus
import re
import random
import time

answerRegex = re.compile("\d")
numberOfQuestions = 10
correctAnswers = 0
wrongAnswers = 0

# TODO: Add Timer


def timer(seconds):
    while seconds > 0:
        seconds -= 1
        time.sleep(1)
    return None


for questionNumber in range(numberOfQuestions):
    # use random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    answer = input(f"{num1} x {num2} = ")
    if answerRegex.search(answer):

        if int(answer) == num1 * num2 and wrongAnswers < 3:
            correctAnswers += 1
            print("Correct!")
        elif wrongAnswers == 3:
            print("Out of tries!")
        else:
            wrongAnswers += 1
            print("Incorrect")
    else:
        print("You need to enter a number!")


print(f"Score: {correctAnswers}/{numberOfQuestions}")
