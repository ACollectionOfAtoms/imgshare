import sys
import scanner
import imgurpython
from PyQt4 import QtGui, QtCore


class Tray(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)

        exitAction = menu.addAction("Exit")
        self.connect(exitAction, QtCore.SIGNAL('triggered()'), self.appExit)
        self.setContextMenu(menu)

    def appExit(self):
        sys.exit()


def launch():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    trayIcon = Tray(QtGui.QIcon("ico.png"), w)

    trayIcon.show()
    sys.exit(app.exec_())
