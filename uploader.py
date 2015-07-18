#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


class Uploader:
    def __init__(self):
        self.client = ''
        self.path = ''

    def upload(self):
        album = 'imgshare_album'
        config = {
                'album': album,
                'name': self.path,
                'title': self.path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        print "Uploading Image"
        if self.client != '':
            image = self.client.upload_from_path(self.path, config=config, anon=False)
        else:
            print 'No Client!'

        print "Done"


def load(client, path):
    tool = Uploader()
    tool.client = client
    tool.path = path
    print str(tool.client) + " PASSED TO UPLOADER LOAD FUNCTION"
    print str(tool) + " This tool has the client object"
    return tool
