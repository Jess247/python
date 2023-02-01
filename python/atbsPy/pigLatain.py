# translate english in pig latin
print("Enter the English message to translate into Pig Latin: ")
message = input()
# vowels
VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
# list of pig latin words
pigLatin = []
for word in message.split():
    # separate symbols that aren't letters from the start of a word
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefixNonLetters += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
    # separate symbols that aren't letters from the end of a word
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    # remember if all or the first letter was uppercase
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    # turn word into lowercase for translation
    word = word.lower()

    # separate constants in the beginnin
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]

    # add piglatin ending
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    # turn letters back to uppercase if they were before
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()

    # add non alphabetic symbols back to word
    pigLatin.append(prefixNonLetters + word + suffixNonLetters)
    # join single words to string
    print(' '.join(pigLatin))
