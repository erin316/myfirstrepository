import re

class ProcessView:

    def menu(self):
        format_title = "{:^4}\t{:^4}\t{:^4}\t{:^4}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}" \
                       "\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}\t{:^6}"
        print(format_title.format("item", "region", "line", "groupmark", "stationcode", "stationname", "retestrate",
                                  "linedownrate", "efficiency", "manualct", "machinect", "stationct", "piece",
                                  "hcpermachine","hc","targetuph", "remark"))

    def insert_data(self):
        insert_list=[]
        item=int(input("请输入ID"))
        region=int(input("请输入ID"))
        groupmark=int(input("请输入ID"))
        stationcode=int(input("请输入ID"))
        stationname=int(input("请输入ID"))
        retestrate=int(input("请输入ID"))
        linedownrate=int(input("请输入ID"))
        efficiency=int(input("请输入ID"))
        manualct=int(input("请输入ID"))
        machinect=int(input("请输入ID"))
        stationct=int(input("请输入ID"))
        piece=int(input("请输入ID"))
        targetuph=int(input("请输入ID"))
        remark=int(input("请输入ID"))



    def main(self):
        input_content = input("请输入选项")
        input_option = re.findall("\d+", input_content)
        if input_option == "1":
            self.insert_data()

ss=ProcessView()
ss.menu()