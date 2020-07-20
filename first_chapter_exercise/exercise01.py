'''
开头
'''
# n=int(input("请输入美元"))
# m=n*6.9
# # print("结果为:%s"%m)
#
# print(5//2)
# print(5%2)
# print(5/2)
# price=float(input("请录入商品价格："))
# qty=int(input("请录入商品数量："))
# money=float(input("请录入获取金额："))
# out=money-price*qty
# if out>0:
#     print("应找回零钱%s"%out)
# else:
#     print("您还应付%s元"%(price*qty-money))
#
# minute=float(input("请输入分钟"))
# hour=float(input("请输入小时"))
# day=float(input("请输入天"))
# second=day*24*(60**2)+hour*(60**2)+minute*60
# print("总秒数为：%s"%second)

# m=float(input("请输入两数："))
# jin=m//16
# liang=m%16
# print("其为%s斤"%jin+"%s两"%liang)


# distance=float(input("请输入距离："))
# time=float(input("请输入时间："))
# rate=float(input("请输入初速度："))
# rate_pro=(distance-rate*time)*2/(time**2)
# print("其加速度为：%s"%rate_pro)


# input_int=int(input("请输入一个四位的整数："))
# ge=input_int%1000%100%10
# shi=input_int%1000%100//10
# bai=input_int%1000//100
# qian=input_int//1000
# sum=ge+shi+bai+qian
# print("其四位整数数字只和为:%s"%sum)

# year=int(input('请输入年份：'))
# if year%4==0 and year%100 !=0:
#     print("该年份为闰年")
# elif year % 400==0:
#     print("该年为闰年")
# else:
#     print("该年为平年")

# a=10
# print("你好","nihao%s"%a)

# input_second=int(input("请输入秒数："))
# hour=input_second//3600
# minute=input_second%3600//60
# second=input_second%3600%60
# print("其为%s小时"%hour,"%s分钟"%minute,"%s秒"%second)
#


# quarter=input('请输入季度：')
# if quarter=="春":
#     print("春季的月份为一月&二月&三月")
# elif quarter=="夏":
#     print("夏季的月份为四月&五月&六月")
# elif quarter=="秋":
#     print("秋天的月份为七月&八月&九月")
# elif quarter=="冬":
#     print("冬天的月份为十月&十一月&十二月")
# else:
#     print("请输入正确的月份")

# data1=int(input("请输入一个数字："))
# sign=input("请输入一个运算符(+，-，*，/)")
# data2=int(input('请录入一个数字：'))
# jia=data1+data2
# jian=data1-data2
# mul=data1*data2
# chu=data1/data2
# if sign=="+":
#     print("%s"%data1,"+","%s"%data2,"==",jia)
# elif sign=="-":
#     print("%s"%data1,"-","%s"%data2,"==",jian)
# elif sign=="*":
#     print("%s"%data1,"*","%s"%data2,"==",mul)
# elif sign=="/":
#     if data2==0:
#         print("分母不能为0")
#     else:
#         print("%s"%data1,"/","%s"%data2,"==",chu)
# else:
#     print("运算符有误")


# number1=int(input("请输入数字1："))
# number2=int(input("请输入数字2："))
# number3=int(input("请输入数字3："))
# number4=int(input("请输入数字4："))
# if number1>number2:
#     if number1>number3:
#         if number1>number4:
#             print('最大数为：',number1)
#     else:
#         if number3>number4:
#             print("最大数为：",number3)
#         else:
#             print("最大数为：",number4)
# else:
#     if number2>number3:
#         if number2>number4:
#             print("最大数为",number2)
#     else:
#         if number3>number4:
#             print("最大数为",number3)
#         else:
#             print("最大数为",number4)

#
# score=float(input('请输入一个成绩：'))
# if 90<= score<=100:
#     print("优秀")
# elif score>=70 and score<90:
#     print('良好')
# elif score>=60 and score<70:
#     print('及格')
# elif 0<=score<60:
#     print('不及格')
# else:
#     print('输入有误')
#


# month=input('请输入一个月份：')
# if not month:
#     print('输入有误')
# else:
#     month01=int(month)
#     if month01 in [1,3,5,7,8,10,12]:
#         print(month01,'月的天数为：31天')
#     elif month01 in [4,6,9,11]:
#         print(month01,'月的天数为30天')
#     elif month01==2:
#         print('二月的天数为28天')
#     else:
#         print('输入有误')
#
# data=int(input('请输入一个整数：'))
# sort="偶数" if not data%2 else '奇数'
# print(sort)

# year= int(input('请输入一个年份：'))
# day=29 if (not year%4 and year%100) or not year % 400 else 28
# print(day)

# year=int(input('请输入年份：'))
# if year%4==0 and year%100 !=0:
#     print("该年份为闰年")
# elif year % 400==0:
#     print("该年为闰年")
# else:
#     print("该年为平年")

# while True:
#     quarter=input('请输入季度:')
#     if quarter=="春":
#         print("春季的月份为一月&二月&三月")
#     elif quarter=="夏":
#         print("夏季的月份为四月&五月&六月")
#     elif quarter=="秋":
#         print("秋天的月份为七月&八月&九月")
#     elif quarter=="冬":
#         print("冬天的月份为十月&十一月&十二月")
#     elif quarter=="e":
#         break
#     else:
#         print("请输入正确的月份")
#
# count=0
# while count<=5:
#     print(count,end=" ")
#     count+=1
#
# count=2
# while count<=7:
#     print(count,end=" ")
#     count+=1
#
# count=0
# while count<=6:
#     print(count,end=" ")
#     count+=2
#



# weigh=float(input('请输入您的体重：'))
# height=float(input('请输入您的身高：'))
# BMI=weigh/height**5
# if BMI<=0 or BMI>=100:
#     print('那不可能')
# elif BMI<18.5:
#     print('您的体重过低')
# elif BMI<24:
#     print('您的体重正常')
# elif BMI<28:
#     print('您的体重超重')
# elif BMI<30:
#     print('您的体重I级肥胖')
# elif BMI<40:
#     print('您的体重II级肥胖')
# else:
#     print('您的体重III级肥胖')



# start=int(input('请输入一个开始值'))
# end=int(input('请输入一个结束值'))
# count=start+1
# while count<end:
#     print(count)
#     count += 1


# thickness=0.01*0.001
# time=0
# while thickness<=8844.43:
#     time+=1
#     thickness=thickness*2
# print("对折次数为:",time)

#
# import random
# random_number=random.randint(1,100)
# time=0
# while time<3:
#     number = int(input("请输入你猜的数字"))
#     time+=1
#     if number<random_number:
#         print("小了")
#     elif number>random_number:
#         print("大了")
#     else:
#         print("恭喜你猜对了！,次数为：%s"%time)
#         break
# else:
#     print("次数超过3次，游戏结束！")
#

# time=0
# while time<3:
#     score=(input('请输入一个成绩：'))
#     if not score:
#         break
#     score01 = int(score)
#     if 90<= score01<=100:
#         print("优秀")
#     elif score01>=70 and score01<90:
#         print('良好')
#     elif score01>=60 and score01<70:
#         print('及格')
#     elif 0<=score01<60:
#         print('不及格')
#     else:
#         time+=1
#         print('输入有误')
# else:
#     print("成绩错误过多！")


