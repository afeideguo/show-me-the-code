#coding=utf-8
import codecs

filtered_word_list=[]
filtered_word_file=open('filtered_words.txt')
for word in filtered_word_file:
    filtered_word_list.append(word.strip()) #将敏感词加入敏感词列表以使用

def filtered(text): #过滤敏感词
    if text.strip() in filtered_word_list:
        return 'freedom'
    else:
        return 'human rights'

word=raw_input('---->')
print filtered(word)


