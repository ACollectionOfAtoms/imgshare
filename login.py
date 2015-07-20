#!/usr/bin/python
# -*- coding: utf-8 -*-

import tray
from PyQt4 import QtGui, QtCore
from webbrowser import open_new_tab
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        client_id = '912116b2944a624'
        client_secret = 'c4fc62a0b62338f9e25f9062147e2d0ca44f428e'
        self.client = ImgurClient(client_id, client_secret)

        self.setWindowTitle('_imgshare')
        self.setWindowIcon(QtGui.QIcon("ico.png"))
        self.setGeometry(300, 300, 250, 50)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.message = QtGui.QLabel('please enter pin_ ')
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.textpin = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('login', self)

        self.buttonPin = QtGui.QPushButton('get pin', self)

        self.buttonLogin.clicked.connect(self.handle_pin)
        self.buttonPin.clicked.connect(self.authenticate)

        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.buttonPin, 0, 0)
        layout.addWidget(self.textpin, 1, 1)
        layout.addWidget(self.message, 0, 1)
        layout.addWidget(self.buttonLogin, 1, 0)

        self.setStyleSheet("""
            QDialog {
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


    def authenticate(self):
        # authenticate imgur user login
        authorization_url = self.client.get_auth_url('pin')
        open_new_tab(authorization_url)

    def handle_pin(self):
        try:
            self.client.authorize(str(self.textpin.text()), 'pin')
            self.accept()
            return self.client

        except ImgurClientError as e:
            QtGui.QMessageBox.warning(self, str(e.status_code), str(e.error_message))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    greet = Login()

    if greet.exec_() == QtGui.QDialog.Accepted:
        tray.launch(greet.client)
        sys.exit(app.exec_())
