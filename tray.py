#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import threading
import psutil
import os
from scanner import Scanner
from PyQt4 import QtGui, QtCore


class Tray(QtGui.QSystemTrayIcon):
    def __init__(self, client, icon, parent=None):
        self.client = client
        self.scanner = Scanner(self.client, self)
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


def launch(client):
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()

    trayIcon = Tray(client, QtGui.QIcon("ico.png"), w)

    trayIcon.show()
    sys.exit(app.exec_())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
