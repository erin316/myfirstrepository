import hashlib
# md5=hashlib.md5()
# data="shjdhnckjdk"
# md5.update(data.encode("utf8"))
# data_2=md5.hexdigest()
# print(data_2)
# print(type(data_2))
# data01="陈维"
# md5.update(data01.encode("utf8"))
# data03=md5.hexdigest()
# print(data03)

import hashlib
import re
#模拟登录
class Loginin:
    def __init__(self):
        self.md5=hashlib.md5("#$%$&%GFYB".encode("utf8"))

    def display(self):
        format_title = "{:^6}\t{:^6}"
        print(format_title.format("1:注册", "2:登录"))

    def menu(self):
        menu_list = {"1": "self.enroll", "2": "self.login"}
        option_raw=input("请输入选项:")
        option=re.search("\d+",option_raw).group()
        if option in menu_list:
            ss=eval(menu_list[option])
            ss()

    def enroll(self):
        name=input("请输入姓名：")
        password=input("请输入密码：")
        self.md5.update(password.encode("utf8"))
        more_password=self.md5.hexdigest()
        with open("./user.txt","a") as f:
            f.write(f"{name}|{more_password}\n")

    def login(self):
        name=input("请输入姓名:")
        password=input("请输入密码:")
        self.md5.update(password.encode("utf8"))
        password_1=self.md5.hexdigest()
        with open("./user.txt","r") as f:
            for line in f:
                tt=re.split("\|",line)
                name01=tt[0]
                password01=tt[1][:-1]
                if name==name01:
                    if password_1==password01:
                        print("登录成功")
                    else:
                        print("密码不对")

    def main(self):
        while True:
            self.display()
            self.menu()


if __name__ == '__main__':
    login=Loginin()
    login.main()