# sum=0
# for i in range(1,101):
#     sum+=i
# print('1到100的和为：',sum)

# sum01=0
# for i in range(2,101,2):
#     sum01+=i
# print('2+4+6+....100的和为：',sum01)

# sum02=0
# for i in range(10,37):
#     sum02+=i
# print('10到36的和为：',sum02)


# import random
# score=0
# for i in range(0,3):
#     data1=random.randint(1,10)
#     data2=random.randint(1,10)
#     result=data1+data2
#     input_result=int(input("请输入"+str(data1)+"+"+str(data2)+"="))
#     if input_result==result:
#         score+=10
# print("总分为：",str(score))


# number=int(input("请输入一个整数："))
# count=0
# for i in range(2,number):
#     if number%i==0:
#         count+=1
# if count==0:
#     print(str(number)+"为素数")
# else:
#     print(str(number) + "不为素数")
#
# sum=0
# for i in range(10,51):
#     number=i%10
#     if number in [2,5,9]:
#         continue
#     sum+=i
# print("和为："+str(sum))

# character=input("请输入一个字符串：")
# for i in character:
#     number = ord(i)
#     print(i+"的编码为：%s"%number)


# while True:
#     number=(input("请输入一个编码值："))
#     if not number:
#         break
#     else:
#         number01=int(number)
#         print("%s编码值的字符为："%number01+chr(number01))


# character=input("请输入一个字符串")
# print(character[0])
# print(character[-1])
# print(character[-3:-2])
# print(character[:2])
# print(character[::-1])
# if len(character)%2==1:
#     len01=len(character)//2
#     print(character[len01:len01+1])

# name="悟空"
# age=800
# score=99.5
# print("我叫%s,年龄%d,成绩%.1f"%(name,age,score))

# number=int(input("请输入一个整数："))
# print("*"*number)
# for i in range(2,number):
#     print("*",""*(number-2),"*")
# print("*"*number)


# character=input("请输入一个回文字符串")
# character01=character[::-1]
# if character==character01:
#     print("该字符串是回文")
# else:
#     print("该字符串不是回文")


# height=100
# count=0
# height01=height
# while height/2>0.01:
#     height=height/2
#     height01 +=height*2
#     count+=1
# print("小球总共弹起%d次"%count)
# print("总共走了%f米"%height01)

#
# print("看教程 www.runoob.com")
# print("看文档 docs.python.org/zh-cn/3/")
# print("逛社区 www.pythontab.com")
#

# container=[]
# while True:
#     character=input("请输入西游记中你喜欢的人物：")
#     if not character:
#         length=len(container)
#         for i in range(0,length):
#             print(container[i],end="\n")
#         break
#
#     else:
#         container.append(character)


# score=[]
# student=['孙悟空','猪八戒','唐僧','沙僧']
# len_student=len(student)
# for i in range(0,len_student):
#     character=input("请输入%s的成绩"%student[i])
#     if not character:
#         len_score=len(score)
#         for i in range(0,len_score):
#             print("%s的成绩为%s"%(student[i],score[i]))
#         break
#
#     else:
#         score.append(float(character))
#
# max_score=max(score)
# min_score=min(score)
# avg_score=sum(score)/len(student)
# print("最高成绩为%s,同学为%s"%(max_score,student[score.index(max_score)]))
# print("最低成绩为%s,同学为%s"%(min_score,student[score.index(min_score)]))
# print("平均成绩为%s"%avg_score)

#
# student=[]
# while True:
#     str_student=input("请输入学生姓名：")
#     if str_student in student:
#         continue
#     else:
#         student.append(str_student)
#     if not str_student:
#         len_student=len(student)
#         for i in range(len_student-1,-1,-1):
#             print(student[i])
#         break
#

# list01=[54,36,12,42,35,17]
# list02=[]
# for i in list01:
#     if i>30:
#         list02.append(i)
# print(list02)


# list=[]
# for i in range(0,5):
#     input_data=int(input("请输入第%s个数字"%(i+1)))
#     list.append(input_data)
# max_data=list[0]
# for i in range(1,len(list)):
#     if max_data<list[i]:
#         max_data=list[i]
# print("最大值为：%s"%max_data)



# list=[9,25,12,8]
# for i in range(len(list)-1,-1,-1):
#     if list[i]>10:
#         list.remove(list[i])
# print(list)

# 字符串拼接
# list01=[]
# while True:
#     character=input("请输入字符串")
#     if not character:
#         break
#     list01.append(character)
# result="".join(list01)
# print(result)


#英文单词翻转
# character=input("请输入一个语句：")
# split_char=character.split(" ")
# list01=[]
# for i in range(len(split_char)-1,-1,-1):
#     list01.append(split_char[i])
# print(" ".join(list01))

#彩票，双色球练习
#生成得奖彩票
# import random
# raffle=[]
# for i in range(0,6):
#     red=random.randint(1,33)
#     raffle.append(red)
# blue=random.randint(1,16)
# raffle.append(blue)
# print("今日彩票为",raffle)
#
# # #购买彩票
# purchase=[]
# while len(purchase)!=1:
#     number=input("请输入您要买的第1个红球号码:")
#     if not number:
#         print("请输入正确信息")
#         continue
#     number01=int(number)
#     if number01 not in range(0,34):
#         print("号码不在[1:33]范围内")
#     else:
#         purchase.append(number01)
# while purchase.index(purchase[-1])<5:
#     number=input("请输入您要买的第%s个红球号码:"%(purchase.index(purchase[-1])+2))
#     if not number:
#         print("请输入正确数字")
#         continue
#     number01=int(number)
#     if number01 not in range(0,34):
#         print("号码不在[1:33]范围内")
#     elif number01 in purchase:
#         print("该红球号码重复")
#     else:
#         purchase.append(number01)
#     if purchase.index(purchase[-1])==5:
#         break
# blue_number=int(input("请输入您想买的蓝球号码"))
# if blue_number not in range(0,17):
#     print("请重新输入")
# else:
#     purchase.append(blue_number)
# print("您购买的彩票为：",purchase)


# list01=[item**2 for item in range(1,11)]
# print(list01)
# list02=[item for item in list01 if item%2==1]
# print(list02)
# list03=[item for item in list01 if item%2==0]
# print(list03)
# list04=[item+1 for item in list01 if item>5 and item%2==0]
# print(list04)



# month=input('请输入一个月份：')
# if not month:
#     print('输入有误')
# else:
#     month01=int(month)
#     if month01 in (1,3,5,7,8,10,12):
#         print(month01,'月的天数为：31天')
#     elif month01 in (4,6,9,11):
#         print(month01,'月的天数为30天')
#     elif month01==2:
#         print('二月的天数为28天')
#     else:
#         print('输入有误')

# tuple=(31,28,31,30,31,30,31,31,30,31,30,31)
# input_day=input("请输入日期")
# data01=int(input_day[0])
# data02=int(input_day[2])
# day=0
# for i in range(0,data01-1):
#     day+=tuple[i]
# day+=data02
# print("该%s的天数为%s"%(input_day,day))


