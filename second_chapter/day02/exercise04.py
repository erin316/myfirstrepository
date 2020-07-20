class Node:
    def __init__(self,val,next=None):
        """
        创建节点类
        :param val: 节点值
        :param next: 连接下一个节点
        """
        self.val=val
        self.next=next


class Link_list:
    """
    单链表，生成链表后可以实现增删改查的功能
    """
    def __init__(self):
        self.head=Node(None)

    def init_list(self,target_list):
        p=self.head
        for item in target_list:
            p.next=Node(item)
            p=p.next

    def show(self):
        p=self.head.next
        while p is not None:
            print(p.val)
            p=p.next

    def is_empty(self):
        if self.head.next is None:
            return True
        else:
            return False

    def append(self,val):
        p=self.head
        while p.next is not None:
            p=p.next
        p.next=Node(val)

    def clear(self):
        self.head.next=None

    def push(self,index,val):
        p=self.head
        i=0
        while i<index:
            if p.next is None:
                break
            p=p.next
            i+=1
        node=Node(val)
        mark=p.next
        p.next=node
        node.next=mark


list01=[1,2,3,4]
l=Link_list()
l.init_list(list01)
l.push(2,5)
l.show()
print(l.is_empty())


























