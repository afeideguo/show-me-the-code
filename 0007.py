# coding=utf-8
import os

code,note,empty=0,0,0

def line_num(file_name):
    global code,note,empty
    for i in file_name:
        if i.strip() == '': #空行
            empty+=1
        elif '#' in i:  #有注释的行
            note+=1
        else:
            code+=1     #代码行

def get_file(path):
    os.chdir(path)
    flist=[]
    for fname in os.listdir(path):
        if '.py' in fname:
            flist.append(fname)
    return flist  #文件列表

mypath='/home/afei/PycharmProjects/untitled/learn'
file_list=get_file(mypath)
for i in file_list:
    fn=open(i)
    line_num(fn)
    fn.close()
print 'cl:%s,nt:%s,em:%s'%(code,note,empty)