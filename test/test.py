import re
import os
import requests

from PyQt5 import QtWidgets			
from untitled import Ui_Form 							#imgUi就是你自己做的UI的名字


class mywindow(QtWidgets.QWidget,Ui_Form):			#Ui_Form要跟UI文件里的class一样的名字
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.func)   #这句是关联按钮槽


    def func(self):

        url_init = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=9&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word="
        keyword = self.lineEdit_k.text()
        Location = self.lineEdit_p.text()
        max_num = self.lineEdit_n.text()
        imgpath = Location + "://" + str(keyword) + "//"
        if not os.path.exists(imgpath):
            os.mkdir(imgpath)
        url = url_init + str(keyword)
        print(url)

        r = requests.get(url)
        r.encoding = r.apparent_encoding
        html = r.text
        fmq = re.findall(r'&fr=sugrec&sf=1&fmq=(.*?)_R&pv', html, re.S)[1]

        gsm = re.findall(r"gsm: '(.*?)',", html, re.S)[0]
        New_List = []
        m = 0
        while (m < int(max_num)):
            urls = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=&is=&fp=result&queryWord=" + str(
                m) + "&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=" + str(
                keyword) + "&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=" + str(m) + "&rn=30&gsm=" + str(
                gsm) + str(fmq) + "="
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest'
            }
            rr = requests.get(urls, headers=headers)
            rr.encoding = rr.apparent_encoding
            htmls = rr.text
            Pic_links = re.findall('"middleURL":"(.*?)"', htmls, re.S)
            index = 1
            for pic_link in Pic_links:
                print(pic_link)
                path = imgpath + str(m + index) + "." + pic_link.split(".")[-1]
                with open(path, 'wb') as f:
                    f.write(requests.get(pic_link).content)
                    f.close()

                    outText = "下载......" + str(m + index) + "......完成！"
                    # print(outText)
                    self.textBrowser.append(outText)
                    QtWidgets.QApplication.processEvents()  # 刷新界面

                    index = index + 1
            m = m + 30



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())