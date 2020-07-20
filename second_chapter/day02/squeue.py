
class Squeue:
    def __init__(self):
        self._list=[]

    def is_empty(self):
        if len(self._list)==0:
            print("该队列为空")

    def enqueue(self,val):
        if len(self._list)>10:
            raise Exception("该栈已满")
        else:
            self._list.append(val)

    def dequeue(self):
        if len(self._list)<0:
            raise Exception("该栈已为空")
        else:
            self._list.pop(0)
    def show(self):
        for item in self._list:
            print(item)

if __name__=="__main__":
    s=Squeue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.show()
    s.dequeue()
    s.show()





























