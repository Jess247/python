#! python 3
import pyperclip
# Add text from clipboard
text = pyperclip.paste()
# edit text
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
# copy new text to clipboard
text = '\n'.join(lines)
pyperclip.copy(text)
print(text)
