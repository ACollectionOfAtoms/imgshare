# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:30:14 2015

@author: Adam

ZetCode PyQt4 tutorial

In this example, we ceate a simple window in PyQt4.

Author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""
import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()


    def initUI(self):
        
        self.setGeometry(0,0,250,150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('web.png'))
        
        
        self.show()


def main():


    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()