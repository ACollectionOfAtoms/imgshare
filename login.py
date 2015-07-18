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
        self.message = QtGui.QLabel('Enter PIN')
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.client = ImgurClient(client_id, client_secret)
        self.textpin = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonPin = QtGui.QPushButton('Get PIN', self)

        self.buttonLogin.clicked.connect(self.handle_pin)
        self.buttonPin.clicked.connect(self.authenticate)

        self.setStyleSheet("""
            background-color: rgb(49,49,49);
            color: rgb(255,255,255);
            """)

        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.message)
        layout.addWidget(self.textpin)
        layout.addWidget(self.buttonPin)
        layout.addWidget(self.buttonLogin)

    def authenticate(self):
        # authenticate imgur user login
        authorization_url = self.client.get_auth_url('pin')
        open_new_tab(authorization_url)

    def handle_pin(self):
        try:
            self.client.authorize(str(self.textpin.text()), 'pin')
            self.accept()
            print str(self.client) + "THE ORIGINAL"
            return self.client

        except ImgurClientError as e:
            QtGui.QMessageBox.warning(self, str(e.status_code), str(e.error_message))


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    greet = Login()

    if greet.exec_() == QtGui.QDialog.Accepted:
        print str(greet.client) + " Client passed to tray"
        tray.launch(greet.client)
        sys.exit(app.exec_())




