# using pipe symbol
import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
batRegex = re.compile(r'Bat(man|mobil|copter|bat)')
mo2 = batRegex.search('Batmobil lost a wheel')
# if both pattern are in the string only the first one will be found
print(mo1.group())
# has bat as prefix
print(mo2.group())
print(mo2.group(1))

# optionals (wo) is marked a optional with ?
batRegex = re.compile(r'Bat(wo)?man')
mo2 = batRegex.search('The adventure of Batman')
print(mo2.group())
batRegex = re.compile(r'Bat(wo)?man')
mo2 = batRegex.search('The adventure of Batwoman')
print(mo2.group())

# with * expression can exist multiple times or 0
batRegex = re.compile(r'Bat(wo)*man')
mo2 = batRegex.search('The adventure of Batman')
print(mo2.group())
mo2 = batRegex.search('The adventure of Batwoman')
print(mo2.group())
mo2 = batRegex.search('The adventure of Batwowowowoman')
print(mo2.group())
