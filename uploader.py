#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


class Uploader:
    def __init__(self):
        self.client = ''

    def upload(self, path):
        album = None
        config = {
                'album': album,
                'name': path,
                'title': path,
                'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
                }
        print "Uploading Image"
        if self.client != '':
            print "*"*10 + " Success! " + "*"*10
            image = self.client.upload_from_path(path, config=config, anon=False)
            print "Here it is: {0} ".format(image['link'])
        else:
            print 'No Client!'

        print "Done"


def load(client):
    tool = Uploader()
    tool.client = client
    print str(tool.client) + " PASSED TO UPLOADER LOAD FUNCTION"
    print str(tool) + " This tool has the client object"
    return tool
