#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

class Uploader:
    def __init__(self, client, path):
        self.client = client
        self.path = path

    def upload(self):
        print str(self.client) + "*"*5
        album = 'imgshare_album'
        config = {
                'album' : album,
                'name' : self.path,
                'title' : self.path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        print "Uploading Image"
        image = self.client.upload_from_path(self.path, config=config, anon=False)
        print "Done"
        return image
