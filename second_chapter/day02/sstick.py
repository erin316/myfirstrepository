"""
 sstick.py 栈模型的顺序存储

#思路总结
1。列表即顺序存储，但功能多，不符合栈的模型特征
2。利用列表将其封装，提供接口方法
"""

class StackError(Exception):
    """
    定义栈的错误提醒
    """
    pass

class Sstack:
    def __init__(self):
        #空列表就是栈的存储空间
        #列表的最后一个元素作为栈顶
        self.__elems=[]

    #定义元素入栈
    def push(self,value):
        self.__elems.append(value)

    #弹出栈的元素
    def pop(self):
        if self.__elems==[]:
            raise StackError("该栈为空")
        self.__elems.pop()
    #打印栈顶元素
    def top(self):
        if self.__elems==[]:
            raise StackError("该栈为空")
        return self.__elems[-1]

if __name__=="__main__":
    st=Sstack()

























