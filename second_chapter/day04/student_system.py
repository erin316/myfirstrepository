import re
def menu():
    # 输出菜单
    print('''
    ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字键选择菜单          │
    ╚———————————————————————╝
    ''')

def select():
    option_dict = {"0": "exit_stu", "1": "add_student", "2": "find_stu", "3": "del_stu", "4": "update_stu",
                   "5": "sort_stu", "6": "get_sum", "7": "show_stu"}
    while True:
        option_input = input("请输入选项：")
        option=re.sub("\D","",option_input)
        for key,val in option_dict.items():
            if option==key:
                eval(val)()

def add_student():
    with open("student_info.txt","a") as stu_file:
        mark=True
        while mark:
            try:
                id=int(input("请输入ID:"))
                if not id:
                    break
                name=input("请输入姓名:")
                if not name:
                    break
                score=int(input("请输入成绩:"))
            except:
                print("您输入有误！")
            student_dict={"id":id,"name":name,"score":score}
            ss=input("是否还要添加")
            if ss=="n":
                mark=False
            stu_file.write(str(student_dict)+"\n")

def del_stu():
    with open("student_info.txt","a+") as stu_file:
        stu=stu_file.readlines()
        name=input("请输入要删除的学生姓名")
        repeat_stu=show(name)
        for item in repeat_stu:
            print(item)
        del_stu_id=input("请输入您要删除的学生ID")
        for item in stu:
            if eval(item)["id"]==del_stu_id:
                re.sub(f"{item}","",stu_file.read())

def show(name01):
    repeat_stu=[]
    with open("student_info.txt","r") as stu_file:
        f=stu_file.readlines()
        for item in f:
            if eval(item)["name"]==name01:
                repeat_stu.append(eval(item))
    return repeat_stu

def show_stu():
    with open("student_info.txt", "r") as stu_file:
        f=stu_file.readlines()
        print("id")
        for item in f:
            print(eval(item))

def main():
    while True:
        menu()
        select()




if __name__ == '__main__':
    main()






