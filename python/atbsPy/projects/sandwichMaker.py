# This program will ask the user to enter different ingredients for a sandwich
# the user will get different menu options
# all inputs need to be valid answers
import pyinputplus as pyip
# Ask user what to put on the sandwich
bread = pyip.inputMenu(["White bread", "Wheat bread", "Whole grain bread"])
mainTopping = pyip.inputMenu(["Chicken", "Turkey", "Ham", "Tofu"])
cheeseYesNo = pyip.inputYesNo("Would you like some cheese?")
if cheeseYesNo == "yes":
    cheeseYesNo = pyip.inputMenu(["Cheddar", "Gouda", "Mozzarella"])
else:
    cheeseYesNo = "no cheese"
mayoYesNo = pyip.inputYesNo("Would you like some mayo?")
if mayoYesNo == "yes":
    mayoYesNo = "mayo"
else:
    mayoYesNo = "no mayo"
lettuceYesNo = pyip.inputYesNo("How about some lettuce?")
if lettuceYesNo == "yes":
    lettuceYesNo = "lettuce"
else:
    lettuceYesNo = "no lettuce"
tomatoYesNo = pyip.inputYesNo("Any tomatoes?")
if tomatoYesNo == "yes":
    tomatoYesNo = "tomatoes"
else:
    tomatoYesNo = "no tomatoes"
amountOfSandwiches = pyip.inputInt("How many sandwiches do you want?", min=1)
price = 5
# TODO: put the sandwiches together

print(
    f"You ordered {bread} with {mainTopping}, {cheeseYesNo}, {mayoYesNo}, {lettuceYesNo} and {tomatoYesNo}.")
if amountOfSandwiches > 1:
    print(
        f"You ordered {amountOfSandwiches}, that makes {price * amountOfSandwiches}$, please.")
