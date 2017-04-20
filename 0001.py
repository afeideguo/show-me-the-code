# coding=utf-8
import random
import string

L = []


def Activetion_code():#通过随机函数得到一个大小写和数字混合的激活码
    code=[]
    for i in range(9):
        if i == 0:
            x=random.choice(string.uppercase+string.lowercase)#激活码首位为字母
            code.append(x)
        else:
            x=random.choice(string.uppercase+string.lowercase+string.digits*2)
            code.append(x)
    code=''.join(code)
    return code

def code_200():#生成包含200个激活码的列表
    code_list= L
    for i in range(200):
        x=Activetion_code()
        code_list.append(x)
    return code_list

print code_200()
