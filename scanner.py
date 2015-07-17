#!/usr/bin/python
# -*- coding: utf-8 -*-
#This object shoudl continually scan a directory, looking for newly created screenshots by the user.

import os
import re
from datetime import datetime

class Scanner():
    def __init__(self):
        self.now = datetime.now()
        self.num_files_in_dir = len(self.dsk_dir)

    def current_time(self):
        format = 'Screen Shot %Y-%m-%d at %H.%M.%S %p'
        cur_time = datetime.strftime(datetime.now(), format)

    def dsk_dir(self):
        desktop = os.path.expanduser('~') + '/Desktop/'
        dir = os.listdir(desktop)
        return dir

    def check_name(self, name):
        """ Returns bool if file name is in OSX screenshot regex pattern"""
        regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){2}\sat\s(\d){2}\.(\d){2}\.(\d){2}\s(AM|PM)'
        Found = re.(regex, name)
        if type(Found) != 'NoneType':
            return True
        else:
            return False

    def scan(self):
        num_files = self.num_files_in_dir
        file_list_set_a = set(self.dskdir)

        while len(self.dsk_dir) == num_files:
            pass
        else:
            file_list_set_b = set(self.dskdir)
            new_file = file_list_set_a ^ file_list_set_b
            new_file = next(iter(nw_file))
            if self.check_name(new_file):





