import pyinputplus as pyip
response = pyip.inputNum(prompt="Enter a number, please.\n")
print("You entered the number: ", response)

# input range mith arguments min, max greaterThan and lessThan
response = pyip.inputNum("Enter num: ", min=4)
print("You entered a number thats minimum 4: ", response)
response = pyip.inputNum("Enter num: ", greaterThan=4)
print("You entered a number thats greater than 4: ", response)
response = pyip.inputNum("Enter num: ", min=4, lessThan=6)
print("You entered a number thats greater than 4: ", response)

# allow blank values input is optional
response = pyip.inputNum(blank=True)
print(response)
