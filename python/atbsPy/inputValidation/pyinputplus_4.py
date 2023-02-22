# custom input
import pyinputplus as pyip


def addUpToTen(numbers):
    numberList = list(numbers)
    for i, digit in enumerate(numberList):
        numberList[i] = int(digit)
    if sum(numberList) != 10:
        raise Exception("The digits mus add up to 10, not %s" %
                        sum(numberList))
        return int(numbers)  # returns the number as int


respomse = pyip.inputCustom(addUpToTen)
