# coding=utf-8
import os
import string
import Image,ImageDraw,ImageFont,ImageFilter
from random import randint,choice

if os.path.exists('tem.png'):#如果图片存在，则删除（方便测试）
    os.remove('tem.png')

def ranchar():
    return choice(string.uppercase)  #返回一个随机大写字符

def rancolor1():                     #返回一个范围内随机颜色（将用作字体色）
    return randint(32,125),randint(32,125),randint(32,125)

def rancolor2():                     #返回一个范围内随机颜色（将用作背景色）
    return randint(64,255),randint(64,255),randint(64,255)

width,height = 240,60
size=(width,height)   #图片尺寸
ttf = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf' # 字体位置

code_img=Image.new('RGBA',size=size,color=(255,255,255))   #创建图片
draw=ImageDraw.Draw(code_img)                  #创建画笔
for i in range(width):
    for j in range(height):
        draw.point((i,j),fill=rancolor2())   #填充每一个像素

code_font=ImageFont.truetype(ttf,36)   #创建文本
for k in range(4):
    draw.text((60*k+10,10),ranchar(),font=code_font,fill=rancolor1()) #将文本画入图片

code_img=code_img.filter(ImageFilter.BLUR)        #模糊图片
code_img.save('tem.png','PNG')
