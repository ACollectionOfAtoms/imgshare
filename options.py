import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class OptionWindow(QWidget):

    def __init__(self):
        super(OptionWindow, self).__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(500,500,500,320)
        self.setWindowTitle('Options')

        self.show()
