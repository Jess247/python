import re
# look for at least one match
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('Batwoman')
print(mo.group())
mo = batRegex.search('Batman')  # no match
print(mo)

# look for a specific amount or a range of occurrences
haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('HaHaHa')
print(mo.group())
mo = haRegex.search('Ha')  # no match
print(mo)

# greedy means if multiple matches longest will be returned
haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('HaHaHaHaHa')
print(mo.group())
# not greedy by adding ?
haRegex = re.compile(r'(Ha){3,5}?')
mo = haRegex.search('HaHaHaHaHa')
print(mo.group())
