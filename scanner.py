#!/usr/bin/python
# -*- coding: utf-8 -*-
# This object should continually scan a directory, looking for newly created screenshots by the user.

import os
import re
import threading


class Scanner:
    """ Scans an OSX desktop directory, the default storage for screenshots!
    """
    def __init__(self):
        self.screenshot_path = ''
        self.desktop = os.path.expanduser('~') + '/Desktop/'
        self.num_files_in_dir = len(self._dsk_dir())
        self.stop_event = threading.Event()
        self.regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){2}\sat\s(\d){2}\.(\d){2}\.(\d){2}\s(AM|PM)\.(\w){3}'

    def _dsk_dir(self):
        dir_list = os.listdir(self.desktop)
        return dir_list

    def _check_name(self, name):
        """ Returns bool on whether file name is in OSX screenshot regex pattern"""
        found = re.search(self.regex, name)
        return found.__repr__() != 'None'

    def scan(self, stop_event):
        """ Create new set containing new file; find difference in set, store name,
            update self.num_files_in_dir,
            check if name matches the OSX screenshot syntax, and finally
            Either store the screenshot path and continue to scan, or
            simply continue to scan!
        :rtype : object
        """
        num_files = self.num_files_in_dir
        file_list_set_a = set(self._dsk_dir())

        if stop_event.isSet():
            return

        while len(self._dsk_dir()) == num_files and not stop_event.isSet():
            pass
        else:
            file_list_set_b = set(self._dsk_dir())
            new_file = file_list_set_a ^ file_list_set_b
            new_file = next(iter(new_file))
            reg_object = re.search(self.regex, new_file)
            new_file = reg_object.group()

            self.num_files_in_dir = len(self._dsk_dir())

            if self._check_name(new_file):
                print new_file
                self.screenshot_path = self.desktop + new_file
                print self.screenshot_path
                self.scan(self.stop_event)
            else:
                print 'Scanner don\'t care!' + ' **** ' + new_file
                self.scan(self.stop_event)





