from pathlib import Path
p = Path('spam.txt')
# write file (path objects only allow one interaction)
p.write_text('Hello, World!')
print(p.write_text('Hello, World!'))  # number of characters
# read file
print(p.read_text())
# proper way to read or write
# create file Object
fileName = open(Path.cwd() / 'hello.txt')
# read file object
fileContent = fileName.read()
print(fileContent)
sonnetFile = open('sonnet29.txt')
sonnetContent = sonnetFile.readlines()
print(sonnetContent)
