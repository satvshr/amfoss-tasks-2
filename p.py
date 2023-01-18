import re
import os

a = input("String you want to search for")
find = re.compile(r'{a}')
dirlist = os.listdir('/home/satvshr/amfoss-tasks-2/pq9/testfolder')

for i in dirlist:
    file = open(f'/home/satvshr/amfoss-tasks-2/pq9/testfolder/{i}')
    content = file.read()
    mo = find.search(content)
    if len(mo.group()) != 0:
        print(f"The string youre searching for was found in file {i}")
    file.close()


