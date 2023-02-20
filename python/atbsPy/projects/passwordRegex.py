# This program will check if the entered password is a strong password
# min 8 characters long
# lower und uppercase letters
# number
import re
password = "Hello2kyt"


def checkPassword(password):
    passwordRegex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    if passwordRegex.search(password):
        return "This is a strong password."
    else:
        return "Your password is easy to guess"


s = checkPassword(password)
print(s)
