import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon


class OptionsWindow(QWidget):

    def __init__(self):
        super(OptionsWindow, self).__init__()

    def initUI(self):
        self.setGeometry(500, 500, 500, 320)
        self.setWindowTitle('Options')

        self.show()
