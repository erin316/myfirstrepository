

# list01=[2,1,3,5,7,4]
# select(list01)
# print(list01)

# 快速排序
# def insert(list_):
#     for i in range(len(list_)):
#         x=list_[i]
#         j=i-1
#         while j>=0 and list_[j]>x:
#             list_[j+1]=list_[j]
#             j-=1
#         list_[j+1]=x

# list01=[2,3,1,5,7,4]
# insert(list01)
# print(list01)

#冒泡排序
def bubble(list_):
    x=0
    j=len(list_)
    while x<j:
        for i in range(j-1):
            if list_[i]>list_[i+1]:
                list_[i],list_[i+1]=list_[i+1],list_[i]
        j-=1
list01=[2,3,1,5,7,4]
bubble(list01)
print(list01)

# 选择排序
def select(list_):
    for item in range(len(list_)-1):
        for item01 in range(item+1,len(list_)):
            if list_[item]>list_[item01]:
                list_[item],list_[item01]=list_[item01],list_[item]



#插入排序
# def insert(list_):
#     for item in range(1,len(list_)):
#         i=0
#         j=item
#         while j==0 or list_[j]<list_[j-1]:
#             list_[j],list_[j-1]=list_[j-1],list_[j]
#             j-=1






















