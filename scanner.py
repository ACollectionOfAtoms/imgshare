#!/usr/bin/env python
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
        self.loader = Uploader(self.client, self.trayIcon)

        self.screenshot_path = ''
        self.scan_path = os.path.expanduser('~') + '/Desktop/'
        self.files_in_dir = self.dir_list()
        self.stop_event = threading.Event()
        self.regex = 'Screen\sShot\s(\d){4}-(\d){2}-(\d){1,2}\sat\s(\d){1,2}\.(\d){1,2}\.(\d){1,2}\s(PM|AM)\.(\w){3}'

        self.file_list_set_a = set(self.files_in_dir)
        self.file_list_set_b = set(self.files_in_dir)

    def dir_list(self):
        d_list = [f for f in os.listdir(self.scan_path) if f[0] != '.']
        return d_list

    def _check_name(self, name):
        """ Returns bool on whether file name is in OSX screenshot regex pattern """
        return re.match(self.regex, name) is not None

    def scan(self, stop_event):
        """ Create set containing new file; find difference in set, store name,
            update self.files_in_dir,
            check if name matches the OSX screenshot syntax, and finally
            Either store the screenshot path and continue to scan, or
            simply continue to scan.
        """
        if stop_event.isSet():
            return

        while len(self.dir_list()) <= len(self.files_in_dir) and not stop_event.isSet():
            pass
        else:
            self.file_list_set_b = set(self.dir_list())
            if len(self.file_list_set_a) == len(self.file_list_set_b):  # Catch if folder was changed
                self.scan(self.stop_event)
            else:
                new_file = self.file_list_set_a ^ self.file_list_set_b
                new_file = next(iter(new_file))
                self.files_in_dir = self.dir_list()

                if self._check_name(new_file):
                    reg_object = re.search(self.regex, new_file)
                    new_file = reg_object.group()
                    self.screenshot_path = self.scan_path + new_file

                    self.loader.upload(self.screenshot_path)
                    self.scan(self.stop_event)
                else:
                    self.scan(self.stop_event)
