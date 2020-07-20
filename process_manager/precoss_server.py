"""
处理从客户端传送的文件，并将其存储至7数据库
"""
import pymysql
from socket import *
import re
sock_server=socket(AF_INET,SOCK_STREAM)
sock_server.bind(("0.0.0.0",8888))
sock_server.listen(5)
connfd,addr=sock_server.accept()

class Database:
    def __init__(self):
        self.db=pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="chenwei316",
            database="ProcessManager",
            charset="utf8"
        )
        self.cur=self.db.cursor()
    #[[item,region,line,groupmark,stationcode,stationname,retestrate,linedownrate,
    # efficiency,manualct,machinect,stationct,piece,uphperhc,uphpermachine,hcpermachine,hc,
    # qpl,targetuph,machinetype,remark]
    def insert_data(self,tar_list):
        # ss=[1.0, 'G5', 'Sub Pre', 'Offline-Panel', 'Outer UCap-1F', 'Die Cut Upper GF Cap ADH - Outside',
        #     0.0, 0.0, 0.92, 94.32, 97.38, 97.38, 9.0, 315.656565656566, 0.0, '', 'Die-Cut', '']
        if tar_list[10]!=0:
            uphpermachine=3600/tar_list[10]*tar_list[8]*(1-tar_list[6])*(1-tar_list[7])*tar_list[12]
        else:
            uphpermachine=0
        if tar_list[9] !=0:
            uphperhc=3600/tar_list[9]*tar_list[8]*(1-tar_list[7])
        else:
            uphperhc=0
        if uphpermachine!=0:
            hcpermachine=uphperhc//uphpermachine+1
        else:
            hcpermachine=0
        if uphpermachine !=0:
            qpl = tar_list[13] // uphpermachine + 1
        else:
            qpl=0
        hc=qpl*hcpermachine
        tar_list.insert(13,uphperhc)
        tar_list.insert(14,uphpermachine)
        tar_list.insert(15,hcpermachine)
        tar_list.insert(16,hc)
        tar_list.insert(17,qpl)
        sql="insert into process values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cur.execute(sql,tar_list)



    def close(self):
        self.cur.close()
        self.db.close()

def main():
    database=Database()
    while True:
        data = connfd.recv(1024)
        if not data:
            database.db.commit()
        row_recv=eval(data.decode())
        print(row_recv)
        database.insert_data(row_recv)
    database.close()
    connfd.close()
    sock_server.close()

if __name__ == '__main__':
    main()