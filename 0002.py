#coding=utf-8
import MySQLdb
import random
import string

def Activetion_codes():#通过随机函数得到一个大小写和数字混合的激活码
    code=[]
    for i in range(9):
        if i == 0:
            x=random.choice(string.letters)#激活码首位为字母
            code.append(x)
        else:
            x=random.choice(string.letters+string.digits*2)
            code.append(x)
    code=''.join(code)
    return code

def code_200():#生成包含200个激活码的列表
    code_list= []
    for i in range(200):
        x=Activetion_codes()
        code_list.append(x)
    return code_list

def save_code(code):
    cxn=MySQLdb.connect(host='localhost',user='root',passwd='1',db='py') #创建数据库链接对象
    cur=cxn.cursor()  #创建游标对象
    for i in range(len(code)):
        #使用游标对象的execute方法执行命令存入数据
        cur.execute(r'insert into code(id,code) values (%d,"%s")'%(i+1,code[i]))
    cxn.commit() #提交事务

activetion_code=code_200()
save_code(activetion_code) #将200个激活码存入数据库