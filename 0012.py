#coding=utf-8

def filtered_word(filepath):
    open_file=open(filepath)
    filtered_word_list=[]
    for i in open_file:
        filtered_word_list.append(i.strip())
    return filtered_word_list

def filtered(input_text,filtered_list):
    for word in filtered_list:
        if word in input_text:#如果输入文本中存在敏感词，替换。
            print 'use'
            input_text=input_text.replace(word,'**')
    return input_text

word_list=filtered_word('filtered_words.txt')
print word_list
text=raw_input('---->')
print filtered(text,word_list)


