# group regex
import re
# create regex object (with raw string ideally)
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# masking sequence
phoneNumRegex2 = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 432-456-6875")

# only prints if number is found otherwise mo is None and print will throw an error
print("Number found: " + mo.group(0))
print("Number found: " + mo.group())
print("prefix found: " + mo.group(1))
print("Number without prefix found: " + mo.group(2))
# print all groups
print("groups found: ",  mo.groups())
# multiple assignment can be used because group is a tuple
areacode, mainNumber = mo.groups()
print(areacode)
print(mainNumber)
mo = phoneNumRegex2.search("My number is (432)-456-6875")
areacode, mainNumber = mo.groups()
print(areacode)
print(mainNumber)
mo = phoneNumRegex
