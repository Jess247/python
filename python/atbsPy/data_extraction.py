#!  python3
import re
import pyperclip
# find numbers and email addresses in clipboard

# phone number regex
phoneRegex = re.compile(r'''(
    # prefix
    (\d{3}|\(\d{3}\))?
    # separator
    (\s|-|\.)?
    # next 3 digits
    \d{3}
    # separator
    (\s|-|\.)
    # next 4 numbers
    \d{4}
    # extension
    (\s*
    ect|x|ext.)\s*\d{2,5})?) 
''')

# TODO: Regex for email

# TODO: find matches in text

# TODO: copy result to clipboard
