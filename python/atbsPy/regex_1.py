# is input a phone number WITHOUT regular expressions

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isDecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isDecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isDecimal():
            return False
    return True
