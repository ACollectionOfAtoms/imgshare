# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:30:14 2015

@author: Adam

"""
from PyQt4 import QtGui


class Login(QtGui.QDialog):

    def __init__(self):
        super(Login, QtGui.QDialog).__init__(self)
        self.textName = QtGui.QLineEdit(self)
        self.textPass = QtGui.QLineEdit(self)
        self.buttonLogin = QtGui.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtGui.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtGui.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

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