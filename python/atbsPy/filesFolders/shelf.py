import shelve
# save data with shelve (like in a dict)
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# does the same:
# cats = ['Zophie', 'Pooka', 'Simon']
# with shelve.open as shelfFile:
# shelfFile['cats'] = cats
# shelfFile.close()

# read shelve file
shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])

# shelve list
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()
