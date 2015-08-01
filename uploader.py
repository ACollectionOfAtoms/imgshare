#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from options import OptionsWindow
import pyperclip


# Need to implement handling when imgur is overloaded!
class Uploader:
    def __init__(self, client, options, trayIcon):
        self.client = client
        self.options = options
        self.trayIcon = trayIcon
        self.album = self.options.set_album(default=True)

    def upload(self, path):
        self.trayIcon.showMessage('Uploading', '...', 1)
        path_list = path.split('/')
        screen_name = path_list[-1]
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        album = self.album
        config = {
                'album': album,
                'name': screen_name,
                'title': screen_name,
                'description': 'Uploaded with imgshare on {0}'.format(dt)
                }
        image = self.client.upload_from_path(path, config=config, anon=False)
        link = image['link']

        self.trayIcon.showMessage('Upload Complete', link, 1)

        if self.trayIcon.messageClicked:
            self.to_clipboard(link)

    def to_clipboard(self, link):
        pyperclip.copy(link)
