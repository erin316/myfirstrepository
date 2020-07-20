class Node:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class Lqueue:
    def __init__(self):
        self.front=self.rear=Node(None)

    def push(self,val):
        self.rear.next=Node(val)
        self.rear=self.rear.next

    def is_empty(self):
        if self.front==self.rear:
            return False

    def pop(self):
        self.front=self.front.next
        return self.front.val

if __name__=="__main__":
    s=Lqueue()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())


























