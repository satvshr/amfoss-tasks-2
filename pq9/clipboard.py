#! python3
# mcb.pyw - Save and loads pieces of tet to the clipboards
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#        py.exe mcb.pyw list - loads all keywords to clipboard
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from shelf
#        py.exe mcb.pyw deleteall - Deletes all keywords from shelve
"""
Extend the multiclipboard program in this chapter so that it has a delete <keyword> 
command line argument that will delete a keyword from the shelf. Then add a delete 
command line argument that will delete all keywords.
"""
import sys, pyperclip, shelve
cboard = shelve.open('clipboard')

    # Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1] == 'copy':
        cboard[sys.argv[2]] = pyperclip.paste()
    # To delete items in a shelve, pass the keyward as an argument to del cboard[keyword]
    elif sys.argv[1] == 'delete':
        del cboard[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1] == 'list':
        pyperclip.copy(str(list(cboard.keys())))
    # To delete all arguments, run a loop through the list of keys
    elif sys.argv[1] == 'deletewhole':
        for keyword in list(cboard.keys()):
            del cboard[keyword]
    elif sys.argv[1] in cboard:
        pyperclip.copy(cboard[sys.argv[1]])
else:
    print('Usage: python3 clipboard.py save/delete/list/deleteall [keyphrase] - copy phrase text')
cboard.close()