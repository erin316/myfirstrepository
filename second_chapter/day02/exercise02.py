"""
逆波兰表达式练习
"""
from sstick import *
st=Sstack()
def input_content():
    while True:
        s01=input()
        s02=s01.split(" ")
        for item in s02:
            st.push(item)

        







