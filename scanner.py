#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import threading
from uploader import Uploader


class Scanner:
    """ Scans an OSX desktop directory, the default storage for screenshots! """
    def __init__(self, client, trayIcon):
        self.client = client
        self.trayIcon = trayIcon
        self.screenshot_path = ''
        self.loader = Uploader(self.client, self.trayIcon)
        self.desktop = os.path.expanduser('~') + '/Desktop/'
        self.num_files_in_dir = len(self._dsk_dir())
        self.stop_event = threading.Event()
        self.regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){1,2}\sat\s(\d){1,2}\.(\d){1,2}\.(\d){1,2}\s(PM|AM)\.(\w){3}'

    def _dsk_dir(self):
        dir_list = [f for f in os.listdir(self.desktop) if f[0] != '.']
        return dir_list

    def _check_name(self, name):
        """ Returns bool on whether file name is in OSX screenshot regex pattern """
        found = re.search(self.regex, name)
        return found.__repr__() != 'None'

    def scan(self, stop_event):
        """ Create new set containing new file; find difference in set, store name,
            update self.num_files_in_dir,
            check if name matches the OSX screenshot syntax, and finally
            Either store the screenshot path and continue to scan, or
            simply continue to scan!
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
            self.num_files_in_dir = len(self._dsk_dir())

            if self._check_name(new_file):
                reg_object = re.search(self.regex, new_file)
                new_file = reg_object.group()
                self.screenshot_path = self.desktop + new_file

                self.loader.upload(self.screenshot_path)
                self.scan(self.stop_event)
            else:
                self.scan(self.stop_event)
