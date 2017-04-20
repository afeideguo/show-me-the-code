# coding=utf-8
import os
import re
import collections


def get_word(file):  #统计文件中出现频次最高的单词
    allword=file.read()  #所有单词
    regex=re.compile(r'\b\w+\b',re.I) #使用正则匹配单词，大小写不敏感
    word_list=re.findall(regex,allword) #使用findall匹配所有单词，不会去重
    word_dict={}
    for i in word_list:
        word_times=word_list.count(i)  #统计单词列表中每个单词的个数
        word_dict[i]=word_times
    great_times=0
    for i in word_dict.keys():
        if word_dict[i]>great_times:  #查找出现次数最多的单词
            great_times=word_dict[i]
            great_word=i
    return '%s--<%s>: %s'%(file.name,great_word,great_times)

def get_file(path):
    os.chdir(path)
    file_list=[]
    for i in os.listdir(path):
        if '.txt' in i:
            file_list.append(i)
    return file_list

mypath='/home/afei/ssskf'
all_file=get_file(mypath)
for i in all_file:
    print get_word(i)



