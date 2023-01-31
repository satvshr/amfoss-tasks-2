import PyPDF2
list = []
file = open('dictionary.txt')
read = file.readlines()
pdf = open('/home/satvshr/Desktop/bruteforce.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf)
for i in read:
    list.append(i.replace("\n", ""))

for i in list:
    print(i)
    try:
        if pdf_reader.decrypt(i) == 1:
            print('The password was ' + i)
            break
        elif pdf_reader.decrypt(i.lower()) == 1:
            print('The password was ' + i)
            break
    except:
        print('Could not determine the password')

