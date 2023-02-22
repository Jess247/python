# use regex with input
# allowRegex and blockRegex accept a list of strings with regular
# expressions to check if input is accepted or should be blocked
# the allowRegex list has a higher priority if both arguments are used
# https://pyinputplus.readthedocs.io/
import pyinputplus as pyip
print("Allow roman numerals.")
response = pyip.inputNum(allowRegexes=[r'(I|V|L|C|D|M)+', r'zero'])
print("Allow roman numerals.")
response = pyip.inputNum(allowRegexes=[r'(i|v|l|c|d|m)+', r'zero'])

print("Block all even numbers.")
response = pyip.inputNum(blockRegexes=[r'[02468]$'])
