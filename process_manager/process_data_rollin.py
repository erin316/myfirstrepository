"""
对Excel文件的读取，并传送给服务端
"""
from socket import *
import xlrd
import time

sock_client=socket(AF_INET,SOCK_STREAM)

sock_client.connect(("127.0.0.1",8888))

class get_excel_info:
    def __init__(self,file_address):
        self.excelfile=xlrd.open_workbook(file_address)

    #定义生成器，每次yield一行内容表示每一条记录
    def get_excel_data(self):
        sheet=self.excelfile.sheet_by_name('ST Process')
        tuple01=(sheet.name,sheet.nrows,sheet.ncols)
        for row in range(1,tuple01[1]):
            # print(sheet.row_values(row))
            yield sheet.row_values(row)

ss=get_excel_info(r"./Process_300.xlsx")
for item in ss.get_excel_data():
    ss=str(item).encode()
    print(ss)
    sock_client.send(ss)
    time.sleep(0.05)

sock_client.close()


