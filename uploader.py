#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


class Uploader:
    def __init__(self, client, trayIcon):
        self.client = client
        self.trayIcon = trayIcon

    def upload(self, path):
        album = None
        config = {
                'album': album,
                'name': path,
                'title': path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        image = self.client.upload_from_path(path, config=config, anon=False)
        print "Here it is: {0} ".format(image['link'])
