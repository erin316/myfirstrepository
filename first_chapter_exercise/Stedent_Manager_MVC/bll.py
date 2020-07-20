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
