# This program will do the same as multiplication_Quiz.py without pyinputplus
import re
import random
import time

answerRegex = re.compile("\d")
numberOfQuestions = 10
correctAnswers = 0
wrongAnswers = 0
timeLimit = 8
# Add Timer
startTime = time.time()

for questionNumber in range(numberOfQuestions):
    # use random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    answer = input(f"{num1} x {num2} = ")
    if answerRegex.search(answer):

        if int(answer) == num1 * num2 and wrongAnswers < 3 and time.time() - startTime < timeLimit:
            correctAnswers += 1
            print("Correct!")
        elif wrongAnswers == 3:
            print("Out of tries!")
        elif time.time() - startTime > timeLimit:
            print("You're out of tries")
        else:
            wrongAnswers += 1
            print("Incorrect")
    else:
        print("You need to enter a number!")


print(f"Score: {correctAnswers}/{numberOfQuestions}")
