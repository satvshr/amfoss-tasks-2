import os, PyPDF2, re, sys
while len(sys.argv) == 2:
    password = sys.argv[1]

    path = '/home/satvshr/Desktop/pdf'

    for folder, subfolders, files in os.walk(path):
        for i in files:
            if i.endswith(('.pdf', '.PDF')):
                pdf = open(os.path.join(folder, i), 'rb')
                reader = PyPDF2.PdfFileReader(pdf)
                writer = PyPDF2.PdfFileWriter()
                writer.encrypt(sys.argv[1])

                pages = reader.numPages
                for j in range(pages):
                    page_obj = reader.getPage(j)
                    writer.addPage(page_obj)
                
                i = re.sub('.pdf', '', i)
                new_pdf = open(os.path.join(folder, i + '_encrypted.pdf'), 'wb')
                writer.write(new_pdf)
                pdf.close()
                new_pdf.close()




