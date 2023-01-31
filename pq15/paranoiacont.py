import os, PyPDF2, re, sys
while len(sys.argv) == 2:
    path = '/home/satvshr/Desktop/pdf'
    for folder, subfolders, files in os.walk(path):
        for i in files:
                pdf = open(os.path.join(folder, i), 'rb')
                reader = PyPDF2.PdfFileReader(pdf)
                reader.decrypt(str(sys.argv[1]))
                writer = PyPDF2.PdfFileWriter()

                try:
                    pages = reader.numPages
                    for j in range(pages):
                        page_obj = reader.getPage(j)
                        writer.addPage(page_obj)
                    i = re.sub('_encrypted.pdf', '', i)
                    new_pdf = open(os.path.join(folder, i + '.pdf'), 'wb')
                    writer.write(new_pdf)
                    pdf.close()
                    new_pdf.close()
                except PyPDF2.utils.PdfReadError:
                    print("Wrong Password!")
                    