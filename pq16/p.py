import os, csv, openpyxl
folder = '/home/satvshr/Desktop/amfoss-tasks-2/pq16/excelSpreadsheets'

for i in os.listdir(folder):
    if i.endswith('xlsx'):
        x = '/home/satvshr/Desktop/amfoss-tasks-2/pq16/excelSpreadsheets/' + i
        wb = openpyxl.load_workbook(x)

        for sheets in wb.get_sheet_names():
            sheet = wb[sheets]
            i = i.rstrip('.xlsx')
            print(i)