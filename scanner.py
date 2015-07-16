#!/usr/bin/python
# -*- coding: utf-8 -*-
#This object shoudl continually scan a directory, looking for newly created screenshots by the user.

import os
import re
from datetime import datetime

class Scanner():
    def current_time(selfs):
        format = 'Screen Shot %Y-%m-%d at %H.%M.%S %p'
        cur_time = datetime.strftime(datetime.now(), format)
        cur_time_lst = cur_time.split()
        return cur_time_lst

    def dsk_dir(self):
        desktop = os.path.expanduser('~') + '/Desktop/'
        dir = os.listdir(desktop)
        return dir

    def check_name(self, name):
        """ Returns bool if file name is OSX screenshot regex pattern"""
        regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){2}\sat\s(\d){2}\.(\d){2}\.(\d){2}\s(AM|PM)'
        Found = re.(regex, name)
        if type(Found) != 'NoneType':
            return True
        else:
            return False


