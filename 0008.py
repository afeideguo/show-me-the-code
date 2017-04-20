#coding=utf-8
from goose.text import StopWordsChinese
from goose import Goose

def url_page(page_url):
    g=Goose({'stopwords_class':StopWordsChinese})  #创建Goose对象
    article=g.extract(url=page_url)                #使用对象提取url
    return article.cleaned_text                 #返回对象文本

url='http://www.pythontab.com/html/mianshiti/2017/0313/1123.html'
print url_page(url)

