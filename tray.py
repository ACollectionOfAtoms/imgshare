#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import psutil
import os
from scanner import Scanner
from PyQt5 import QtGui, QtCore, QtWidgets


class Tray(QtWidgets.QSystemTrayIcon):
    def __init__(self, client, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.client = client
        self.scanner = Scanner(self.client, self)
        self.stop_event = threading.Event()
        self.c_thread = threading.Thread(target=self.scanner.scan, args=(self.stop_event,))
        self.c_thread.start()
        self.menu = QtWidgets.QMenu(parent)
        self.exitAction = QtWidgets.QAction("&Quit", self)
        self.exitAction.setShortcut("Cmd+Q")
        self.exitAction.setStatusTip('Good bye')
        self.exitAction.triggered.connect(self.appExit)

        self.menu.addAction(self.exitAction)
        # self.trigger.connect(exitAction, QtCore.pyqtSignal('triggered()'), self.appExit)
        self.setContextMenu(self.menu)

    def appExit(self):
        kill_proc_tree(me)
        self.stop_event.set()
        self.scanner.scan(self.stop_event)
        sys.exit()


def launch(client):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    trayIcon = Tray(client, QtGui.QIcon("ico.png"), w)
    trayIcon.show()
    sys.exit(app.exec_())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
