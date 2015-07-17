#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime


def upload(client, image_path):
    clnt = client
    print str(clnt) + "*"*5
    album = 'imgshare_album'
    config = {
            'album' : album,
            'name' : image_path,
            'title' : image_path,
            'description' : 'Uploaded with imgshare on {0}'.format(datetime.now())
            }
    print "Uploading Image"
    image = clnt.upload_from_path(image_path, config=config, anon=False)
    print "Done"
    return image