# dict01={}
# while True:
#     name=input("请输入商品名称：")
#     if not name:
#         break
#     price=int(input("请输入单价"))
#     dict01[name]=price
# for k,v in dict01.items():
#     print(k,v)
# for i in dict01.values():
#     print(i)
# for i in dict01:
#     print(i,dict01[i])


# dict01={}
# while True:
#     name=input("请输入学生姓名:")
#     if not name:
#         break
#     age=input("请输入学生年龄:")
#     score=input("请输入学生成绩:")
#     sex=input("请输入学生性别:")
#     dict01[name]=(age,score,sex)
# for key,values in dict01.items():
#     print("学生%s的年龄为%s,成绩为%s，性别为%s"%(key,values[0],values[1],values[2]))
#

# dict02={}
# while True:
#     name=input("请输入学生姓名:")
#     if not name:
#         break
#     age=input("请输入学生年龄:")
#     score=input("请输入学生成绩:")
#     sex=input("请输入学生性别:")
#     dict02[name]={"年龄:":age, "成绩：":score, "性别:":sex}
# for item in dict02.items():
#     print(item)

# list01=[]
# while True:
#     name=input("请输入学生姓名:")
#     if not name:
#         break
#     age=input("请输入学生年龄:")
#     score=input("请输入学生成绩:")
#     sex=input("请输入学生性别:")
#     dict02={"姓名：":name,"年龄:":age, "成绩：":score, "性别:":sex}
#     list01.append(dict02)
# for item in range(0,2):
#     print(list01[item])
#

# dict01={}
# while True:
#     name=input("请输入姓名：")
#     if not name:
#         break
#     i = 1
#     list01=[]
#     while True:
#         interest=input("请输入您的第%s个兴趣爱好："%i)
#         if not interest:
#             break
#         list01.append(interest)
#         dict01[name]=list01
#         i+=1
# for name,interest in dict01.items():
#     print("%s的兴趣爱好为%s"%(name,interest))


# list_year=[]
# for year in range(1970,2051):
#     if (year%4==0 and year%100 !=0) or year % 400==0:
#         list_year.append(year)
# print(list_year)

# dict01={"北京":[{"景区":"故宫，天安门，天坛"},{"美食":"烤鸭，炸酱面，豆汁，卤煮"}],"四川":[{"景区":"九寨沟，峨眉山，春熙路"},{"美食":"火锅，串串香，兔头"}]}
#
# for key,values in dict01.items():
#     print('''%s:
#         %s
#         %s
#           '''%(key,values[0],values[1]))


# dict01={}
# while True:
#     character = input("请输入字符串:")
#     if not character:
#         break
#
#     for i in range(0,len(character)):
#         count=1
#         if character[i] in dict01:
#             continue
#         for s in range(i+1,len(character)):
#
#             if character[i]==character[s]:
#                 count+=1
#         dict01[character[i]]=count
# for key,values in dict01.items():
#     print("字符串%s的出现次数为：%s"%(key,values))

# list01=["ss","www","deswd"]
#
# dict01={i:len(i) for i in list01}
# print(dict01)
#
# list01=["ss","www","deswd"]
# list02=[101,102,103]
# dict01={list01[i]:list02[i] for i in range(0,len(list01))}
# print(dict01)

# set01=set()
# while True:
#     character=input("请输入字符串:")
#     if not character:
#         break
#     set01.add(character)
# print(set01)


# manager={"曹操","刘备","孙权"}
# tel={"曹操","刘备","张飞","关羽"}
# print("是技术也是经理的有%s"%(manager&tel))
# print("是经理，不是技术的有%s"%(manager-tel))
# print("是技术，不是经理的有%s"%(tel-manager))
# if "张飞" in manager:
#     print("张飞是经理")
# print("张飞不是经理")
#
# print("身兼一职的都有%s"%(manager^tel))
# print("经理和技术总共有%s人"%(len(manager|tel)))
#

# for i in range(4):
#     for s in range(4):
#         if s%2==0:
#             print("*",end=" ")
#         else:
#             print("#",end=" ")
#     print()
#


# list01=[3,80,45,7,1]
# for i in range(0,len(list01)):
#     for s in range(i+1,len(list01)):
#         if list01[i]<list01[s]:
#             continue
#         else:
#             list01[i],list01[s]=list01[s],list01[i]
# print(list01)


# list01=[3,45,5,80,1]
# eq_list01=[]
# for i in range(0,len(list01)):
#     for s in range(i+1,len(list01)):
#         if list01[i]==list01[s]:
#             eq_list01.append(list01[i])
# if eq_list01 ==[]:
#     print("无发现相同项",list01)
# else:
#     print("相同元素为：",eq_list01)

# list01=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# print(list01[1][2])
# print(list01[2])
# for i in list01[0]:
#     print(i)
# for i in list01:
#     print(i[0])

# list01=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# list03=[]
# for i in range(0,len(list01)):
#     list02 = []
#     for s in range(0,len(list01[i])):
#         list02.append(list01[s][i])
#     list03.append(list02)
# print(list03)

# list01=["x","p","h"]
# list02=["k","n"]
# list03=[i+s for i in list01 for s in list02]
# print(list03)
#

# def draw_print(row,column):
#
#     for i in range(row):
#         for c in range(column):
#             print("*",end=" ")
#         print()
# draw_print(4,4)

# list01=[1,2,3]
# list02=[4,5,6]
# def print_row(list):
#     """
#
#     :param list01: 填入容器
#     :return: 返回容器的值并打印
#     """
#     for i in range(0,len(list)):
#         print(list[i])
#
# print_row(list01)
# print_row(list02)

# list01=[
#     [1,2,3,44],
#     [4,5,5,6,65,6,87],
#     [7,5]
# ]
# def print_list(list):
#     for i in list:
#         for s in i:
#             print(s,end=" ")
#         print()
#
# print_list(list01)

#
# list01=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# for i in range(0,len(list01)):
#     for s in range(i,len(list01[i])):
#         list01[i][s],list01[s][i]=list01[s][i],list01[i][s]
#
# print(list01)

# def data_sum(s):
#     """
#     计算整数的每位相加和
#     :param s: 四位整数
#     :return:
#     """
#     s=int(s)
#     ge=s%1000%100%10
#     shi=s%1000%100//10
#     bai=s%1000//100
#     qian=s//1000
#     sum=ge+shi+bai+qian
#     return sum
#
# data_sum(5428)

# def cal_jin_liang(liang):
#     """
#     换算两到斤两
#     :param liang: 两数
#     :return:元组（斤，两）
#     """
#     jin=liang//16
#     liang=liang%16
#     return (jin,liang)
#
# s=cal_jin_liang()
# print(s)


# def assess_score_level(score):
#     """
#     依据成绩评估其等级(优秀，良好，及格，不及格)
#     :param score: 成绩
#     :return: 等级(优秀，良好，及格，不及格)
#     """
#     if 90<= score<=100:
#         return "优秀"
#     if score>=70 and score<90:
#         return '良好'
#     if score>=60 and score<70:
#         return '及格'
#     if 0<=score<60:
#         return '不及格'
#
#     return '输入有误'
# s=assess_score_level(80)
# print(s)

