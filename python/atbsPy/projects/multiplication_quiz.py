# This program will aks a user to enter the result of a multiplication
# the user has 8 secomds to answer amd 3 tries
import pyinputplus as pyip
import random
import time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    # us random numbers
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = "#%s: %s x %s = " % (questionNumber + 1, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=["^%s$" % (
            num1 * num2)], blockRegexes=[(".*", "Incorrect!")], timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Out of time")
    except pyip.RetryLimitException:
        print("Out of tries")
    else:
        print("Correct!")
        correctAnswers += 1
    time.sleep(1)
print("Score: %s / %s" % (correctAnswers, numberOfQuestions))
