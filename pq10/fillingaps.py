import re, os
object = re.compile(r'00')
dirlist = os.listdir('/home/satvshr/amfoss-tasks-2/pq9/testfolder')
for i in dirlist:
    mo = object.search(f'{i}')     
    print(mo)
