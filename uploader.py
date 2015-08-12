#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from webbrowser import open_new_tab
import pyperclip
from imgurpython.helpers.error import ImgurClientError


class Uploader:
    def __init__(self, client, trayIcon, click=False, auto=False, auto_open=False):
        """  default loader is set to click=True when loader is initialized by Options object """
        self.client = client
        self.trayIcon = trayIcon
        self.auto = auto
        self.auto_open = auto_open
        self.click = click

        self.album = None
        self.link = ''

        if self.click:
            self.trayIcon.messageClicked.connect(self.message_click_copy)  # Needs to be connected here! Qt Bug?!

    def upload(self, path):
        try:
            self.trayIcon.showMessage('Uploading', '...', 0)
            path_list = path.split('/')
            photo_name = path_list[-1]
            dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            album = self.album
            config = {
                    'album': album,
                    'name': photo_name,
                    'title': photo_name,
                    'description': 'Uploaded with imgshare on {0}'.format(dt)
                    }
            image = self.client.upload_from_path(path, config=config, anon=False)
            self.link = image['link']
            self.trayIcon.showMessage('Upload Complete', self.link, 0)

            if self.auto:
                self.to_clipboard()
                self.copy_notification()

            if self.auto_open:
                open_new_tab(self.link)

        except ImgurClientError as e:
            self.trayIcon.showMessage("Upload Error!", "\"" + str(e.error_message + "\""))

    def to_clipboard(self):
        if self.link == '':
            self.trayIcon.showMessage('Nothing to Send To Clipboard', 'You haven\'t taken a picture yet!', 0)
        else:
            pyperclip.copy(self.link)

    def copy_notification(self):
        self.trayIcon.showMessage("Link Copied", "imgur link sent to clipboard")

    def message_click_copy(self):  # Can be infinite loop if user continues to click. But who would do that?! (fix this)
        if self.link == '':
            pass
        else:
            self.to_clipboard()
            self.copy_notification()
            self.trayIcon.messageClicked.connect(self.message_click_copy)  # Needs to be reconnected! May be OSX Qt Bug.

