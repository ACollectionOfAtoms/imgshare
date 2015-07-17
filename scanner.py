#!/usr/bin/python
# -*- coding: utf-8 -*-
#This object should continually scan a directory, looking for newly created screenshots by the user.

import os
import re

class Scanner:
    """ Scans an OSX desktop directory, the default storage for screenshots!
    """
    def __init__(self):
        self.num_files_in_dir = len(self.dsk_dir())
        self.screenshot_path = ''
        self.desktop = os.path.expanduser('~') + '/Desktop/'

    def dsk_dir(self):
        dir = os.listdir(self.desktop)
        return dir

    def check_name(self, name):
        """ Returns bool on whether file name is in OSX screenshot regex pattern"""
        regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){2}\sat\s(\d){2}\.(\d){2}\.(\d){2}\s(AM|PM)'
        Found = re.(regex, name)
        if type(Found) != 'NoneType':
            return True
        else:
            return False

    def scan(self):
        """ Create new set containing new file; find difference in set, store name,
            update self.num_files_in_dir,
            check if name matches the OSX screenshot syntax, and finally
            Either store the screenshot path and continue to scan, or
            simply continue to scan!
        :rtype : object
        """
        num_files = self.num_files_in_dir
        file_list_set_a = set(self.dsk_dir())

        while len(self.dsk_dir()) == num_files:
            pass
        else:
            file_list_set_b = set(self.dsk_dir())
            new_file = file_list_set_a ^ file_list_set_b
            new_file = next(iter(nw_file))
            self.num_files_in_dir = len(self.dsk_dir())

            if self.check_name(new_file):
                self.screenshot_path = self.desktop + new_file
                self.scan()
            else:
                self.scan()





