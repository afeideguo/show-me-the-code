# coding=utf-8
import xlwt

student_file=open('student.txt')  #打开student.txt文件
student_dict=eval(student_file.read()) #读取文件内容内的python表达式（学生成绩的字典）
student_file.close()

workbook=xlwt.Workbook('utf-8')   #创建编码为utf-8的工作簿
worksheet=workbook.add_sheet('student') #创建名为student的工作表

row,col=0,0           #将成绩字典的键依次写入0列
for i in student_dict.keys():
    worksheet.write(row,col,label='%s'%i)
    row+=1

row, col = 0, 1       #将字典的值（列表）的每个项写入每行
for j in student_dict.values():
    for k in j:
        worksheet.write(row,col,label='%s'%k)
        col+=1
    col=1
    row+=1

workbook.save('student.xls')   #保存工作表，名称为student.xls