# def judge_same_unit(list01):
#     """
#     判断列表是否有相同的元素
#     :param list01: 列表
#     :return:元组(说明，相同项)
#     """
#     eq_list01=[]
#     for i in range(0,len(list01)):
#         for s in range(i+1,len(list01)):
#             if list01[i]==list01[s]:
#                 eq_list01.append(list01[i])
#     if eq_list01 ==[]:
#         return False
#
#     return True
# s=judge_same_unit([2,3,4,5])
# print(s)


# year=int(input('请输入年份：'))
# if (year%4==0 and year%100 !=0) or year % 400==0:
#     print("该年份为闰年")
# else:
#     print("该年为平年")
#
# def get_day_by_month(year,month):
#     """
#     输入年月，判断该月有多少天
#     :param year: int(年)
#     :param month: int(月)
#     :return: tuple(年，月，天数)
#     """
#     if month in [1,3,5,7,8,10,12]:
#         return(year,month,31)
#     if month in [4,6,9,11]:
#         return(year,month,30)
#     if month==2:
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             return (year,month,29)
#         return (year, month, 28)
#     return (year, month, 0)
# s=get_day_by_month(2134,13)
# print(s)

# def is_leap_year(year):
#     return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# print(is_leap_year(2020))


# def up_sort(list):
#     """
#     对列表进行升序排序
#     :param list: 列表
#     :return: 升序后的列表
#     """
#     for i in range(0,len(list)):
#         for s in range(i+1,len(list)):
#             if list[i]<list[s]:
#                 continue
#             else:
#                 list[i],list[s]=list[s],list[i]
#
# list01=[2,4,3,2,12,4]
# print(up_sort(list01))
#
# print(list01)

# def reversal_list(list):
#     """
#     将方阵列表的行列交换
#     :param list: 方阵列表
#     """
#     for i in range(0,len(list)):
#         for s in range(i,len(list[i])):
#             list[i][s],list[s][i]=list[s][i],list[i][s]
# list01=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]
# ]
# reversal_list(list01)
# print(list01)

#记录函数调用的次数
# count=0
# def cal_time():
#     pass
#     global count
#     count+=1
# cal_time()
# cal_time()
# print(count)
#
# def c(a,b,c,d):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
# # c(1,2,3,4)
# # c(a=1,c=2,b=3,d=4)
# # list01=[1,2,3,4]
# # c(*list01)
# dict={"a":1,"b":2,"c":3,"d":4}
# c(**dict)

# def get_second(hour=0,minute=0,second=0):
#     sum_second=hour*3600+minute*60+second
#     return sum_second
# print(get_second(1,2,3))

# def c(*a):
#     print(a)
# c()
# c(1)
# c(1,2)

# def get_sum(*args):
#     sum01=0
#     for i in args:
#         sum01+=i
#     return sum01
# print(get_sum(1,2,3))

# a=[1,2]
# b=[1,2]
# print(a is b)
# print(a==b)


# number=int(input("请输入一个整数："))
# count=0
# for i in range(2,number):
#     if number%i==0:
#         count+=1
# if count==0:
#     print(str(number)+"为素数")
# else:
#     print(str(number) + "不为素数")


# str01="  校 训：自强不息、厚德载物。  "
# print(str01.count(" "))
# print(str01.strip(" "))
# print(str01.replace(" ",""))
# print(str01.find("载物"))
# print(str01.startswith("校训"))
#

# def fun07(a,b,*args,c,d,**kwargs):
#     pass
# fun07(1,2,c=0,d=0)

# def fun01(*args,**kwargs):
#     print(args)
#     print(kwargs)
# fun01(0,1,2,a=6,d=3,e="ee")

#
# def prime(number):
#     count=0
#     for i in range(2,number):
#         if number%i==0:
#             count+=1
#     if count==0:
#         return True
#     return False
#
#
# def primer_count(start,end):
#     prime_return=[]
#     for i in range(start,end+1):
#         result=prime(i)
#         if result==True:
#             prime_return.append(i)
#     return prime_return
# print(primer_count(1,9))


# class Student:
#     def __init__(self,name,age,score,sex):
#         self.name=name
#         self.age=age
#         self.score=score
#         self.sex=sex
#     def print_information(self):
#         print(self.name,self.age,self.score,self.sex)

# list_student=[]
# while True:
#     name=input("请录入姓名：")
#     if not name:
#         break
#     age=input("请录入年龄：")
#     score=input("请录入成绩：")
#     sex=input("请录入性别：")
#     student_information=Student(name,age,score,sex)
#     list_student.append(student_information)
#
# for item in list_student:
#     item.print_information()
#
# info=list_student[0]
# info.print_information()


# class Student:
#     def __init__(self,name,age,score,sex):
#         self.name=name
#         self.age=age
#         self.score=score
#         self.sex=sex
#     def print_information(self):
#         print(self.name,self.age,self.score,self.sex)
#     def find_info(self,name=None,age=None,score=None,sex=None):
#         if self.name==name:
#             print(self.name,self.age,self.score,self.sex)
#         if self.age==age:
#             print(self.name,self.age,self.score,self.sex)
#         if self.score==score:
#             print(self.name,self.age,self.score,self.sex)
#         if self.sex==sex:
#             print(self.name,self.age,self.score,self.sex)

# list01=[
#     Student("a",32,34,'女'),
#     Student("b",13,35,'男'),
#     Student("c",41,26,'女'),
#     Student("d",35,37,'男'),
#     Student("e",26,28,'女')
# ]
# for item in list01:
#     item.find_info( sex="女")

# def find_stu():
#     list_find=[]
#     for item in list01:
#         if item.age>=30:
#             list_find.append(item)
#     count_stu=len(list_find)
#     return count_stu
# print(find_stu())

# def score_to_zero():
#     for item in list01:
#         item.score=0
# score_to_zero()
# for i in list01:
#     print(i.name,i.age,i.score,i.sex)

# def get_name():
#     list=[]
#     for item in list01:
#         list.append(item.name)
#     print(list)
# get_name()

# def get_max_age_stu():
#     max_stu=[]
#     for item in list01:
#         max_stu.append(item.age)
#     max=0
#     for s in range(0,len(max_stu)):
#         if int(max_stu[s])>max:
#             max=max_stu[s]
#     for q in list01:
#         if q.age==max:
#             print(q.name)
# get_max_age_stu()
#

# class Wife:
#     count=0
#     @classmethod
#     def print_count(cls):
#         print(cls.count)
#     def __init__(self,name):
#         self.name=name
#         Wife.count+=1
# Wife("a")
# Wife("b")
# Wife("c")
# Wife.print_count()
#

