# find phone number with regex
import re
# create regex object (with raw string ideally)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search("My number is 432-456-6875")
# only prints if number is found otherwise mo is None and print will throw an error
print("Number found: " + mo.group())
