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