# list01=[
#     ["00","01","02","03"],
#     ["10","11","12","13"],
#     ["20","21","22","23"]
# ]
#
# class Vector2:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     @staticmethod
#     def left():
#         return Vector2(0,-1)
#     @staticmethod
#     def right():
#         return Vector2(0,1)
#     @staticmethod
#     def up():
#         return Vector2(-1,0)
#     @staticmethod
#     def down():
#         return Vector2(1,0)
# pos01=Vector2(1,2)
# l01=Vector2.left()
# pos01.x+=l01.x
# pos01.y+=l01.y
# print(pos01.x,pos01.y)
# class DoubleListHelper:
#     @staticmethod
#     def get_element(Target,vect_pos,vect_dir,count):
#         result=[]
#         for i in range(count):
#             vect_pos.x+=vect_dir.x
#             vect_pos.y+=vect_dir.y
#             element=Target[vect_pos.x][vect_pos.y]
#             result.append(element)
#         return result
# # re=DoubleListHelper.get_element(list01,Vector2(2,3),Vector2.left(),2)
# # print(re)
#     @staticmethod
#     def get_pos(element):
#         for x in range(0,len(list01)):
#             for y in range(0,len(list01[x])):
#                 if list01[x][y]==element:
#                     return Vector2(x,y)

# print(DoubleListHelper.get_pos("13").x,DoubleListHelper.get_pos("13").y)

# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("13"),Vector2.left(),3)
# print(re)
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("22"),Vector2.up(),2)
# print(re)
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("03"),Vector2.down(),2)
# print(re)

# class enemy:
#     def __init__(self,name,blood,attack,defense):
#         self.name=name
#         self.blood=blood
#         self.attack=attack
#         self.defense=defense
#     def print(self):
#         print(self.name,self.blood,self.attack,self.defense)
# list_enemy=[]
# enemy01=enemy("灭霸",31,40,34)
# list_enemy.append(enemy01)
# enemy02=enemy("灭1",32,41,35)
# list_enemy.append(enemy02)
# enemy03=enemy("灭2",33,42,36)
# list_enemy.append(enemy03)
# enemy04=enemy("灭3",0,43,37)
# list_enemy.append(enemy04)
# avg_attack=0
# for item in list_enemy:
    # if item.name=="灭霸":
    #     print(item.name,item.blood,item.attack,item.defense)
    # if item.blood==0:
    #     print(item.name)
#     avg_attack+=item.attack
# print(avg_attack/len(list_enemy))
#     if item.defense<10:
#         del list_enemy[item]
#     print(item.name)
#     item.attack+=50
#     print(item.name,item.attack)

#
# class enemy:
#     def __init__(self,name,attack,blood):
#         self.name=name
#         self.attack=attack
#         self.blood=blood
#     @property
#     def attack(self):
#         return self.__attack
#     @attack.setter
#     def attack(self,value):
#         if 20<value<100:
#             self.__attack = value
#         else:
#             raise ValueError("攻击力超过范围")
#     @property
#     def blood(self):
#         return self.__blood
#     @blood.setter
#     def blood(self,value):
#         if 20<value<3000:
#             self.__blood=value
#         else:
#             raise ValueError("血量超出范围")
# enemy01=enemy("a",90,80)
# print(enemy01.name,enemy01.attack)
# enemy01.attack=80
# print(enemy01.__dict__)
#

# class Person:
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#     @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self,value):
    #     self.__name=value
    # @property
    # def money(self):
    #     return self.__money
    # @money.setter
    # def money(self,value):
    #     self.__money=value

# class Bank:
#     def __init__(self,name,money):
#         self.name=name
#         self.money=money
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @property
#     def money(self):
#         return self.__money
#     @money.setter
#      def money(self,value):
#         self.__money=value
#     @staticmethod
#     def get_money(person,value):
#         Bank.money-=value
#         person.money+=value
#         print(person.name,"取了%s钱"%value)
#
# person01=Person("小明",0)
# bank01=Bank("工商",10000)
# Bank.get_money(person01,1000)

# class Person:
#     def __init__(self,name,worker,money=0):
#         self.name=name
#         self.worker=worker
    #     self.money=money
    # money=0
    # @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self,value):
    #     self.__name=value
    # @property
    # def worker(self):
    #     return self.__worker
    # @worker.setter
    # def worker(self,value):
    #     self.__worker=value
    # def teach(self,person):
    #     print(self.name,"教%s%s"%(person.name,self.worker))
    # @staticmethod
    # def get_money(person,money):
    #     print(person.name,"挣了%s"%money)
#     @classmethod
#     def get_money(self,person):
#         Person.money+=person.money
#         print(person.name,"挣了%s"%person.money)
#
#
# person01=Person("张无忌","九阳神功",10000)
# person02=Person("赵敏","化妆",6000)
#
# Person.teach(person01,person02)
# Person.get_money(person01)
# class Player:
#     def __init__(self,blood,attack):
#         self.blood=blood
#         self.attack=attack
#     def attack(self,other):
#         print("玩家攻击敌人 ")
#         print("玩家掉装备 ")
#         other.damage(self.attack)
#     def damage(self,value):
#         self.blood-=value
#         if self.blood<=0:
#             self.__death()
#     def __death(self):
#         print("玩家死了")
#
# class Enemy:
#     def __init__(self,blood,attack):
#         self.attack=attack
#         self.blood=blood
#     def damage(self,value):
#         self.blood-=value
#         if self.blood<=0:
#             self.__death()
#     def __death(self):
#         print("敌人死了")
#         print("掉装备")
#     def attack(self,other):
#         print("敌人攻击玩家")
#         other.damage(self.attack)
#
# p01=Player(1000,10)
# print(p01.blood,p01.attack)
# e01=Enemy(500,5)
# print(e01.blood,e01.attack)
# p01.attack(e01)


# class Animal:
#     def jiao(self):
#         print("叫")
#
# class Dog(Animal):
#     def run(self):
#         print("run")
#
# class Brid(Animal):
#     def fly(self):
#         print("飞")
#
# dog01=Dog()
# print(isinstance(dog01,Dog))
# print(issubclass(Dog,Animal))
# print(issubclass(Animal,Brid))


# class Car:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
#
# class EleCar(Car):
#     def __init__(self,brand,speed,ele_container,power):
#         super().__init__(brand,speed)
#         self.ele_container=ele_container
#         self.power=power
#
#
# class Bomb:
#     def __init__(self,attack):
#         self.attack=attack
#     def explode(self,damage_target):
#         print("炸了")
#         damage_target.damage(self.attack)
# class Damageable:
#     def damage(self,value):
#         pass
#
#
# class Player(Damageable):
#     def __init__(self,hp):
#         self.hp=hp
#     def damage(self,value):
#         self.hp-=value
#         print("玩家受伤了")
#
# class Enmey(Damageable):
#     def __init__(self,hp):
#         self.hp=hp
#
#     def damage(self,value):
#         self.hp-=value
#         print("敌人受伤啦")
#         print("碎屏")
#
# import math
# class PhotoController:
#     def __init__(self,length=0,width=0,height=0,r=0,angle=0):
#         self.length=length
#         self.width=width
#         self.height=height
#         self.r=r
#         self.angle=angle
#     def area(self):
#         pass
#
# class Circle(PhotoController):
#     def area(self):
#         s=math.pi*self.r**2
#
# class juxing(PhotoController):
#     def area(self):
#         s=self.width*self.height
#         print(s)
# s=juxing(width=5,length=5)
# print(s.area)


