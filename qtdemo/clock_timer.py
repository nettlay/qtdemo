import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time, sys

class UpdateTime(QThread):
    time_show = pyqtSignal(str)

    def run(self):
        while 1:
            a = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.time_show.emit(str(a))
            time.sleep(1)


class LogWnd(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(300, 300, 440, 350)
        self.setWindowTitle('记录工作内容')

        self.log_field = QTextEdit(self)
        self.log_field.setGeometry(20, 20, 300, 300)

        # layout
        self.log_btn = QPushButton('Save', self)
        self.log_btn.move(350, 300)
        self.close_btn = QPushButton('Close', self)
        self.close_btn.move(350, 270)

        self.close_btn.clicked.connect(self.close_event)

        # self.closeEvent()
    def close_event(self):
        self.log_btn.setEnabled(True)
        self.close()


class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle('字体设置')

        # layout
        layout = QGridLayout(self)
        self.setGeometry(300, 300, 250, 50)

        self.time_label = QLabel('123456',self)
        self.time_label.resize(230, 40)
        self.timer_btn = QPushButton('Start', self)

        self.timer_btn.clicked.connect(self.start_action)

        layout.addWidget(self.time_label, 0 ,0)
        layout.addWidget(self.timer_btn, 0, 1)

        self.thread = UpdateTime()
        self.thread.time_show.connect(self.display_time)
        self.thread.start()

    def start_action(self):
        if self.timer_btn.text()=="Start":
            self.timer_btn.setText('Stop')
            pass
        if self.timer_btn.text()== "Stop":
            self.timer_btn.setEnabled(False)
            self.logwnd = LogWnd()  # 加了self之后打开子窗口会停留，否则子窗口会一闪而过
            print(self.logwnd, 'begin')
            self.logwnd.show()

    def display_time(self, msg):
        self.time_label.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    x = Main()
    x.show()
    # a = LogWnd()
    # a.show()
    sys.exit(app.exec_())


