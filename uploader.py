#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import pyperclip
from PyQt5 import QtGui


# Need to implement handling when imgur is overloaded!
class Uploader:
    def __init__(self, client, trayIcon):
        self.client = client
        self.trayIcon = trayIcon

    def upload(self, path):
        self.trayIcon.showMessage('Uploading', '...', 1)
        print self.client.get_account_albums('me')
        album = None
        config = {
                'album': album,
                'name': path,
                'title': path,
                'description': 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        image = self.client.upload_from_path(path, config=config, anon=False)
        link = image['link']

        self.trayIcon.showMessage('Upload Complete', link, 1)

        if self.trayIcon.messageClicked:
            self.to_clipboard(link)

    def to_clipboard(self, link):
        pyperclip.copy(link)
