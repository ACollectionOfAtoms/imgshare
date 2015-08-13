#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import threading
import psutil
import os
import subprocess
from scanner import Scanner
from PyQt5 import QtWidgets
from options import OptionsWindow


class Tray(QtWidgets.QSystemTrayIcon):
    def __init__(self, client, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.client = client
        self.icon = icon
        self.user = self.client.get_account('me').url
        self.scanner = Scanner(self.client, self)
        self.options = OptionsWindow(self.client, self.scanner, self)
        self.options.init_options()

        self.stop_event = threading.Event()
        self.scan_thread = threading.Thread(target=self.scanner.scan, args=(self.stop_event,))
        self.scan_thread.start()

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
        sendAction.triggered.connect(self.copy_last)

        menu.addAction(sendAction)
        menu.addAction(optAction)
        menu.addSeparator()
        menu.addAction(exitAction)
        self.setContextMenu(menu)

    def appExit(self):
        # Reset OSX Screenshot storage
        with open(os.devnull, 'w') as nul:
            path = os.path.expanduser('~') + '/Desktop/'
            subprocess.call(["defaults", "write", "com.apple.screencapture", "location", path])
            subprocess.call(["killAll", "SystemUIServer"])

        kill_proc_tree(me)
        self.stop_event.set()
        self.scanner.scan(self.stop_event)
        sys.exit()

    def show_options(self):
        self.options.show_opts()

    def copy_last(self):
        if self.scanner.loader.link == '':
            self.scanner.loader.to_clipboard()
        else:
            self.scanner.loader.to_clipboard()
            self.scanner.loader.copy_notification()


def launch(client, icon):
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    trayIcon = Tray(client, icon, w)
    trayIcon.show()
    trayIcon.showMessage("Log In Successful!", "Hello {} (~:".format(trayIcon.user), 0)
    sys.exit(app.exec_())


def kill_proc_tree(pid, including_parent=True):
    parent = psutil.Process(pid)
    if including_parent:
        parent.kill()

me = os.getpid()
