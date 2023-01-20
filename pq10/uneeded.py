import os, shutil

for folderName, subfolders, filenames in os.walk('/home/satvshr/Desktop/'):
    print('The current FOLDER is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        filename = os.path.join(folderName,filename)
        print('FILES: ' + filename)
        print(os.path.getsize(filename)) 
        if os.path.getsize(filename) > 100000000:
            print("These are the files over 100mb:",os.path.join(folderName, filename))


            