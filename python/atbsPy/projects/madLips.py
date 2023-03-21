#! python3
# madLips.py generates a text with random words from user input
import re

adjective = input("Enter an adjective: ")
noun = input("Enter an noun: ")
adverb = input("Enter an adverb: ")
verb = input("Enter an verb: ")


tf = open("madLips.txt")
text = tf.read()
t = ''

# TODO: change code below with regex sub
print(text)
for word in text.split():
    if word == "ADJECTIVE":
        t += f"{input('Enter an adjective: ')} "
    elif word == "NOUN":
        t += f"{input('Enter an noun: ')} "
    elif word == "VERB":
        t += f"{input('Enter an verb: ')} "
    elif word == "ADVERB":
        t += f"{input('Enter an adverb: ')} "
    else:
        t += f"{word} "
tf.close()
tf = open("madLips.txt", "w")
tf.write(t)
