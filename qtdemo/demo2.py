from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from demo1 import prowler  # 子界面的py文件的位置，函数导入自己根据文件名和位置修改


class main(QWidget):
    def __init__(self, parent=None):
        super(main, self).__init__(parent)

        self.sendData = {"first": "I", "second": "Love", "third": "You"}

        self.OpenBtn = QPushButton("呼唤子界面")
        self.OpenEdit = QLineEdit()
        self.ShowBtn = QPushButton("显示")
        self.ShowEdit = QLineEdit()
        self.ShowBtn1 = QPushButton("显示1")
        self.ShowEdit1 = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(self.OpenBtn, 0, 0)
        layout.addWidget(self.OpenEdit, 0, 1)
        layout.addWidget(self.ShowBtn, 1, 0)
        layout.addWidget(self.ShowEdit, 1, 1)
        layout.addWidget(self.ShowBtn1, 2, 0)
        layout.addWidget(self.ShowEdit1, 2, 1)

        QHBLayout = QHBoxLayout()
        QVBLayout = QVBoxLayout()

        QHBLayout.addLayout(layout)
        QVBLayout.addLayout(QHBLayout)

        self.setLayout(QVBLayout)

        self.OpenBtn.clicked.connect(self.Connect)
        self.setWindowTitle("Father")

    def Connect(self):
        self.widget = prowler()
        self.widget.show()
        self.widget.switchSig.connect(self.reaction)

    def reaction(self, string):
        print("父界面接收到的字典", string)
        self.sondata = string
        tmp = self.sondata["first"]
        print("父界面接收到的值", tmp)
        self.ShowEdit.setText(tmp)
        tmp1 = self.sondata["second"]
        print("父界面接收到的值1", tmp1)
        self.ShowEdit1.setText(tmp1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Jenney = main()
    Jenney.show()
    sys.exit(app.exec_())