#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from options import OptionsWindow
import pyperclip
from imgurpython.helpers.error import ImgurClientError


class Uploader:
    def __init__(self, client, options, trayIcon, auto=False, never_copy=False):
        self.client = client
        self.options = options
        self.trayIcon = trayIcon
        self.auto = auto
        self.never_copy = never_copy

        if self.never_copy:
            self.auto = False

        self.album = None
        self.album = self.options.album(default=True)
        self.link = ''

        if not self.auto and not self.never_copy:
            self.trayIcon.messageClicked.connect(self.message_click_copy)

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

            if self.auto and not self.never_copy:
                self.to_clipboard()
                self.copy_notification()

        except ImgurClientError as e:
            self.trayIcon.showMessage("Upload Error!", "\"" + str(e.error_message + "\""))

    def to_clipboard(self):
        if self.link == '':
            self.trayIcon.showMessage('Nothing to Send To Clipboard', 'You haven\'t taken a picture yet!', 0)
        else:
            pyperclip.copy(self.link)

    def copy_notification(self):
        self.trayIcon.showMessage("Link Copied", "imgur link sent to clipboard")

    def message_click_copy(self):  # Can be infinite loop if user continues to click. But who would do that?!
        if self.link == '':
            pass
        else:
            self.to_clipboard()
            self.copy_notification()
            self.trayIcon.messageClicked.connect(self.message_click_copy)  # Needs to be reconnected! May be OSX Qt Bug.