# class GraphicManager:
#     def __init__(self):
    #     self.__graphic=[]
    # def add_graphic(self,graphic):
    #     if isinstance(graphic,Graphic):
    #         self.__graphic.append(graphic)
    #     else:
    #         raise ValueError()
    # def get_total_area(self):
    #     total_area=0
    #     for item in self.__graphic:
    #         total_area+=item.calculate_area()
    #     return total_area

# class Graphic:
#     def calculate_area(self):
#         raise NotImplementedError()
#
# class Circle(Graphic):
#     def __init__(self,r):
#         self.r=r
#     def calculate_area(self):
#         return 3.14*self.r**2
# class juxing(Graphic):
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length
#     def calculate_area(self):
#         return self.width*self.length

# c01=Circle(5)
# r01=juxing(10,20)
# manager=GraphicManager()
# manager.add_graphic(c01)
# manager.add_graphic(r01)
# re=manager.get_total_area()
# print(re)
#
# class WorkerController:
#     def __init__(self):
#         self.__salary=[]
#     def add_worker(self,worker):
#         if isinstance(worker,Worker):
#             self.__salary.append(worker)
#     def calulate_salary(self):
#         total_salary=0
#         for item in self.__salary:
#             total_salary+=item.calculate_salary()
#         return total_salary
#
# class Worker:
#     def calculate_salary(self):
#         raise NotImplementedError
#
# class programmer(Worker):
#     def __init__(self,base_salary,additional_salary):
#         self.base_salary=base_salary
#         self.additional_salary=additional_salary
#     def calculate_salary(self):
#         ttl_salary=self.base_salary+self.additional_salary
#         return ttl_salary
#
# class sales(Worker):
#     def __init__(self,base_salary,sales_money):
#         self.base_salary=base_salary
#         self.sales_money=sales_money
#     def calculate_salary(self):
#         ttl_salary=self.base_salary+self.sales_money*0.05
#         return ttl_salary
#
# p01=programmer(5000,10000)
# s01=sales(5000,10000)
# manager=WorkerController()
# manager.add_worker(p01)
# manager.add_worker(s01)
# re=manager.calulate_salary()
# print(re)

# class Enemy:
#     def __init__(self,name,hp,atk,defense):
#         self.name=name
#         self.hp=hp
#         self.atk=atk
#         self.defense=defense
#     def __str__(self):
#         return "%s--%d--%d--%d"%(self.name,self.hp,self.atk,self.defense)
#
#     def __repr__(self):
#         return "Enemy('%s',%d,%d,%d)"%(self.name,self.hp,self.atk,self.defense)
#
#
# e01=Enemy("s",10000,1000,10)
# print(e01)
# e02=eval(repr(e01))
# e02.name="dd"
# print(e02)

# class Vector:
#     def __init__(self,x):
#         self.x=x
    #
    # def __str__(self):
    #     return "一维向量的分量是"+str(self.x)
    #
    # def __add__(self, other):
    #     return Vector(self.x+other)
    # def __radd__(self, other):
    #     return Vector(other+self.x)
    #
    # def __sub__(self, other):
    #     return Vector(self.x-other)
    #
    # def __mul__(self, other):
    #     return Vector(self.x*other)
    #
    # def __iadd__(self, other):
    #     self.x +=other
    #     return self

# v01 = Vector(10)
# print(v01,id(v01))
# #重写__iadd__，实现在原对象基础上的变化
# #如果重写_iadd__，默认使用__add__,一般会产生新对象
# v01+=2
# print(v01,id(v01))
# # print(2+v01)
# # print(v01-2)
# # print(v01*2)
#
# list01=3
# print(list01,id(list01))
# list01+=4
# print(list01,id(list01))

# import Vector
# re=Vector.DoubleListHelper.get_element(Vector.list01,Vector.DoubleListHelper.get_pos("13"),Vector.Vector2.left(),3)
# print(re)
# re=Vector.DoubleListHelper.get_element(Vector.list01,Vector.DoubleListHelper.get_pos("22"),Vector.Vector2.up(),2)
# print(re)
# re=Vector.DoubleListHelper.get_element(Vector.list01,Vector.DoubleListHelper.get_pos("03"),Vector.Vector2.down(),2)
# print(re)

# list01=[
#     ["00","01","02","03"],
#     ["10","11","12","13"],
#     ["20","21","22","23"]
# ]
# from Vector import Vector2,DoubleListHelper
#
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("13"),Vector2.left(),3)
# print(re)
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("22"),Vector2.up(),2)
# print(re)
# re=DoubleListHelper.get_element(list01,DoubleListHelper.get_pos("03"),Vector2.down(),2)
# print(re)

# from Vector import Vector2 as Vtr02
# from Vector import DoubleListHelper as DHP
# re=DHP.get_element(list01,DHP.get_pos("13"),Vtr02.left(),3)
# print(re)
# re=DHP.get_element(list01,DHP.get_pos("22"),Vtr02.up(),2)
# print(re)
# re=DHP.get_element(list01,DHP.get_pos("03"),Vtr02.down(),2)
# print(re)


# import time
# str_time=time.time()
# local_time=time.localtime(158406324105.0133991)
# mon_local_time=local_time.tm_wday
# if mon_local_time==0:
#     print("星期一")
# elif mon_local_time==1:
#     print("星期二")
# elif mon_local_time==2:
#     print("星期三")
# elif mon_local_time==3:
#     print("星期四")
# elif mon_local_time==4:
#     print("星期五")
# elif mon_local_time==5:
#     print("星期六")
# elif mon_local_time==6:
#     print("星期天")
# print(str_time)
# print(local_time)
# print(mon_local_time)

# import time
# def get_week(year,month,day):
#     """
#     依据年月日，获取星期几
#     :param year:
#     :param month:
#     :param day:
#     :return:
#     """
#     tuple_time=time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")
#     week_time=tuple_time[6]
#     pri_week_time={
#         0:"星期一",
#         1:"星期二",
#         2:"星期三",
#         3:"星期四",
#         4:"星期五",
#         5:"星期六",
#         6:"星期天"
#     }
#     print(pri_week_time[week_time])
# get_week(2020,3,22)

# import time
# def get_day(year,month,day):
#     born_time=time.mktime((time.strptime("%d-%d-%d"%(year,month,day),"%Y-%m-%d")))
#     current_time=time.mktime(time.localtime())
#     life_day=current_time-born_time
#     life_time=life_day/3600//24
#     print(life_time)
#
# get_day(1994,4,26)

# score=[]
# def get_score():
#     while True:
#         try:
#             score_input=int(input("请输入成绩"))
#             if 0<score_input<100:
#                 score.append(score_input)
#             else:
#                 raise ValueError
#         except ValueError:
#             print("超出范围")
#             continue
#         else:
#             break
#
# get_score()


# class Enemy:
#     def __init__(self,attack):
#         self.attack=attack
#     @property
#     def attack(self):
#         return self._attack
#     @attack.setter
#     def attack(self,value):
#         if 0<=value<=100:
#             self._attack=value
#         else:
#             raise ValueError("攻击力超出范围")
#
# print(Enemy(23).attack)
# print(Enemy(101).attack)


