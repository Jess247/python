# This program will find dates in DD/MM/YYYY format
# The matched strings will be saved in the variables day month year
# check if date is valid
import re

# TODO: Date regex
dateRegex = re.compile(r'(\d{1,2})\/(\d{1,2})\/(\d{4})')
mo = dateRegex.search("23/2/1990")
day = int(mo.group(1))
month = int(mo.group(2))
year = int(mo.group(3))

isLeapYear = False
if year % 4 == 0 and year % 100 != 0:
    isLeapYear = True
else:
    isLeapYear = False

# month 4, 7, 11 = 30 days
# month 1, 3, 5, 6, 8 , 9,10, 12 = 31 days
# month 2 either 28 or 26


def checkDate(day, month, year, isLeapYear):
    if day < 32 and month < 13 and year > 999 and year < 3000:
        if month == 4 or month == 7 or month == 11:
            if day <= 30:
                return "Date is valid"
        elif month == 2:
            if isLeapYear and day < 29:
                return "Date is valid"
            elif isLeapYear != True and day < 30:
                return "Date is valid"
            else:
                return "Date is not valid"
        elif day < 32:
            return "Date is valid"
    else:
        return "Date is not valid"


isValid = checkDate(day, month, year, isLeapYear)
print(isValid)
