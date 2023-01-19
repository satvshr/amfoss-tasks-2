import os, shutil

for folderName, subfolders, filenames in os.walk('/home/satvshr/Desktop'):
    print('The current FOLDER is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        filename = os.path.join(folderName,filename)
        print(filename)
        if filename.endswith(".c"):
           shutil.copy(filename, '/home/satvshr/amfoss-tasks-2/pq10/copy')