import openpyxl, sys
if len(sys.argv) == 4:
    n = int(sys.argv[1])
    m = int(sys.argv[2])
    doc = sys.argv[3]
    print(sys.argv)

    open = openpyxl.load_workbook(doc)
    sheet = open['Sheet']
    sheet1 = open['Sheet1']
    col_len = 0
    row_len = 0

    for i in range(1, 1000):
        if sheet.cell(row = i, column = 1).value != None:
            row_len += 1
        else:
            break
    print(row_len)
    for i in range(1, 1000):
        if sheet.cell(row = 1, column = i).value != None:
            col_len += 1
        else:
            break
    print(col_len)
    print(sheet.max_row-1)
    print(sheet.max_column-1)



