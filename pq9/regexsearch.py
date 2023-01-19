import re
import os
a = input("String you want to search for: ")
find = re.compile(f'{a}')
dirlist = os.listdir('/home/satvshr/amfoss-tasks-2/pq9/testfolder')
for i in dirlist:
    with open(os.path.join('/home/satvshr/amfoss-tasks-2/pq9/testfolder', i), 'r') as file:
        content = file.read()
        mo = find.search(content)
        try:
            print(mo.group() + " was found in:")
            print(f"{i}")
        except AttributeError:
            continue

