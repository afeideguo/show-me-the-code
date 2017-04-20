# coding=utf-8
import urllib,urllib2
import re

#头信息
header={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:44.0) Gecko/20100101 Firefox/44.0'}

def get_img_url(page_url):#得到页面所有图片的链接

    request=urllib2.Request(page_url,headers=header) #生成request对象
    reference=urllib2.urlopen(request)    #获取页面对象
    page=reference.read()            #读取页面

    regex=re.compile(r'<img.*?class="BDE_Image" src="(.*?)".*?>') #编译正则匹配模式字符串
    img_url_list=re.findall(regex,page)       #匹配所有图片链接生成列表

    return img_url_list

def download_img(url_list,img_path):  #从图片链接下载图片并存放在指定文件夹
    for img_url in url_list:
        urllib.urlretrieve(img_url,'%s/%s.jpg'%(img_path,img_url[-8:-5])) #下载图片
    print 'done'

url='http://tieba.baidu.com/p/2166231880?see_lz=1' #爬虫页面
path='/home/afei/picture'  #存放路径
urllist=get_img_url(url)
download_img(urllist,path)
