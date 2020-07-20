"""
服务端实现对数据库的增删改查
"""
from socket import *
from select import *
import pymysql,re,hashlib

class Database:
    def __init__(self):
        self.__create_db()

    def __create_db(self):
        self.__db = pymysql.connect(host="localhost",
                                  port=3306,
                                  user="root",
                                  password="chenwei316",
                                  database="process_manager_formal",
                                  charset="utf8")

        self.__cur = self.__db.cursor()

    def insert_register(self,name,tel,mail,password):
        sql="insert into user (name,tel,mail,password) values(%s,%s,%s,%s)"
        self.__cur.execute(sql,[name,tel,mail,password])
        self.__db.commit()

    def get_user_info(self):
        sql="select * from user"
        self.__cur.execute(sql)
        data=self.__cur.fetchmany()
        print(data)

    def find_name(self,name):
        sql="select name from user where name=%s"
        self.__cur.execute(sql,[name])
        if self.__cur.fetchone():
            return True
        return False

    def login(self,name,password):
        sql="select name,password from user where name=%s"
        try:
            self.__cur.execute(sql,[name])
            result=self.__cur.fetchone()
            if result[1]==password:
                return True
            return False
        except:
            return False

class ProcessManager:
    def __init__(self,host="0.0.0.0",port=8000):
        self.__host=host
        self.__port=port
        self.__rlist=[]
        self.__wlist=[]
        self.__xlist=[]
        self.__socket_set()
        self.__db=Database()

    def __socket_set(self):
        self.__sock=socket(AF_INET,SOCK_STREAM)
        self.__sock.setblocking(False)
        self.__sock.bind((self.__host,self.__port))

    def start(self):
        self.__sock.listen(5)
        self.__rlist.append(self.__sock)
        while True:
            rs,ws,xs=select(self.__rlist,self.__wlist,self.__xlist)
            for r in rs:
                if r is self.__sock:
                    connfd,addr=self.__sock.accept()
                    connfd.setblocking(False)
                    self.__rlist.append(connfd)
                else:
                    self.__handle(r)

    def __handle(self,connfd):
        recv_data=connfd.recv(1024).decode()
        print(recv_data)
        recv_info=re.split("\|",recv_data)
        if recv_info[0]=="register":
            self.register(recv_info[1],connfd)
        elif recv_info[0]=="login":
            self.login(recv_info[1],connfd)

    def register(self,info,connfd):
        md5=hashlib.md5("sjd@&%$#^$".encode("utf8"))
        recv_info=re.split("#",info)
        name=recv_info[0]
        tel=recv_info[1]
        mail=recv_info[2]
        row_password=recv_info[3]
        md5.update(row_password.encode("utf8"))
        password =md5.hexdigest()
        data=self.__db.find_name(name)
        print(data)
        if not self.__db.find_name(name):
            self.__db.insert_register(name, tel, mail,password)
            self.__db.get_user_info()
            connfd.send("OK".encode())
        else:
            connfd.send("Fail".encode())

    def login(self,info,connfd):
        md5 = hashlib.md5("sjd@&%$#^$".encode("utf8"))
        recv_info = re.split("#", info)
        name = recv_info[0]
        row_password = recv_info[1]
        md5.update(row_password.encode("utf8"))
        password=md5.hexdigest()
        if self.__db.login(name,password):
            connfd.send("OK".encode())
        else:
            connfd.send("Fail".encode())

if __name__ == '__main__':
    process_severe=ProcessManager("127.0.0.1",8889)
    process_severe.start()



















