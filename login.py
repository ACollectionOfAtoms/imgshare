#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from webbrowser import open_new_tab
from imgurpython import ImgurClient


class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.textpin = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonPin = QtGui.QPushButton('Get PIN', self)

        self.buttonLogin.clicked.connect(self.handle_pin)
        self.buttonPin.clicked.connect(self.authenticate)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textpin)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonPin)

    def authenticate(self):
        #authenticate imgur user login
        client_id = '912116b2944a624'
        client_secret = 'c4fc62a0b62338f9e25f9062147e2d0ca44f428e'
        client = ImgurClient(client_id, client_secret)
        authorization_url = client.get_auth_url('pin')
        open_new_tab(authorization_url)

    def handle_pin(self):
        pass



class Window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)

    if Login().exec_() == QtGui.QDialog.Accepted:
        window = Window()
        window.show()
        sys.exit(app.exec_())




