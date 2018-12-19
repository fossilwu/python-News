import re
import os
import requests


from PyQt5 import QtWidgets
from imgUi import Ui_Form


class mywindow(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.textEdit.append("1.搜关键字，如“壁纸”")
        self.textEdit.append("2.图片数量，请填30的倍数")
        self.textEdit.append("3.保存路径，只填盘符，如：E")
        self.textEdit.append("4.参考路径：E:\\壁纸")
        self.textEdit.append("===========================")

        self.pushButton.clicked.connect(self.imgDownload)


    def imgDownload(self):
        url_init = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word="
        keyword = self.lineEdit_key.text()
        Location = self.lineEdit_path.text()
        max_num = self.lineEdit_num.text()
        imgpath = Location + "://" + str(keyword) + "//"
        if not os.path.exists(imgpath):
            os.mkdir(imgpath)
        url = url_init + str(keyword)
        r = requests.get(url)
        r.encoding = r.apparent_encoding
        html = r.text
        fmq = re.findall(r'&fr=sugrec&sf=1&fmq=(.*?)_R&pv', html, re.S)[1]
        gsm = re.findall(r"gsm: '(.*?)',", html, re.S)[0]
        m = 0
        while (m < int(max_num)):
            urls = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=" + str(
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
                #print(pic_link)
                path = imgpath + str(m + index) + "." + pic_link.split(".")[-1]
                with open(path, 'wb') as f:
                    f.write(requests.get(pic_link).content)
                    f.close()
                    outText = "下载......"+str(m + index)+"......完成！"
                    #print(outText)
                    self.textEdit.append(outText)
                    QtWidgets.QApplication.processEvents()      #刷新界面
                    index = index + 1
            m = m + 30
        self.textEdit.append("=====全部完成！=====")





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())