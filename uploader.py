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
        self.album = None
        self.albums = self.get_album_dict()
        self.default_album(True)

    def get_album_dict(self):
        return {str(album.title): str(album.id) if album.title else 'untitled' for album in self.client.get_account_albums('me')}

    def default_album(self, default):
        if "imgshare" in self.albums and default:
            self.album = self.albums["imgshare"]

        elif default:
            config ={
                'title': "imgshare",
                'description': "Images Uploaded with the imgshare app",
                'privacy': "hidden",
                'layout': "grid"
            }
            self.client.create_album(config)
            self.albums = self.get_album_dict()
            self.album = self.albums["imgshare"]
        else:
            pass

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
