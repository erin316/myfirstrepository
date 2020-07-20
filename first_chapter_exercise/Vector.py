
list01=[
    ["00","01","02","03"],
    ["10","11","12","13"],
    ["20","21","22","23"]
]
class Vector2:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @staticmethod
    def left():
        return Vector2(0,-1)
    @staticmethod
    def right():
        return Vector2(0,1)
    @staticmethod
    def up():
        return Vector2(-1,0)
    @staticmethod
    def down():
        return Vector2(1,0)

class DoubleListHelper:
    @staticmethod
    def get_element(Target,vect_pos,vect_dir,count):
        result=[]
        for i in range(count):
            vect_pos.x+=vect_dir.x
            vect_pos.y+=vect_dir.y
            element=Target[vect_pos.x][vect_pos.y]
            result.append(element)
        return result
# re=DoubleListHelper.get_element(list01,Vector2(2,3),Vector2.left(),2)
# print(re)
    @staticmethod
    def get_pos(element):
        for x in range(0,len(list01)):
            for y in range(0,len(list01[x])):
                if list01[x][y]==element:
                    return Vector2(x,y)

# print(DoubleListHelper.get_pos("13").x,DoubleListHelper.get_pos("13").y)
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("13"),Vector2.left(),3)
# print(re)
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("22"),Vector2.up(),2)
# print(re)
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("03"),Vector2.down(),2)
# print(re)

