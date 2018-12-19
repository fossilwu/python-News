import re
import os
import requests
import queue
import time
url_init="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word="
Input=input("Please enter the keyword:")
Location=input("where disk do you wanna save this:c-g：")

root=Location+"://"+str(Input)+"//"
print(root)
if not os.path.exists(root):
                os.mkdir(root)
url=url_init+str(Input)
r=requests.get(url)
r.encoding=r.apparent_encoding
html=r.text
fmq=re.findall(r'&fr=sugrec&sf=1&fmq=(.*?)_R&pv',html,re.S)[1]

gsm=re.findall(r"gsm: '(.*?)',",html,re.S)[0]
New_List=[]
m=0
max=input("Please enter the number(requirement:number%30==0):  ")           
while(m<int(max)):
        urls="https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord="+str(m)+"&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word="+str(Input)+"&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn="+str(m)+"&rn=30&gsm="+str(gsm)+str(fmq)+"="
        headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest'
                }       
        rr=requests.get(urls,headers=headers)
        rr.encoding=rr.apparent_encoding
        htmls=rr.text
        Pic_links=re.findall('"middleURL":"(.*?)"',  htmls,re.S)  
        index=1
        for pic_link in Pic_links:
                print(pic_link)
                path=root+str(m+index)+"."+pic_link.split(".")[-1]
                with open(path,'wb') as f:
                        f.write(requests.get(pic_link).content)
                        f.close()
                        print("downloading",'-----------------',m+index)
                        index=index+1
        m=m+30       
print("OK，EXCITED！")
print("All Rights Reserved by Pei Xiaodong")
time.sleep(5)
                
                
         


                
        
