"""
定义栈
"""
class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next
class Lsstack:
    def __init__(self):
        self._top=None

    def is_empty(self):
        if self._top==None:
            print("该栈为空")

    def push(self,val):
        self._top=Node(val,self._top)

    def pop(self):
        if self._top==None:
            raise ValueError("栈顶已为空")
        value=self._top.val
        self._top=self._top.next
        return value
    def top(self):
        if self._top==None:
            raise ValueError("栈顶已为空")
        return self._top.val

if __name__=="__main__":
    l=Lsstack()
    l.push(1)
    l.push(2)
    l.push(3)
    print(l.top())
    l.pop()
    print(l.top())


























































