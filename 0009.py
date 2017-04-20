# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re

def get_page(url):
    url_page=requests.get(url)  #得到链接url页面
    url_tag=BeautifulSoup(url_page.text,'lxml') #解析链接页面
    tag_list=url_tag.find_all('a')   #得到有链接的所有标签
    url_list=[]
    for i  in tag_list:
        url_list.append(i.get('href'))  #得到所有标签的链接属性并存入列表
    return url_list

page_url='http://www.pythontab.com/html/mianshiti/2017/0313/1123.html'
all_url=get_page(page_url)
for j in all_url:
    print j

