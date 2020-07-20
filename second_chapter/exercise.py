# class A:
#     v = 100
#     def __init__(self):
#         self.v = 200
# a1 = A()
# a2 = A()
# del a2.v
# print(a1.__dict__)
# print(a2.__dict__)
# print(A.v)
# print(a2.v)
# print(a1.__class__.v)
# print(list((("aaa"))))
# d = {"a": 3, "b": 2, "c": 1}
# print(d.clear())

# class A:
#    a = 1
# obj = A()
# obj.a = 2
# print(obj.a)
# print(A.a)
# A.a = 3
# print(obj.a)
# print(A.a)
# print(dict([('two', 2), ('one', 1), ('three', 3)]))
# print(dict({'three': 3, 'one': 1, 'two': 2}))

# b = {5, 6, 7, 8, 9}
# c = {5, 6}
# d = {5, 6, 7}
# print(c-b)
# d = {1:"a", 2:"b", 3:"4"}
# d["3"] = 3
# print(d)

# L = [1,2,3,4,5,6]
# L[2:4] = []
# print(L)

# s="sssaswdedx"
# tt=s[2:5]
# print(s)
# print(tt)

with open("./day04/student_info.txt","r") as f:
    for line in f:
        print(line)



