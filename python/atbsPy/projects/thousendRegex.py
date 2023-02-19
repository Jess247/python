# This program will format for numbers like 1,000 to numbers like 1000
#! Python 3

import re

numberRegex = re.compile(r'^\d{1,3}(,\d{3})*$')
print(numberRegex.search('6,384,384'))

firstnameRegex = re.compile(r'^[A-Z][a-z]*\sWatanabe')
print(firstnameRegex.search('Paul Watanabe'))
print(firstnameRegex.search('Paul watanabe'))
print(firstnameRegex.search('paul watanabe'))
