import re
# find text with one or more numbers in the begining, followed by whitespace and  letters
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(
    '''10 drummers, 11 pipers, 10 swans, 9 ladies,8 maids, 
    7 birds,6 geese, 5 rings,4 birds, 3 hens, 2 doves, 1 partridge'''))

# find vowels
vowels = re.compile('[aeiouAEIOU]')
print(vowels.findall('RoboCop eats baby food. BABY FOOD'))
# find everything but vowels
noVowels = re.compile('[^aeiouAEIOU]')
print(noVowels.findall('RoboCop eats baby food. BABY FOOD'))
# string has to start with a match
startsWith = re.compile(r'^hello')
print('startsWith: ', startsWith.search('hello, world.'))
print('startsWith: ', startsWith.search('She said hello, world.'))
# string has to end with a match
endsWith = re.compile(r'\d$')
print('endswWith: ', endsWith.search('i am 30'))
print('endswWith: ', endsWith.search('i am jess'))
# beginning and end has to match
wholeStringNum = re.compile(r'^\d+$')
print('wholeStringNum: ', wholeStringNum.search("12346"))
print('wholeStringNum: ', wholeStringNum.search("123hts46"))
# joker .
joker = re.compile(r'.at')
print('joker: ', joker.findall('The cat in rhe hat sat on a flat mat'))
# find any (.*) is always greedy (.*?) not greedy
nameReg = re.compile(r'First name: (.*) Last name: (.*)')
mo = nameReg.search('First name: Jess Last name: Sample')
print('nameReg: ', mo.group(1), mo.group(2))
# not greedy
nameRegNotGreedy = re.compile(r'<.*?>')
mo = nameRegNotGreedy.search('<First name: Jess> Last name: Sample>')
print('nameRegNotGreedy: ', mo.group())
# DOTALL finds matches even if theres a linebreak
dotall = re.compile('.*', re.DOTALL)
mo = dotall.search('Hello,\nworld!')
print('nameRegNotGreedy: ', mo.group())
# substitude
nameReg = re.compile(r'Agent \w+')
print('nameReg: ', nameReg.sub('CENSORED',
      'Agent Alice gave the secret documents to Agent Bob'))
# integrate spaces and comments with re.VERBOSE
complexReg = re.compile(r'''(
(\d{3}|\(d{3}\))?
# prefix
(\s|-|\.)?
# separator
\d{3}
# first three digits
(\s|-|\.)
# separator
\d{4}
# last four digits
(\s*
(ext|x|ext.)\s*\d{2,5})?
# extension
)''', re.VERBOSE)
# add more than one argumemt to re.compile()
argsReg = re.compile("foo", re.IGNORECASE | re.DOTALL | re.VERBOSE)
