
#! python3
# mcb.pyw - Save and loads pieces of tet to the clipboards
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf
#        py.exe mcb.pyw deleteall - Deletes all keywords from shelve

import sys, pyperclip, shelve
cboard = shelve.open('clipboard')

if len(sys.argv) == 3:
    if sys.argv[1] == 'save':
        cboard[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1] == 'delete':
        del cboard[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(cboard.keys())))
    elif sys.argv[1] == 'deletewhole':
        cboard.clear()
    elif sys.argv[1] in cboard:
        pyperclip.copy(cboard[sys.argv[1]])
else:
    print('Usage: python3 clipboard.py save/delete/list/deleteall [keyphrase] - copy phrase text')
cboard.close()