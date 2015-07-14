import sys
from PyQt4 import QtGui

class Tray():
    class SystemTrayIcon(QtGui.QSystemTrayIcon):
        def __init__(self, icon, parent=None):
            QtGui.QSystemTrayIcon.__init__(self, icon, parent)
            menu = QtGui.QMenu(parent)
            exitAction = menu.addAction("Exit")
            self.setContextMenu(menu)

    def main(self):
        app = QtGui.QApplication(sys.argv)

        w = QtGui.QWidget()
        trayIcon = self.SystemTrayIcon(QtGui.QIcon("ico.png"), w)

        trayIcon.show()
        sys.exit(app.exec_())