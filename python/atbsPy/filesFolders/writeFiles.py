from pathlib import Path

baconFile = open('bacon.txt', 'w')
# write file object
fileContent = baconFile.write('Hello, world!\n')
baconFile.close()
