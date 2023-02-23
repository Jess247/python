# This program will do the same as multiplication_Quiz.py without pyinputplus
import re
import random
import time

answerRegex = re.compile("\d")
numberOfQuestions = 10
correctAnswers = 0
wrongAnswers = 0
# TODO: Add Timer

for questionNumber in range(numberOfQuestions):
    # us random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    answer = input(f"{num1} x {num2} = ")
    if answerRegex.search(answer) and answer == num1 * num2 and wrongAnswers < 3:
        correctAnswers += 1
        print("Correct!")
    else:
        wrongAnswers += 1
        print("Incorrect")
    if wrongAnswers == 3:
        print("Out of tries!")
    time.sleep(1)
print(f"Score: {correctAnswers / numberOfQuestions}")
