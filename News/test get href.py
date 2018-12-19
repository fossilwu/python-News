import urllib.request
import re
import requests
from bs4 import BeautifulSoup as bs

html_doc = "http://www.lyjyfw.net/"

res = requests.get(html_doc)  #发送请求
print(res.encoding)    #这个是用来查看网页编码的
res.encoding = 'utf-8'   #跟上一个结合来用，如果编码有乱码，则可以通过这个定义编码来改变
html = res.text


soup = bs(html, 'html.parser')

item=soup.select('ul')
for items in item:
    items = soup.find_all('a')#,attrs={'class':'nbg'})
#print(items)

for i in items:
    wangzhi = i.get('href')
    biaoti = i.string

    print(biaoti,wangzhi)

#req = urllib.request.Request(html_doc)
#webpage = urllib.request.urlopen(req)
#html = webpage.read()
#print(html)