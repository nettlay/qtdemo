from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
class Example(QWidget):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super().__init__()
        self._initUI()
        self.center()
        #self.Use_Qss()
        #self.show()
    def closewindow(self):
        self.close()


    def center(self, screenNum=0):
        '''多屏居中支持'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

        self.normalGeometry2 = QRect((screen.width() - size.width()) / 2 + screen.left(),
                                     (screen.height() - size.height()) / 2, size.width(), size.height())
        self.setGeometry((screen.width() - size.width()) / 2 + screen.left(),
                         (screen.height() - size.height()) / 2, size.width(), size.height())

    def _initUI(self):
        #self.resize(800, 400)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        #def Use_Qss(self):
        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./p1.jpg")))
        self.setPalette(palette)
        #self.setObjectName("MainWindow")
        # #todo 1 设置窗口背景图片
        #self.setStyleSheet("#MainWindow{border-image:url(.\p1.jpg);}")
        # todo 2 设置窗口背景色
        #self.setStyleSheet("#MainWindow{background-color: gray}")
        btn1 = QPushButton("back", self)
        btn1.move(240, 300)
        btn1.setStyleSheet(
            '''QPushButton{
              border:none;
        color:white;
        background:blue;
        border:1px solid #F3F3F5;
        border-radius:10px;
        font-size:20px;
        height:40px;
        padding-left:5px;
        padding-right:10px;
        text-align:left;
    }
    QPushButton:hover{
        color:black;
        border:1px solid #F3F3F5;
        border-radius:10px;
        background:LightGray;
    }
        ''')
        btn1.clicked.connect(self.buttonClicked)
        btn1.clicked.connect(self.closewindow)
        self.lb1 = QLabel(self)
        qle = QLineEdit(self)

        qle.move(60, 300)
        self.lb1.move(60, 40)
        qle.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    background:cyan;
                    width:120px;
                    border-radius:10px;
                    padding:2px 4px;
                    font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif; 
            }''')
        self.lb1.setStyleSheet(
            '''QLabel{
            color:red;
            font-size:60px;
            font-family: 微软雅黑,宋体,Arial,Helvetica,Verdana,sans-serif; 
            }
            '''
        )



        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(600, 300, 480, 370)
        self.setWindowTitle('单行文本')
        self.show()
    def buttonClicked(self):
        from qtdemo import UI
        self.qt = UI.Example1()
        self.qt.initUI()
        self.qt.center()

    def onChanged(self, text):
        self.lb1.setText(text)
        self.lb1.adjustSize()


    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())