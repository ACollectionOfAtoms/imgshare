import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon


class OptionsWindow(QWidget):

    def __init__(self, client):
        super(OptionsWindow, self).__init__()
        self.client = client

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(50,50,50);
            }
            QLineEdit {
                border-color: solid black;
                selection-color: green;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: rgb(50,50,50);
                border-color: solid black;
                border-width: 2px;
                color: rgb(255,255,255);
                font: bold 14px;
            }
            """)

    def initUI(self):
        self.resize(500, 320)
        self.center()
        self.setWindowTitle('Options')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
