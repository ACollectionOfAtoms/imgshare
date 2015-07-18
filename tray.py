#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
import psutil
import os
import scanner
from PyQt4 import QtGui, QtCore


class Tray(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        self.client = ''
        self.scanner = scanner.load(self.client)
        self.stop_event = threading.Event()
        self.c_thread = threading.Thread(target=self.scanner.scan, args=(self.stop_event,))
        self.c_thread.start()

        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)

        exitAction = menu.addAction("Exit")
        self.connect(exitAction, QtCore.SIGNAL('triggered()'), self.appExit)
        self.setContextMenu(menu)

    def appExit(self):
        kill_proc_tree(me)
        self.stop_event.set()
        self.scanner.scan(self.stop_event)
        sys.exit()

    def load_client(self):
        if self.client == '':
            print 'Client Not loaded'
        else:
            self.scanner = scanner.load(self.client)


def launch(client):
    print str(client) + " PASSED TO LAUNCH FUNCTION"
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    trayIcon = Tray(QtGui.QIcon("ico.png"), w)
    trayIcon.client = client
    trayIcon.load_client()
    print str(trayIcon.client) + " PASSED TO trayIcon OBJECT"

    trayIcon.show()
    sys.exit(app.exec_())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()

