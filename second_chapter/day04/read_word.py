import xlrd

from datetime import date,datetime

def read_excel():
    #打开excel文件
    excelfile=xlrd.open_workbook(r'./Process.xlsx')
    #获取每个sheet的名字
    sheet_list=excelfile.sheet_names()
    print(sheet_list)
    sheet=excelfile.sheet_by_name('ST  Process')
    print(sheet)
    sheet01=excelfile.sheet_by_index(0)
    print(sheet01)
    print(sheet.name,sheet.nrows,sheet.ncols)
    rows=sheet.row_values(7)
    cols=sheet.col_values(1)
    print(rows,cols)

    # print(sheet.cell(10,25).value)
    # print(sheet.cell(10,25).ctype)


# read_excel()

list01='[1,2,3,4,5,6]'
l=eval(list01)
print(type(l))






