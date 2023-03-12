import pprint
# create own modules
# the script creates a module named cats example in file cats.py
# print statements are only used to see the output
cats = [{'name': 'Zophie', 'desc': 'chubby'},
        {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))
fileObj = open('myCats.py', 'w')
print(fileObj.write('cats = ' + pprint.pformat(cats) + '\n'))
fileObj.close()
