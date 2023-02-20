# This program will do the same as strip() only with regex
import re

string = "Hello, world !"


def stripRegex(string):
    stripReg = re.compile(r'\s*')
    return stripReg.sub('', string)


stripedText = stripRegex(string)
print(stripedText)
