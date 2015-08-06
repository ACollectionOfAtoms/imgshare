#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import psutil
import os
from scanner import Scanner
from PyQt5 import QtGui, QtWidgets
from options import OptionsWindow


class Tray(QtWidgets.QSystemTrayIcon):
    def __init__(self, client, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.MessageIcon
        self.client = client
        self.icon = icon
        self.user = self.client.get_account('me').url
        self.options = OptionsWindow(self.client)
        self.scanner = Scanner(self.client, self.options, self)

        self.stop_event = threading.Event()
        self.c_thread = threading.Thread(target=self.scanner.scan, args=(self.stop_event,))
        self.c_thread.start()

        menu = QtWidgets.QMenu(parent)

        exitAction = QtWidgets.QAction("&Quit     ", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip('Good bye')
        exitAction.triggered.connect(self.appExit)

        optAction = QtWidgets.QAction("&Options...  ", self)
        optAction.setShortcut("Ctrl+O")
        optAction.setStatusTip("Customize")
        optAction.triggered.connect(self.show_options)

        sendAction = QtWidgets.QAction("Copy Link of Last Uploaded Image", self)
        sendAction.setShortcut("Ctrl+S")
        sendAction.setStatusTip("...")
        # Trigger goes here should grey-out if
        # Auto send to clipboard option enabled.

        menu.addAction(sendAction)
        menu.addAction(optAction)
        menu.addAction(exitAction)
        self.setContextMenu(menu)

    def appExit(self):
        kill_proc_tree(me)
        self.stop_event.set()
        self.scanner.scan(self.stop_event)
        sys.exit()

    def show_options(self):
        self.options.initUI()


def launch(client, icon):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = Tray(client, QtGui.QIcon(icon), w)
    trayIcon.show()
    trayIcon.showMessage("Log In Successful!", "Hello {} (~:".format(trayIcon.user), 0)
    sys.exit(app.exec_())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
