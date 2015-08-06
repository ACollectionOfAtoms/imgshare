#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tray
from PyQt5 import QtGui, QtCore, QtWidgets
from webbrowser import open_new_tab
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError


class Login(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        client_id = '912116b2944a624'
        client_secret = 'c4fc62a0b62338f9e25f9062147e2d0ca44f428e'
        self.client = ImgurClient(client_id, client_secret)

        self.setWindowTitle('imgshare')
        self.resize(250, 50)
        self.center()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

        self.message = QtWidgets.QLabel('please enter pin')
        self.message.setObjectName('message')
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.textpin = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('login', self)

        self.buttonPin = QtWidgets.QPushButton('get pin', self)

        self.buttonLogin.clicked.connect(self.handle_pin)
        self.buttonPin.clicked.connect(self.authenticate)

        layout = QtWidgets.QGridLayout(self)
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
            QLabel#message {
                color: #85BF25;
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
            credentials = self.client.authorize(str(self.textpin.text()), 'pin')
            self.accept()
            self.client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
            return self.client

        except ImgurClientError as e:
            QtWidgets.QMessageBox.warning(self, str(e.status_code), str(e.error_message))

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app_icon = QtGui.QIcon()
    app_icon.addFile('icons/ico-16.png', QtCore.QSize(16, 16))
    app_icon.addFile('icons/ico-32.png', QtCore.QSize(32, 32))
    app_icon.addFile('icons/ico-64.png', QtCore.QSize(64, 64))
    app_icon.addFile('icons/ico-128.png', QtCore.QSize(128, 128))
    app_icon.addFile('icons/ico-256.png', QtCore.QSize(256, 256))
    app_icon.addFile('icons/ico-512.png', QtCore.QSize(512, 512))
    app_icon.addFile('icons/ico-1024.png', QtCore.QSize(1024, 1024))

    app.setWindowIcon(app_icon)
    app.setQuitOnLastWindowClosed(False)  # Ensures app is only exited through Tray icon
    greet = Login()

    if greet.exec_() == QtWidgets.QDialog.Accepted:
        tray.launch(greet.client, app_icon)
        sys.exit(app.exec_())
