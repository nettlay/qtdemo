from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys


class prowler(QWidget):
    switchSig = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(prowler, self).__init__(parent)

        self.sendData = {"first": "I", "second": "Love", "third": "You"}

        self.SendBtn = QPushButton("向父界面传值1")
        self.SendEdit = QLineEdit()
        self.SendBtn1 = QPushButton("向父界面传值2")
        self.SendEdit1 = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.SendBtn, 0, 0)
        layout.addWidget(self.SendEdit, 0, 1)
        layout.addWidget(self.SendBtn1, 1, 0)
        layout.addWidget(self.SendEdit1, 1, 1)

        QHBLayout = QHBoxLayout()
        QVBLayout = QVBoxLayout()

        QHBLayout.addLayout(layout)
        QVBLayout.addLayout(QHBLayout)

        self.setLayout(QVBLayout)
        self.SendBtn.clicked.connect(self.SendData)
        self.SendBtn1.clicked.connect(self.SendData1)

        self.setWindowTitle("Son")

    def SendData(self):
        tmp = self.SendEdit.text()
        print("向父界面发送的值", tmp)
        self.sendData["first"] = tmp
        print("向父界面发送的字典", self.sendData)
        self.switchSig.emit(self.sendData)

    def SendData1(self):
        tmp = self.SendEdit1.text()
        print("向父界面发送的值", tmp)
        self.sendData["second"] = tmp
        print("向父界面发送的字典", self.sendData)
        self.switchSig.emit(self.sendData)


if __name__ == "__main__":
    print('aaa')
    app = QApplication(sys.argv)
    Jenney = prowler()
    Jenney.show()
    sys.exit(app.exec_())