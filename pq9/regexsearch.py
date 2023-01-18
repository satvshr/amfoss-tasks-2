import re
import os

a = input("String you want to search for: ")
find = re.compile(r'{a}')
dirlist = os.listdir('/home/satvshr/amfoss-tasks-2/pq9/testfolder')
for i in dirlist:
    with open(f'{i}', 'r') as file:
        content = file.read()
        if '{a}' in content:
            print(f"string you were searching for was found in {i}!")

