"""
开心消消乐游戏
"""
import random
list_merge=[2,2,3,2,2,2,2]

def eliminate_same_broadwise():
    """
    横向假如左右有相同项，则消除相同项并向右移动，之后在左侧补充1到5的随机数
    :return:
    """

    for i in range(0,len(list_merge)-2):
        if list_merge[i]==list_merge[i+1]==list_merge[i+2]:
            for s in range(0,3):
                del list_merge[i+s]
                item1 = random.randint(1, 5)
                list_merge.insert(0, item1)
        elif list_merge[i]==list_merge[i+1]==list_merge[i+2]==\
                list_merge[i+3]:
            for s in range(0,4):
                del list_merge[i+s]
                item1 = random.randint(1, 5)
                list_merge.insert(0, item1)
        elif list_merge[i]==list_merge[i+1]==list_merge[i+2]==\
                list_merge[i+3]==list_merge[i+4]:
            for s in range(0,5):
                del list_merge[i+s]
                item1 = random.randint(1, 5)
                list_merge.insert(0, item1)
        elif list_merge[i]==list_merge[i+1]==list_merge[i+2]==\
                list_merge[i+3]==list_merge[i+4]==list_merge[i+5]:
             for s in range(0,6):
                del list_merge[i+s]
                item1 = random.randint(1, 5)
                list_merge.insert(0, item1)
        elif list_merge[i]==list_merge[i+1]==list_merge[i+2]==\
                list_merge[i+3]==list_merge[i+4]==list_merge[i+5]==\
                list_merge[i+6]:
            for s in range(0,7):
                del list_merge[i+s]
                item1 = random.randint(1, 5)
                list_merge.insert(0, item1)

# eliminate_same_broadwise()
# print(list_merge)

map=[
    [2,1,1,2,3,5,4],
    [4,4,2,2,3,2,4],
    [2,4,1,4,3,4,5],
    [1,1,2,2,3,4,2],
    [1,2,3,4,4,4,3],
    [2,2,3,3,3,3,4],
    [2,2,3,2,2,2,4]
]

def move_matrix():
    for i in range(0,len(map)):
        for s in range(i,len(map)):
            map[i][s],map[s][i]=map[s][i],map[i][s]
    return map

def up_down_eliminate():
    """
    列表上下有相同项，删除相同项，并在上方补充1到5的随机数
    :return:
    """
    move_matrix()
    for list in map:
        global list_merge
        list_merge=list
        eliminate_same_broadwise()
    move_matrix()

up_down_eliminate()
print(map)




















































































































