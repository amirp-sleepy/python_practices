#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, sys, pyperclip, os

KEYWORDS_PATH = os.path.join("keyword", "Keywords")

def main():

    os.makedirs(os.path.dirname(KEYWORDS_PATH), exist_ok= True)
    input_argument = sys.argv[1].lower().strip()

    if input_argument == "save":
        saving(sys.argv[2].lower().strip())

    else:
        copy_to_clipboard(input_argument)
    
#save the new keyword
def saving(keyword):
    
    file = shelve.open(KEYWORDS_PATH)

    file[keyword] = pyperclip.paste()
    file.close()

#find the keyword and return it in clipboard
def copy_to_clipboard(key):
    
    file = shelve.open(KEYWORDS_PATH)

    if key == "list":
        keys = list(file.keys())
        if len(keys) > 0:

            keys = "\n".join(keys)
            pyperclip.copy(keys)

        else:
            print("list is empty!")

    else:
        if key in file:
            pyperclip.copy(file[key])
        else:
            print(f"The keyword '{key}' doesn't exist!")
    file.close()

main()
