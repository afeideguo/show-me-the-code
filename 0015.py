# coding=utf-8
import xlwt

city_file=open('city.txt')   #打开文件
city_dict=eval(city_file.read()) #读取文件中的表达式
city_file.close()  #关闭文件

workbook=xlwt.Workbook('utf-8')  #创建工作簿
worksheet=workbook.add_sheet('city') #创建工作表

row,col=0,0
for i in city_dict.iteritems():#将数据填入工作表
    for j in i:
        worksheet.write(row,col,label='%s'%j)
        col+=1
    col=0
    row+=1

workbook.save('citys.xls') #保存工作表