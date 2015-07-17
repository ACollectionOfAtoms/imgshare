import sys
import scanner
from PyQt4 import QtGui, QtCore

class Tray():
    class SystemTrayIcon(QtGui.QSystemTrayIcon):
        def __init__(self, icon, parent=None):
            QtGui.QSystemTrayIcon.__init__(self, icon, parent)
            menu = QtGui.QMenu(parent)

            exitAction = QtGui.QAction("&Exit", self)
            exitAction.triggered.connect(QtGui.QApplication.quit) # This will quit the app but also raise an error...?!
            menu.addAction(exitAction)

            self.setContextMenu(menu)

    def main(self):
        app = QtGui.QApplication(sys.argv)

        w = QtGui.QWidget()
        trayIcon = self.SystemTrayIcon(QtGui.QIcon("ico.png"), w)

        trayIcon.show()
        sys.exit(app.exec_())
