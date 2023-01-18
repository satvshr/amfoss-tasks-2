import os, shutil

for folderName, subfolders, filenames in os.walk('/home/satvshr/Desktop/'):
    print('The current FOLDER is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        print(os.path.getsize(filename)) 
        if os.path.getsize(filename) > 100000000:
            os.unlink(os.path.join(subfolder, filename))


            