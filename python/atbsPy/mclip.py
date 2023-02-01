#! python3
# mclip.py is a program that saves multiple clippings to clipboard
import pyperclip
import sys
TEXT = {"agree": """Yes I agree. That sounds fine to me""", "busy": """Sorry, can we do this later this week?""",
        "upsell": """Would you consider making this monthly donation?"""}


if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] -  copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"there is no text for {keyphrase}")
