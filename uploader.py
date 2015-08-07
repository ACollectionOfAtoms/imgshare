#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from options import OptionsWindow
import pyperclip
from imgurpython.helpers.error import ImgurClientError


class Uploader:
    def __init__(self, client, options, trayIcon):
        self.client = client
        self.options = options
        self.trayIcon = trayIcon
        self.album = None
        self.album = self.options.album(default=True)

        self.link = ''

    def upload(self, path):
        try:
            self.trayIcon.showMessage('Uploading', '...', 0)
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
            self.link = image['link']

            self.trayIcon.showMessage('Upload Complete', self.link, 0)

            if self.trayIcon.messageClicked:
                self.to_clipboard()
                self.showMessage('Link Copied', 'imgur link image has been sent to clipboard.')

        except ImgurClientError as e:
            self.trayIcon.showMessage(str(e.status_code), str(e.error_message))

    def to_clipboard(self):
        if self.link == '':
            self.trayIcon.showMessage('Nothing to Send To Clipboard', 'You haven\'t taken a picture yet!', 0)
        else:
            pyperclip.copy(self.link)
