#! python3
# mcb.pyw - saves text end loads it to the clipboard
# py.exe mcb.py save <key> - saves text with key to clipboard
# py.exe mcb.py <key> - loads text saved in clipboard
# py.exe mcb.py list - loads all keys to the clipboard
# py.exe mcb.py delete <key> - deletes text and leyword
import shelve
import pyperclip
import sys

mcbSelf = shelve.open('mcb')

# save contents to clipboard
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbSelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbSelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbSelf.keys())))
    # delete all
    elif sys.argv[1].lower() == 'deleteall':
        mcbSelf.clear()
    elif sys.argv[1] in mcbSelf:
        pyperclip.copy(mcbSelf[sys.argv[1]])
mcbSelf.close()
