import shelve
print(shelve.__file__)
# save data with shelve (like in a dict)
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
# read shelve file
shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])
