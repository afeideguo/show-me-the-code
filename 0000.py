# coding=utf-8

import Image,ImageDraw,ImageFont

pic=Image.open('0001.jpg')#打开图片作为图片对象
ttf = '/usr/share/fonts/truetype/fonts-japanese-gothic.ttf' #字体路径
font=ImageFont.truetype(ttf,size=50) #打开字体作为字体对象
fill='#ff0000' #字体填充颜色
draw=ImageDraw.Draw(pic) #将图片对象作为画布对象
draw.text((160,0),chr(52),fill=fill,font=font) #在画布对象上添加文字

pic.save('test.png','PNG') #将图片对象保存为png格式