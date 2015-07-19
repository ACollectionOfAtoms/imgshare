#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


class Uploader:
    def __init__(self, client):
        self.client = client

    def upload(self, path):
        album = None
        config = {
                'album': album,
                'name': path,
                'title': path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        if self.client != '':
            image = self.client.upload_from_path(path, config=config, anon=False)
            print "Here it is: {0} ".format(image['link'])
        else:
            pass
