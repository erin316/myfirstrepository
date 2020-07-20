from bll import StudentManagerController
from model import StudentModle

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