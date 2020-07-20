"""
客户端实现功能以下
1。用户登录
1。通过可通过上传excel达到上传数据到数据库的目的
2。修改数据
3。删除数据
4。查找数据
5。保存后的整个流程发送至邮箱
6。下载整个流程
"""
from socket import *
import re
import openpyxl

# class ProcessManagerClint:
#     def __init__(self,host="127.0.0.1",port=8888):
#         self.host=host
#         self.port=port
#         self.create_sock()
#
#     def create_sock(self):
#         self.__sock=socket(AF_INET,SOCK_STREAM)
#         self.__sock.connect((self.host,self.port))
#
#     def display1(self):
#         print('---------------------')
#         print('-------1.注册 --------')
#         print('-------2.登录 --------')
#         print('---------------------')
#
#     def display_func(self):
#         print('-----------------------------')
#         print('----------1.上传CT -----------')
#         print('----------2.修改流程参数 ------')
#         print('----------3.删除数据 ---------')
#         print('----------4.搜索 -------------')
#         print('----------5.下载 -------------')
#         print('-----------------------------')
#
#     def menu(self):
#         row_option=input("请输入选项：")
#         option=re.findall("\d",row_option)[0]
#         print(option)
#         if option=="1":
#             self.register()
#         elif option=="2":
#             self.login()
#
#     def menu_func(self):
#         row_option=input("请输入选项：")
#         option=re.findall("\d",row_option)[0]
#         print(option)
#         if option=="1":
#             self.uploading()
#         # elif option=="2":
#         #     self.login()
#
#     def register(self):
#         choose=True
#         while choose:
#             name = input("请输入姓名：")
#             if not name:
#                 print("该姓名已存在")
#             tel = int(input("请输入电话："))
#             mail = input("请输入邮箱：")
#             password=input("请输入密码：")
#             send_info = "register|"+name + "#" + str(tel) + "#" + mail+"#"+password
#             self.__sock.send(send_info.encode())
#             recv_info=self.__sock.recv(1024)
#             print(recv_info)
#             if recv_info.decode()=="OK":
#                 print("添加成功")
#                 choose=False
#             else:
#                 print("该姓名已存在")
#
#     def login(self):
#         name=input("请输入姓名：")
#         password=input("请输入密码：")
#         send_info="login"+"|"+name+"#"+password
#         self.__sock.send(send_info.encode())
#         result=self.__sock.recv(1024).decode()
#         if result=="OK":
#             print("登录成功")
#         else:
#             print("用户不存在或密码错误")

def uploading():
    workbook=openpyxl.load_workbook("Process_300.xlsx")
    mysheet=workbook.get_sheet_by_name("ST Process")
    print(mysheet["A1"].value)
    ss=mysheet.cell(row=1,column=1).value
    print(ss)

uploading()





#     def main(self):
#         self.display1()
#         self.menu()
#         while True:
#             self.display_func()
#             self.menu_func()
#
#
#
# if __name__ == '__main__':
#     process_manager=ProcessManagerClint(host="127.0.0.1",port=8888)
#     process_manager.main()




