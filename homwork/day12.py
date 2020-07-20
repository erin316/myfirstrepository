"""
    2048 游戏核心算法
"""

list_merge = [2, 0, 2, 0]


# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 测试
# zero_to_end()
# print(list_merge)

# zero_to_end()
# print(list_merge)

# 2. 定义合并函数(向左移动的核心算法)　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()
    # [4,4,4,4]
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)

# merge()
# print(list_merge)

# 作业
list_map = [
    [2, 0, 2, 0],
    [2, 0, 0, 2],
    [4, 4, 4, 4],
    [2, 0, 4, 2],
]
# 3. 定义向左移动函数,改变list_map中的数据
#    思路：将list_map每行赋值给list_merge
#         调用合并函数(练习2)

def left_move():
    global list_merge
    for item in list_map:
        list_merge=item
        merge()
# left_move()
# for item in list_map:
#     print(item)

# 4. 定义向右移动函数,改变list_map中的数据
#    思路：将list_map每行,反转,赋值给list_merge
#         调用合并函数
#         将list_merge反转后赋值给list_map

def right_move():
    global list_merge
    for item in list_map:
        list_merge=item[::-1]
        merge()
        item[::-1]=list_merge

# right_move()
# for item in list_map:
#     print(item)

def transfer():
    for item01 in range(len(list_map)):
        for item02 in range(item01,len(list_map[item01])):
            list_map[item01][item02],list_map[item02][item01]=\
                list_map[item02][item01],list_map[item01][item02]

# transfer()
# for item in list_map:
#     print(item)

def up_move():
    transfer()
    left_move()
    transfer()

# up_move()
# for item in list_map:
#     print(item)

def down_move():
    transfer()
    right_move()
    transfer()

# down_move()
# for item in list_map:
#     print(item)

# 5.  使用面向对象思想,描述下列情景.
#     张无忌使用乾坤大挪移(眩晕+伤害)攻击
#     张无忌使用九阳神功(伤害+击飞)攻击
#     还可能使用其他技能攻击
#     要求：增加其他技能，人的代码不变。

class Person:
    def __init__(self,name):
        self.name=name
    def attack(self,skill,*args):
        print(f"{self.name}使用{skill.name}{skill.act(*args)}攻击")
class Skill:
    def __init__(self,name):
        self.name=name
    def act(self,*args):
        pass
class Qiankun(Skill):
    def __init__(self, name):
        super().__init__(name)
    def act(self, *args):
        target_list=[]
        for item in args:
            target_list.append(item.act01())
        return (target_list)

class Damage:
    def __init__(self,name):
        self.name=name
    def act01(self):
        return self.name

p01=Person("张无忌")
q01=Qiankun("乾坤大挪移")
q02=Qiankun("九阳神功")
d01=Damage("伤害")
d02=Damage("眩晕")
d03=Damage("踢腿")

p01.attack(q02,d01,d02,d03)










