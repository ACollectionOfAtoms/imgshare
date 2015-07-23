#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime


# Need to implement handling when imgur is overloaded!
class Uploader:
    def __init__(self, client, trayIcon):
        self.client = client
        self.trayIcon = trayIcon

    def upload(self, path):
        self.trayIcon.showMessage('Uploading', '...')  # Growl required for this to work on OSX < 10.8
        album = None
        config = {
                'album': album,
                'name': path,
                'title': path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        image = self.client.upload_from_path(path, config=config, anon=False)

        link = image['link']
        self.trayIcon.showMessage('Upload Complete',link)

        print "Here it is: {0} ".format(image['link'])