# list01=["铁扇公主","铁锤公主","扳手王子"]
# iterator=list01.__iter__()
# while True:
#     try:
#         item=iterator.__next__()
#         print(item)
#     except StopIteration:
#         break



# dict01={"铁扇公主":101,"铁锤公主":102,"扳手王子":103}
# iterator=dict01.__iter__()
# while True:
#     try:
#         item=iterator.__next__()
#         print(item,dict01[item])
#     except StopIteration:
#         break
#


# class GraphicManager:
#     def __init__(self):
#         self.__graphic=[]
#     def add_graphic(self,graphic):
#         if isinstance(graphic,Graphic):
#             self.__graphic.append(graphic)
#         else:
    #         raise ValueError()
    # def get_total_area(self):
    #     total_area=0
    #     # for item in self.__graphic:
    #     #     total_area+=item.calculate_area()
    #     result=0
    #     iterator=self.__graphic.__iter__()
    #     while True:
    #         try:
    #             next_graphic=iterator.__next__()
    #             result+=next_graphic.calculate_area()
    #         except StopIteration:
    #             break
    #     return result

# class Graphic:
#     def calculate_area(self):
#         raise NotImplementedError()
#
# class Circle(Graphic):
#     def __init__(self,r):
#         self.r=r
#
#     def calculate_area(self):
#         return 3.14*self.r**2
# class juxing(Graphic):
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length
#
#     def calculate_area(self):
#         return self.width*self.length

# Circle(2)
# juxing(4,5)
# manager=GraphicManager()
# manager.add_graphic(Circle(2))
# manager.add_graphic(juxing(4,5))
# print(manager.get_total_area())


# class Graphic:
#     def calculate_area(self):
#         raise NotImplementedError()
# class GraphicManager:
#     def __init__(self):
#         self.__graphic=[]
#     def add_graphic(self,graphic):
#         if isinstance(graphic,Graphic):
#             self.__graphic.append(graphic)
#     def __iter__(self):
#         return GraphicIterator(self.__graphic)
# class GraphicIterator:
#     def __init__(self,target):
#         self.__target=target
#         self.__index=0
#     def __next__(self):
#         if self.__index>len(self.__target)-1:
#             raise StopIteration
#         self.__index+=1
#         return self.__target[self.__index]

# manager=GraphicManager()
# result=0
# iterator=manager.__iter__()
# while True:
#     try:
#         next_graphic=iterator.__next__()
#         result+=next_graphic.calculate_area()
#     except StopIteration:
#         break

#
# class Employee:
#     def __init__(self,name):
#         self.name=name
#

# class EmployeeManager:
#     def __init__(self):
#         self.__employee=[]
#
#     def add_employee(self,emp):
#         self.__employee.append(emp)
#
#     def __iter__(self):
#         return EmployeeIterator(self.__employee)
#
# class EmployeeIterator:
#     def __init__(self,target):
#         self.__target=target
#         self.__index=-1
#
#     def __next__(self):
#             self.__index += 1
#             if self.__index<len(self.__target)-1:
#                 raise StopIteration
#             return self.__target[self.__index]
#
# manager=EmployeeManager()
# Employee01=Employee("a")
# Employee02=Employee("b")
# manager.add_employee(Employee01)
# manager.add_employee(Employee02)
#
# employeeIterator=manager.__iter__()
#
# while True:
#     try:
#         next_employee=employeeIterator.__next__()
#         print(next_employee.name)
#     except StopIteration:
#         break

#
# """
# 练习Myrange,实现以下功能
# for item in range(10):
#     print(item)
# """
#
# class MyRange:
#     def __init__(self,range):
#         self.range=range
#     def __iter__(self):
#         return MyRangeIterator(self.range)
#
# class MyRangeIterator:
#     def __init__(self,range):
#         self.range=range
#         self.__result=-1
#     def __next__(self):
#         self.__result += 1
#         if self.__result>self.range:
#             raise StopIteration
#         return self.__result
#
# manager=MyRange(10)
# range_iterator=manager.__iter__()
# while True:
#     try:
#         next_object=range_iterator.__next__()
#         print(next_object)
#     except StopIteration:
#         break

# list01=[4,5,566,7,8,10]
# class EvenNumber:
#     def __init__(self,list):
#         self.list=list
#     def __iter__(self):
#         return Myiterator(self.list)
# class Myiterator:
#     def __init__(self,list):
#         self.list=list
#         self.space_list = []
#     def __next__(self):
#         start=0
#         while start<len(self.list):
#             if self.list[start]//2==0:
#                 self.space_list.append(self.list[start])
#         return self.space_list
#
# manager=EvenNumber(list01)
# range_iterator=manager.__iter__()
# while True:
#     try:
#         next_object=range_iterator.__next__()
#
#     except StopIteration:
#         break

# list01=[4,5,566,7,8,10]
# result=[]
# for item in list01:
#     if item%2==0:
#         result.append(item)
# print(result)

# 定义一个生成器函数，my_enumerate，实现下列现象，将元素与索引合成一个元组

# list01=[3,4,55,6,7]
# for item in enumerate(list01):
#     print(item)
#
# for index,element in enumerate(list01):
#     print(index,element)
#
# def my_enumerate(list_target):
#     index=0
#     for item in list_target:
#         yield index,item
#         index+=1
#
# for index,element in my_enumerate(list01):
#     print((index,element))


# list01=["孙悟空","猪八戒","唐僧","沙僧"]
# list02=[101,102,103,104]
# # for item in zip(list02,list01):
# #     print(item)
#
# def my_zip(target_list01,target_list02):
#     for i in range(len(target_list01)):
#         yield target_list01[i],target_list02[i]
#
# for item in my_zip(list01,list02):
#     print(item)


# list01=[3,"54",True,6,"76",1.6,False,3.5]
# def find01():
#     for item in list01:
#         if type(item)==int:
#             yield item
# re=find01()
# for item in re:
#     print(item)

# 使用生成器函数及生成器表达式完成
#1.获取列表中的字符串
#2.获取列表中的小数
# list01=[3,"54",True,6,"76",1.6,False,3.5]

#生成器函数
# def find02():
#     for item in list01:
#         if type(item)== str:
#             yield item
#
# re01=find02()
# for item in re01:
#     print(item)

#生成器表达式
# re02=(item for item in list01 if type(item)==str)
# for item in re02:
#     print(item)
# 列表推导式
# re03=[item for item in list01 if type(item)==str]
# print(re03)

# class SkillData:
#     def __init__(self,id,name,atk_ratio,duration):
#         self.id=id
#         self.name=name
#         self.atk_ratio=atk_ratio
#         self.duration=duration
#
#     def __str__(self):
#         return "技能数据是：%d,%s,%d,%d"%(self.id,self.name,self.atk_ratio,self.duration)
#
# list_skill=[
# SkillData(101,"乾坤大挪移",5,10),
# SkillData(102,"祥龙十八掌",8,5),
# SkillData(103,"葵花宝典",10,2)
# ]

