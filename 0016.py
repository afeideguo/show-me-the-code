# coding=utf-8
import xlwt

numbers_file=open('numbers.txt') #打开文件
numbers_list=eval(numbers_file.read()) #读取文件中的表达式
numbers_file.close()

workbook=xlwt.Workbook('utf-8') #创建工作簿
worksheet=workbook.add_sheet('numbers') #创建工作表

row,col=0,0 #将数据写入工作表
for i in numbers_list:
    for j in i:
        worksheet.write(row,col,label='%s'%j)
        col+=1
    col=0
    row+=1

workbook.save('numbers.xls') #保存工作簿