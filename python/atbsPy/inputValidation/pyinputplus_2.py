# arguments limit and timeout
# limit sets how many tries or seconds function will take to get the 'right' input
# if the user doesn't enter a valid input, an exception will be triggered

import pyinputplus as pyip
print("Try entering something other than a number.")
response = pyip.inputNum(limit=2)
print("Wait a bit before entering a number to see what timeout does.")
response = pyip.inputNum(timeout=10)

# return default value instead of an exception
print("Try entering something other than a number.")
response = pyip.inputNum(limit=2, default="N/A")
