"""
有一个列表，内部每项是一个元组，元组中第一项产品名称，
第二项产品数量。怎么把列表内相同产品的数量求和，
并按照数量对列表排序
"""
list01=[("牙刷",23),("牙膏",22),("葡萄",15),("车厘子",29),("牙膏",29),("车厘子",29),("葡萄",15)]
#将相同项的数量进行叠加
for item01 in range(len(list01)-1):
    #将列表每项转为列表进行数量的叠加
    list03=list(list01[item01])
    for item02 in range(item01+1,len(list01)):
        if list03[0]==list01[item02][0]:
            list03[1]+=list01[item02][1]
            #将数量叠加后的列表转为元组替换原项
            list01[item01]=tuple(list03)
            #将后面的重复项赋值为元组(0,0)
            list01[item02]=(0,0)
#删除(0,0)的元组
for item in range(len(list01)-1,-1,-1):
    if list01[item][0]==0:
        del list01[item]
#排序
result=sorted(list01,key=lambda item:item[1])
print(result)


# import re
# f=open("student_info.txt","r")
# print(f.readline())

format_title = "{:^6}{:^12}\t{:^6}\t{:^10}\t{:^10}\t{:^10}"
print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))












