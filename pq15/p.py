import os, PyPDF2, re, sys
while len(sys.argv) == 2:
    path = '/home/satvshr/Desktop/pdf/'
    for folder, subfolders, files in os.walk(path):
        for i in files:
                pdf = open(os.path.join(folder, i), 'rb')
                print(pdf)
                reader = PyPDF2.PdfFileReader(pdf)
                print(reader.isEncrypted)