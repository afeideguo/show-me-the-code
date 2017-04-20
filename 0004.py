#coding=utf-8

"""其实可以通过正则表达式匹配单词更快更方便

   使用\b匹配单词边界，使用re.findall得到每个单词的不去重列表
   再使用list.count统计列表中各单词个数（或使用collections模块"""

import string

def count_word(text):
    word_count_dict={}
    word=''
    for line in text:
        for char in line:
            if char in string.letters:
                word+=char.lower()   #当字符为大小写字母时，将字符添加入字符串作为单词的一个字母
            if char in [' ','\t','\n','  ',':']:
                if word in word_count_dict.keys(): #当遇见标点或者换行时，说明单词到结尾
                    word_count_dict[word]+=1 #则当单词已在字典，次数加一
                else:
                    word_count_dict[word]=1  #不在字典，则添加进字典，次数设为1
                word=''                      #重置字符串，继续下一个单词
                word+=char.lower().strip()   #不区分单词大小写同时去掉换行符（不知为何单词前偶尔会出现换行符）
    word_count_dict.pop('')       #去掉字典的那个空字符（不知为何会出现空字符）
    return word_count_dict        #返回字典，键为单词，值为次数

counted_page=open('0004.txt')
print count_word(counted_page)



