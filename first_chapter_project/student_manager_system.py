"""
学生管理系统
项目计划：
    1.完成数据模型StudentModel
    2.创建逻辑控制类StudentManagerController
    3.完成数据：学生列表__stu_list
    4.行为：获取列表stu_list
    5.添加学生方法 add_studend
    6.根据学生删除学生remove_student
"""
class StudentModle:

    def __init__(self,name="",age=0,score=0,id=0):
        self.id=id
        self.name=name
        self.age=age
        self.score=score
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name=value
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,value):
        if 0<=value<=100:
            self.__age=value
        else:
            raise ValueError("年龄范围应在0到100之间")
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if 0<=value<=100:
            self.__score=value
        else:
            raise ValueError("请输入正确的成绩")

class StudentManagerController:
    #类的初始变量，可以被创建的对象共用
    __init_id=1000
    def __init__(self):
        self.__stu_list=[]
    @property
    def stu_list(self):
        return self.__stu_list
    def add_student(self,stu_info):
        stu_info.id=self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.__init_id +=1
        return StudentManagerController.__init_id

    def remove_student(self,id):
        for item in self.stu_list:
            if item.id==id:
                self.__stu_list.remove(item)
                print("删除成功")
            else:
                raise ValueError("该学生不存在！")

    def update_info(self,student):
        for item in self.__stu_list:
            if item.id==student.id:
                item.name=student.name
                item.score=student.score
                item.age=student.age
                return True
        return False

    def sort_score(self):
        for i in range(len(self.stu_list)):
            for s in range(i,len(self.stu_list)):
                if self.stu_list[s].score<self.stu_list[i].score:
                    self.stu_list[i].score,self.stu_list[s].score=self.stu_list[s].score,self.stu_list[i].score

class StudentManagerView:
    def __init__(self):
        self.__manager = StudentManagerController()
    def __display(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")
    def __select_menue(self):
        self.__display()
        item=input("请输入编号")
        if item=="1":
            self.__input_student()
        if item=="2":
            self.__output_student(self.__manager.stu_list)
        if item=="3":
            self.__remove_student()
        if item=="4":
            self.__modify_student()
        if item=="5":
            self.__sort_student_score()
    def __input_student(self):
        name=input("请输入姓名")
        age=int(input("请输入年龄"))
        score=int(input("请输入成绩"))
        stu=StudentModle(name,age,score)
        self.__manager.add_student(stu)
    def __output_student(self,student_list):
        for item in student_list:
            print(item.id,item.name,item.age,item.score)
    def __remove_student(self):
        stu_id=int(input("请输入要删除的学生ID:"))
        self.__manager.remove_student(stu_id)
        self.__output_student(self.__manager.stu_list)
    def __modify_student(self):
        id=int(input("请输入要更新的学生ID"))
        for item  in self.__manager.stu_list:
            if item.id !=id:
                raise ValueError("请输入正常的学生ID")
        name=input("请输入要更新的学生姓名")
        age=int(input("请输入要更新的学生年龄"))
        score=int(input("请输入要更新的学生成绩"))
        modify_stu=StudentModle(name,age,score,id)
        self.__manager.update_info(modify_stu)
    def __sort_student_score(self):
        self.__manager.sort_score()
        self.__output_student(self.__manager.stu_list)
        self.__display()
    def main(self):
        while True:
            self.__select_menue()

view=StudentManagerView()
view.main()


# for item in manager.stu_list:
#     print(item.name,item.id,item.score)
# manager.update_info(StudentModle("dd",2,45,1002))
# # manager.remove_student(1001)
# for item in manager.stu_list:
#     print(item.name,item.id,item.score)



































