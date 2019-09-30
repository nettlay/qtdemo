import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time, sys


class UpdateTime(QThread):
    time_show = pyqtSignal(str)

    def run(self):
        while 1:
            a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.time_show.emit(str(a))
            time.sleep(1)


class UpdateSpend(QThread):
    time_spend = pyqtSignal(str)

    def run(self):
        spend = 0
        while 1:
            spend += 1
            d = int(spend / 60 / 60 / 24)
            h = int(spend / 60 / 60)
            m = int(spend / 60)
            s = spend % 60
            if d == 0 and h != 0:
                str1 = '{}时{}分{}秒'.format(h, m, s)
            elif d == 0 and h == 0 and m != 0:
                str1 = '{}分{}秒'.format(m, s)
            elif d == 0 and h == 0 and m == 0:
                str1 = '{}秒'.format(s)
            else:
                str1 = '{}天{}时{}分{}秒'.format(d, h, m, s)
            self.time_spend.emit(str(str1))
            time.sleep(1)


class LogWnd(QWidget):
    close_signal = pyqtSignal(str)

    def __init__(self, content):
        QWidget.__init__(self)
        self.setFixedSize(440, 350)
        self.setWindowTitle('记录工作内容')

        self.log_field = QTextEdit(content, self)
        self.log_field.setGeometry(20, 20, 300, 300)

        # layout
        self.log_btn = QPushButton('Save', self)
        self.log_btn.move(350, 300)
        self.close_btn = QPushButton('Close', self)
        self.close_btn.move(350, 270)

        self.close_btn.clicked.connect(self.close_event)

        # self.closeEvent()

    def close_event(self):
        print('close')
        self.close_signal.emit('closed')
        self.close()


class Main(QDialog):
    _startPos = None
    _endPos = None
    _isTracking = False

    def __init__(self):
        QDialog.__init__(self)
        self.log_content = 'hello'
        self.setWindowTitle('字体设置')
        self.setFixedSize(QSize(305, 80))
        # border-image:url(img.jpg);
        self.setStyleSheet(
            '''
            QFrame{
                border:none;
                color:white;
                background:lightblue;
                border:1px solid #F3F3F5;
                border-radius:10px;
                text-align:center;
                }
            QDialog{
                background-color:lightgreen;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-right:1px solid white;
                border-top-left-radius:12px;
                border-bottom-left-radius:12px;
                border-top-right-radius:12px;
                border-bottom-right-radius:12px;
                }
            QLabel{
                border:none;
                color:black;
                background:lightgreen;
                border:1px solid #F3F3F5;
                border-radius:10px;
                font-size:12px;
                height:40px;
                padding-left:10px;
                padding-right:10px;
                text-align:center;
                }
            QPushButton{
                border:none;
                color:white;
                background:gray;
                border:1px solid #F3F3F5;
                border-radius:10px;
                font-size:20px;
                height:40px;
                padding-left:10px;
                padding-right:10px;
                text-align:center;
                }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
                }
                '''
        )
        self.setAutoFillBackground(True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)  # 无边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 透明度，去掉圆弧边角
        # layout
        self.label_frame = QFrame(self)
        self.label_frame.resize(305, 75)

        layout = QGridLayout(self.label_frame)
        self.time_label = QLabel('Current:', self.label_frame)
        self.time_label.resize(230, 20)
        self.time_spend = QLabel('Spend  :', self.label_frame)
        self.time_spend.resize(230, 20)
        self.timer_btn = QPushButton('Start', self.label_frame)
        self.timer_btn.setFixedSize(70, 25)
        self.timer_close = QPushButton('Close', self.label_frame)
        self.timer_close.setFixedSize(70, 25)
        self.timer_btn.clicked.connect(self.start_action)
        self.timer_close.clicked.connect(self.closeW)

        layout.addWidget(self.time_label, 0, 0)
        layout.addWidget(self.timer_btn, 0, 1)
        layout.addWidget(self.time_spend, 1, 0)
        layout.addWidget(self.timer_close, 1, 1)

        self.thread = UpdateTime()
        self.thread.time_show.connect(self.display_time)
        self.thread.start()

    def closeW(self):
        try:
            self.logwnd.close()
        except:
            pass
        self.close()

    def start_action(self):
        if self.timer_btn.text() == "Start":
            self.timer_btn.setText('Stop')
            self.end_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            self.thread = UpdateSpend()
            self.thread.time_spend.connect(self.display_spend)
            self.thread.start()

        elif self.timer_btn.text() == "Stop":
            self.begin_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.timer_btn.setText('Start')
            self.timer_btn.setEnabled(False)
            self.logwnd = LogWnd(self.log_content)  # 加了self之后打开子窗口会停留，否则子窗口会一闪而过
            self.logwnd.close_signal.connect(self.update_close)
            self.logwnd.show()
            try:
                self.thread.disconnect()
                # print(self.end_time - self.begin_time)
            except:
                pass

    def update_close(self, msg):
        if msg == 'closed':
            self.timer_btn.setEnabled(True)
            print(self.begin_time)
            print(self.end_time)
            print(self.time_spend.text())

    def display_time(self, msg):
        self.time_label.setText("Current:" + msg)

    def display_spend(self, msg):
        self.time_spend.setText('Spend  :' + msg)

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
    x = Main()
    x.show()
    sys.exit(app.exec_())
