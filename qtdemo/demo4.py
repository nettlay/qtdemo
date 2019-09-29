from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('字体设置')

        self.tx = QTextEdit(self)
        self.tx.setGeometry(20, 20, 300, 300)

        self.bt1 = QPushButton('打开文件', self)
        self.bt1.move(350, 20)
        self.bt2 = QPushButton('选择字体', self)
        self.bt2.move(350, 70)
        self.bt3 = QPushButton('选择颜色', self)
        self.bt3.move(350, 120)
        self.bt4 = QPushButton('更改背景', self)
        self.bt4.move(350, 170)
        self.bt5 = QPushButton('图像背景', self)
        self.bt5.move(350, 220)
        self.bt6 = QPushButton('文字背景', self)
        self.bt6.move(350, 270)

        self.bt1.clicked.connect(self.openfile)
        self.bt2.clicked.connect(self.choicefont)
        self.bt3.clicked.connect(self.choicecolor)
        self.bt4.clicked.connect(self.BackgroundColor)
        self.bt5.clicked.connect(self.Backgroundimg)
        self.bt6.clicked.connect(self.testbackground)

        self.show()

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, '打开文件', '')
        print(fname)
        if fname[0]:
            with open(fname[0], 'r', encoding='utf-8', errors='ignore') as f:
                self.tx.setText(f.read())

    def choicefont(self):  # 字体设置
        font, ok = QFontDialog.getFont()
        if ok:
            self.tx.setCurrentFont(font)

    def choicecolor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            # self.tx.setTextColor(Qt.red)#根据自己的需要设置颜色
            self.tx.setTextColor(col)  # 可以自己选择需要的颜色

    def BackgroundColor(self):
        self.tx.setStyleSheet("background:yellow")  # 自己输入需要的颜色

    def Backgroundimg(self):
        self.tx.setStyleSheet("background-image:url(img.jpg)")  # 需要输入正确的图像地址

    def testbackground(self):
        self.tx.setTextBackgroundColor(QColor(255, 0, 0))  # 需要自己设置颜色


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x:QWidget = Example()
    sys.exit(app.exec_())