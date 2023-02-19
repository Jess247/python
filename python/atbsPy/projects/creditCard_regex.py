# This program will find credit card numbers in a text from the clipboard.
# (without checking if it is a valid visa, master card etc format)
# All found credit card numbers will be censored.
# The new text will be saved to the clipboard.
#!Python 3
import re
import pyperclip

# card regex
cardRegex = re.compile(r'\d{4}\s\d{4}\s\d{4}\s\d{4}')

# find matches in clipboard text and copy censored
text = str(pyperclip.paste())

if cardRegex.findall(text):
    pyperclip.copy(cardRegex.sub('CENSORED', text))
    print(cardRegex.sub('CENSORED', text))
else:
    print("Nothing found!")
# copy result to clipboard