#练习1：获取攻击力比例大于6的所有技能
#要求：使用生成器函数/生成器表达式

# def find01(target_data):
#     for item in target_data:
#         if item.atk_ratio>6:
#             yield item.name
# re=find01(list_skill)
# for item in re:
#     print(item)

# re=(item for item in list_skill if item.atk_ratio>6)
# for item in re:
#     print(item)

# 练习2：获取持续时间在4--11之间的所有技能
#练习3：获取技能编号是102的技能
#练习4：获取技能名称大于4个字并且持续时间小于6的所有技能

#练习2：
# re=(item for item in list_skill if 4<item.duration<11)
# for item in re:
#     print(item)

#练习3：
# re=(item for item in list_skill if item.id==102)
# for item in re:
#     print(item)

#练习4：
# re=(item for item in list_skill if 4<len(item.name) and item.duration<6)
# for item in re:
#     print(item)
#

# list01=[43,4,5,5,6,7,87]
# def ou_data(list):
#     for item in list:
#         if item%2==0:
#             yield item
#
# def lt_data(list):
#     for item in list:
#         if item>10:
#             yield item
#
# def range_data(list):
#     for item in list:
#         if 10<item<50:
#             yield item


# def condition01(item):
#     return item%2==0
#
# def condition02(item):
#     return item>10
#
# def condition03(item):
#     return 10<item<50
#
# def find(condition):
#     for item in list01:
#         if condition(item):
#             yield item
#
# for item in find(condition01):
#     print(item)
#
# for item in find(condition02):
#     print(item)
#

# class SkillData:
#     def __init__(self,id,name,atk_ratio,duration):
#         self.id=id
#         self.name=name
#         self.atk_ratio=atk_ratio
#         self.duration=duration
#
#     def __str__(self):
#         return "技能数据是：%d,%s,%d,%d"%(self.id,self.name,self.atk_ratio,self.duration)
#
# list_skill=[
# SkillData(101,"乾坤大挪移",5,10),
# SkillData(102,"祥龙十八掌",8,5),
# SkillData(103,"葵花宝典",10,2)
# ]

#1.查找名称是"葵花宝典"的技能
#2.查找编号是101的技能
#3.查找持续时间大于0的技能

# def condition01(item):
#     return item.name=="葵花宝典"
#
# def condition02(item):
#     return item.id==101
#
# def condition03(item):
#     return  item.duration>0
#
#
# from list_helper import *
# # generate01=find_all.find(list_skill,condition01)
#
# generate02=find_all.find(list_skill,lambda item:len(item.name)>4)
# generate03=find_all.find(list_skill,lambda item:item.duration<5)


# for item in list_skill:
#     if item.name=="葵花宝典":
#         print(item.name)
#
# for item in list_skill:
#     if item.id==101:
#         print(item.name)
#
# for item in list_skill:
#     if item.duration>0:
#         print(item.name)


# def condition01(item):
#     return item.name=="葵花宝典"
#
# def condition02(item):
#     return item.id==101
#
# def condition03(item):
#     return  item.duration>0

# def find(condition):
#     for item in list_skill:
#         if condition(item):
#             print(item)

# find(condition02)

#
# class Enemy:
#     def __init__(self,name,attack,defence,blood):
#         self.name=name
#         self.attack=attack
#         self.defence=defence
#         self.blood=blood
#
#     def __str__(self):
#         return "敌人信息为：%s,%d,%d,%d"%(self.name,self.attack,self.defence,self.blood)
#
# enemy_list=[
# Enemy("灭霸",4,5,90),
# Enemy("昆成",9,4,70),
# Enemy("大鸟",14,7,80),
# Enemy("小鸟",14,7,0)
# ]
#
# from list_helper import *
# find_all.find(enemy_list,lambda item:item.name=="灭霸")
# find_all.find(enemy_list,lambda item:item.attack>10)
#find_all.get_count(enemy_list,lambda item:item.blood<=0)
# s=find_all.judge_info(enemy_list,lambda item:item.attack<5 or item.defence<10)

# total_blood=find_all.get_sum(enemy_list,lambda item:item.blood)
# print(total_blood)

# name_list=find_all.get_list(enemy_list,lambda item:(item.name,item.blood))
# print(name_list)

# max_atk_list=find_all.get_max(enemy_list,lambda item:item.attack)
# print(max_atk_list)


# def uporder_list():
#     for i in range(len(enemy_list)):
#         for s in range(i,len(enemy_list)):
#             if enemy_list[i].attack>enemy_list[s].attack:
#                 enemy_list[i],enemy_list[s]=enemy_list[s],enemy_list[i]



# order_list=find_all.uporder_list(enemy_list,lambda item:item.attack)
# for item in enemy_list:
#     print(item)


# list01=([1,1,1],[2,2],[3,3,3,3])
# #获取长度最大的列表
# re=max(list01,key=lambda item:len(item))
# print(re)

# class Enemy:
#     def __init__(self,name,attack,defence,blood):
#         self.name=name
#         self.attack=attack
#         self.defence=defence
#         self.blood=blood
#
#     def __str__(self):
#         return "敌人信息为：%s,%d,%d,%d"%(self.name,self.attack,self.defence,self.blood)
#
# enemy_list=[
# Enemy("灭霸",4,5,90),
# Enemy("昆成",90,4,40),
# Enemy("大鸟",14,7,80),
# Enemy("小鸟",14,7,0)
# ]

# re01=filter(lambda item:item.attack>10,enemy_list)
# for item in re01:
#     print(item)

# re02=map(lambda item:(item.name,item.blood,item.attack),enemy_list)
# for item in re02:
#     print(item)

# re03=sorted(enemy_list,key=lambda item:item.blood,reverse=True)
# for item in re03:
#     print(item)

# from list_helper import *
# re=find_all.get_min(enemy_list,lambda item:item.attack)
# print(re)


# re01=find_all.remove_value(enemy_list,lambda item:item.blood==0)
# for item in re01:
#     print(item)

# re02=find_all.remove_value(enemy_list,lambda item:item.defence<5)
# for item in re02:
#     print(item)



#在不改变原有功能（存取钱）的定义与调用情况下，增加验证账号的功能

#验证账号
# def verify_account(func):
#     def wrapper(*args,**kwargs):
#         print("验证账号")
#         return func(*args,**kwargs)
#     return wrapper
#
# @verify_account
# def deposite(money):
#     print("存%d钱喽"%money)
# @verify_account
# def withdraw(login_id,pwd):
#     print("取钱喽",login_id,pwd)
#
# deposite(1000)
#
# withdraw("sasa",222)

#在不改变原有功能(fun01 fun02)调用与定义情况下，为其增加新功能(打印函数执行时间)

import time
def verify_time(fun):
    def wrapper(*args,**kwargs):
        before_time=time.time()
        result=fun(*args,**kwargs)
        after_time=time.time()
        print("程序时间为%d"%(after_time-before_time))
        return result
    return wrapper

@verify_time
def fun01():
    time.sleep(2)
    print("fun01执行完毕喽")

@verify_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完毕喽，参数是：",a)


fun01()
fun02(100)









































