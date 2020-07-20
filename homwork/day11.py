list01=[6,2,3,4,5,6,7,3,2,4,8]
#定义函数，删除列表中重复的元素

def del_repeat():
    list01.sort()
    m=list01[-1]
    for item in range(len(list01)-2,-1,-1):
        if list01[item]==m:
            del list01[item]
        else:
            m=list01[item]


# del_repeat()
# print(list01)

class Commodity:
    def __init__(self, cid, name, price):
        self.cid = cid
        self.name = name
        self.price = price

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
    Commodity(1006, "屠龙刀", 10000),
    Commodity(1007, "口罩", 50),
]

# 定义函数, 删除列表中商品名称相同的商品(不使用其他容器, 自定义算法)

def del_re_commdity():
    dict01={}
    for item01 in range(len(list_commodity_infos)-1):
        for item02 in range(item01+1,len(list_commodity_infos)):
            if list_commodity_infos[item02].name==list_commodity_infos[item01].name:
                dict01[item01]=item02
    list01=[]
    for item in dict01:
        list01.append(dict01[item])
    list01.sort(reverse=True)

    for item in list01:
        del list_commodity_infos[item]
#
# del_re_commdity()
# for item in list_commodity_infos:
#     print(item.name)

# (1)定义零元素向后移动的函数　zero_to_end()
#      思想：从后向前判断，如果是0则删除,在末尾追加.
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]

# (2)定义合并函数　merge()
#     核心思想：零元素后移，判断是否相邻相同。如果是则合并.
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]

list_merge = [2, 0, 0, 2]

def zero_to_end(list_merge):
    for item in range(len(list_merge)-1,-1,-1):
        if list_merge[item]==0:
            del list_merge[item]
            list_merge.append(0)
# zero_to_end(list_merge)
# print(list_merge)


def merge(list_merge):
    zero_to_end(list_merge)
    for item in range(len(list_merge)-1):
        if list_merge[item]==list_merge[item+1]:
            list_merge[item]+=list_merge[item+1]
            del list_merge[item+1]
            list_merge.append(0)


# 3.定义向左移动函数, 改变list_map中的数据
# 思路：将list_map每行赋值给list_merge
# 调用合并函数(练习2)

list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]

def left_move():
    for list_merge in list_map:
        merge(list_merge)


def right_move():
    for item in list_map:
        list_merge=item[::-1]
        merge(list_merge)





# left_move()
# for item in list_map:
#     print(item)










