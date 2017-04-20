# coding=utf-8
import Image
import os

path='/home/afei/picture' #图片目录
os.chdir(path) #工作目录切换到此目录

def change_size(imgname):    #参数为文件名
    img=Image.open(imgname)  #打开文件作为文件对象
    if max(img.size)>1136:    #如果最大尺寸大于1136
        rat=max(img.size)/1136 #求出最大尺寸与1136的比
        new_min=min(img.size)/rat #根据最大尺寸与1136的比 求出对应的转换后短边尺寸
        new_img=img.resize((1136,new_min),Image.ANTIALIAS) #将图片的尺寸缩放为长边为1136
        new_img.save('new_'+imgname) #保存图片
        img.close()

def getname(imgpath): #得到图片的所有文件名列表
    img_namelist=[]
    for img_name in os.listdir(imgpath): #遍历图片所在目录
        if '.jpg' in img_name:      #若后缀名为图片格式，则加入图片文件名列表（不严谨）
            img_namelist.append(img_name)
    return img_namelist

img_list=getname(path)
for i in img_list:
    change_size(i)

