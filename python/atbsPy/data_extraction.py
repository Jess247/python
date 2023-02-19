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
    (ect|x|ext.)\s*\d{2,5})?
    ) ''', re.VERBOSE)

# TODO: Regex for email
emailRegex = re.compile(r'''
# username
([a-zA-Z0-9._%+-]+
# followed by @ symbol
@
# domain name
a-zA-Z0-9.-]+
# dot top level domain
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)
# TODO: find matches in text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
# TODO: copy result to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
