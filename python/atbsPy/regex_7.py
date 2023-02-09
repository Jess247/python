# findall method returns a list of all matches or tupels if the pattern contains groups
import re
# creates a list
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegex.findall(
    "My number is 432-456-6875 my office number is 442-847-7465"))

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall(
    "My number is 432-456-6875 my office number is 442-847-7465"))
