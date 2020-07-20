"""
2048游戏核心算法
"""

#1.零元素移至末尾
#[2,0,2,0]--->[2,2,0,0]
#[2,0,0,2]--->[2,2,0,0]
#[2,4,0,2]--->[2,4,2,0]

list_merge=None

def zero_to_end():
    """
    将零元素移至末尾
    :param list_merge:列表
    :return:零元素移至末尾的列表
    """
    for i in range(-1,-len(list_merge)-1,-1):
        if list_merge[i] ==0:
            del list_merge[i]
            list_merge.append(0)

# zero_to_end()
# print(list_merge)

def merge():
    """
    现将中间零元素移至末尾
    合并相邻相同的元素
    """
    zero_to_end()
    for i in range(0,len(list_merge)-1):
         if list_merge[i]==list_merge[i+1]:
            list_merge[i]+=list_merge[i+1]
            del list_merge[i+1]
            list_merge.append(0)
# merge()
# print(list_merge)

map=[
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2]
]

def left_move():
    """
    地图列表向左移动将零元素移至末尾后合并相邻相同的元素
    :param map:
    :return:
    """
    for list in map:
        global list_merge
        list_merge=list
        merge()
# left_move()
# print(map)

def right_move():
    """
    地图列表向右移动将零元素移至末尾后合并相邻相同的元素
    :param map:
    :return:
    """
    for line in map:
        global list_merge
        list_merge=line[::-1]
        merge()
        line[::-1]=list_merge

# right_move()
# print(map)


def move_matrix():
    for i in range(0,len(map)):
        for s in range(i,len(map)):
            map[i][s],map[s][i]=map[s][i],map[i][s]
    return map

def up_move():
    move_matrix()
    left_move()
    move_matrix()

# up_move()
# print(map)

def down_move():
    move_matrix()
    right_move()
    move_matrix()

down_move()
print(map)










