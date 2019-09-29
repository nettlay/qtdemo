from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example1(QMainWindow):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        super().__init__()
        self.initUI()
        self.center()

    def closewin(self):
        self.close()

    def center(self, screenNum=0):
        '''多屏居中支持'''

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()

        self.normalGeometry2 = QRect((screen.width() - size.width()) / 2 + screen.left(),
                                     (screen.height() - size.height()) / 2, size.width(), size.height())
        self.setGeometry((screen.width() - size.width()) / 2 + screen.left(),
                         (screen.height() - size.height()) / 2, size.width(), size.height())

    def initUI(self):
        self.setFixedSize(QSize(400, 300))

        self.setWindowFlags(Qt.FramelessWindowHint)  # 无边框
        btn1 = QPushButton("Button 1", self)
        btn1.move(80, 150)

        btn2 = QPushButton("Button 2", self)
        btn2.move(220, 150)
        btn3 = QPushButton("☜", self)
        btn3.move(0, 0)
        btn4 = QPushButton("☞", self)
        btn4.move(300, 260)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.buttonClicked)
        btn3.clicked.connect(self.closewin)
        btn4.clicked.connect(self.buttonClicked)
        btn4.clicked.connect(self.closewin)

        self.statusBar()

        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.window().setStyleSheet('''
            QPushButton{
                border:none;
                color:black;
                font-size:20px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:red;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }

            QMainWindow{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-right:1px solid white;
                border-top-left-radius:12px;
                border-bottom-left-radius:12px;
                border-top-right-radius:12px;
                border-bottom-right-radius:12px;
            }
        ''')

          # 一定要加上
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        if sender.text() == "Button 1":

            print("执行%s" % sender.text())
        elif sender.text() == "Button 2":
            print("执行%s" % sender.text())
        elif sender.text() == "☜":
            print("执行%s" % sender.text())

            import qt5
            self.qt = qt5.Example()
            self.qt._initUI()

            self.qt.center()
        else:
            print("执行%s" % sender.text())
            import qt5

            self.qt = qt5.Example()
            self.qt._initUI()
            self.qt.center()


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
    ex = Example1()
    sys.exit(app.exec_())