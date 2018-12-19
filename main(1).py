


from PyQt5 import QtWidgets			
from imgUi import Ui_Form 							#imgUi就是你自己做的UI的名字


class mywindow(QtWidgets.QWidget,Ui_Form):			#Ui_Form要跟UI文件里的class一样的名字
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)






if __name__ == "__main__":						#这个py自己执行的话才运行下面的，如果是被其他程序调用，并不执行下面的
    import sys
    app = QtWidgets.QApplication(sys.argv)
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())