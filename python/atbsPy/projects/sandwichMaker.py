# This program will ask the user to enter different ingredients for a sandwich
# the user will get different menu options
# all inputs need to be valid answers
import pyinputplus as pyip
# Ask user what to put on the sandwich
bread = pyip.inputMenu(
    "Bread Menu:\n", ["White bread", "Wheat bread", "Whole grain bread"])
mainTopping = pyip.inputMenu(
    "Toppings Menu:\n", ["Chicken", "Turkey", "Ham", "Tofu"])
cheeseYesNo = pyip.inputYesNo("Would you like some cheese?")
cheeseType = pyip.inputMenu(
    "Cheese Menu:\n", ["Cheddar", "Gouda", "Mozzarella"])
mayoYesNo = pyip.inputYesNo("Would you like some mayo?")
lettuceYEsNo = pyip.inputYesNo("How about some lettuce?")
tomatoYesNo = pyip.inputYesNo("Tomatos?")
amountOfSandwiches = pyip.inputInt()
price = 5
# TODO: put the sandwiches together
