"""
实现单链表的构建和功能操作
"""

#创建节点类
class Node:
    """
    思路：将自丁隐的类视为节点的生成类，实现对象中包含数据部分和指向下一个节点的next
    """
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class LinkList:
    """
    思路：单链表类，生成对象可以进行增删改查操作，具体操作通过调用具体方法完成
    """
    def __init__(self):
        self.head=Node(None)

    #通过list_为链表添加一组节点
    def init_list(self,list_):
        p=self.head
        for item in list_:
            p.next=Node(item)
            p=p.next

    #遍历链表
    def show(self):
        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next
    #判断链表为空
    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    #清空链表
    def clear(self):
        self.head.next=None

    #尾部插入
    def append(self,val):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=Node(val)

    #头部插入
    def head_insert(self,val):
        node=Node(val)
        node.next=self.head.next
        self.head.next=node

    #指定插入位置
    def insert(self,index,val):
        p=self.head
        for i in range(index):
            if p.next is None:
                break
            p=p.next

        node=Node(val)
        node.next=p.next
        p.next=node

    #删除节点
    def delete(self,x):
        p=self.head
        while p.next and p.next.val !=x:
            p=p.next

        if p.next is None:
            raise ValueError("无该值")
        else:
            p.next=p.next.next

        #获取某个节点值，传入节点位置获取节点值

    def get_index(self,index):
        if index<0:
            raise IndexError("index out of range")
        p=self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range")
            p=p.next
        return p.val


l=LinkList()
l.init_list([1,2,3,4,5])
l.delete(2)
l.show()


































