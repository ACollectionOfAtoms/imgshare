#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QLabel, QPushButton, QLineEdit, QComboBox)
from uploader import Uploader


class OptionsWindow(QWidget):
    def __init__(self, client, scanner, trayIcon):
        super(OptionsWindow, self).__init__()
        self.client = client
        self.scanner = scanner
        self.loader = self.scanner.loader
        self.trayIcon = trayIcon
        self.albums = self.get_album_dict()
        self.scan_dir = self.scanner.scan_path

    def get_album_dict(self):
        try:
            return {(str(album.title) if album.title else 'untitled'): (str(album.id))
                    for album in self.client.get_account_albums('me')}

        except ImgurClientError as e:
            stat_code = str(e.status_code)
            err_msg = str(e.error_message)
            self.trayIcon.showMessage(stat_code, "Error: " + "\"" + err_msg + "\"" +
                                      "\nimgur is having issues! You may want to restart.")

    def album(self, default, path=''):
        if "imgshare" in self.albums and default:
            self.album = self.albums["imgshare"]

        elif default:
            config = {
                'title': "imgshare",
                'description': "Images Uploaded with the imgshare app",
                'privacy': "hidden",
                'layout': "grid"
            }
            self.client.create_album(config)
            self.albums = self.get_album_dict()
            return self.albums["imgshare"]
        else:
            return path

    def initUI(self):
        if self.layout() is None:
            self.center()
            self.setWindowTitle('Options')
            # Grid for checkbox options
            set_header = QLabel('Preferences')
            set_header.setObjectName('preferences')  # In order to customize style in stylesheet

            pref_header = QLabel('Settings')
            pref_header.setObjectName('settings')

            set_dir = QLabel('Set Screenshot Directory:')
            set_album = QLabel('Set imgur Album:')

            cb_click_send = QCheckBox('Click Balloon to Copy Image Link', self)
            cb_click_send.setChecked(True)

            cb_no_copy = QCheckBox('Never Copy Image Link')
            cb_auto_open = QCheckBox('Open Image in Browser')
            cb_auto_send = QCheckBox('Automatically Copy Image Link')
            cb_launch_start = QCheckBox('Launch on Start up')

            cb_no_copy.setChecked(True)
            cb_no_copy.setDisabled(True)

            cb_click_send.stateChanged.connect(lambda: cb_no_copy.setChecked(not cb_no_copy.isChecked()))
            cb_click_send.stateChanged.connect(lambda: cb_auto_send.setDisabled(cb_auto_send.isEnabled()))
            cb_click_send.stateChanged.connect(lambda: cb_auto_send.setChecked(cb_auto_send.isChecked()))
            cb_click_send.stateChanged.connect(self.toggle_click)

            cb_click_send.stateChanged.emit(1)

            cb_auto_send.stateChanged.connect(lambda: cb_click_send.setDisabled(cb_click_send.isEnabled()))
            cb_auto_send.stateChanged.connect(lambda: cb_click_send.setChecked(cb_click_send.isChecked()))
            cb_auto_send.stateChanged.connect(lambda: cb_no_copy.setChecked(not cb_no_copy.isChecked()))
            cb_auto_send.stateChanged.connect(self.toggle_auto_upload)

            cb_auto_open.stateChanged.connect(self.toggle_auto_open)

            dir_field = QLineEdit()
            dir_field.insert(self.scan_dir)

            album_choice = QComboBox()
            album_list = self.albums.keys()
            album_choice.addItems(album_list)

            check_box_layout = QGridLayout()
            check_box_layout.addWidget(set_header, 0, 0)
            check_box_layout.addWidget(cb_click_send, 1, 0)
            check_box_layout.addWidget(cb_no_copy, 1, 1)
            check_box_layout.addWidget(cb_auto_open, 1, 2)
            check_box_layout.addWidget(cb_auto_send, 2, 0)
            check_box_layout.addWidget(cb_launch_start, 2, 1)

            check_box_layout.addWidget(pref_header, 3, 0)
            check_box_layout.addWidget(set_dir, 4, 0)
            check_box_layout.addWidget(dir_field, 5, 0)
            check_box_layout.addWidget(set_album, 4, 1)
            check_box_layout.addWidget(album_choice, 5, 1)
            ok_button = QPushButton("Ok")
            cancel_button = QPushButton("Cancel")

            # Window Layout
            hbox = QHBoxLayout()
            hbox.addStretch(1)
            hbox.addWidget(ok_button)
            hbox.addWidget(cancel_button)

            vbox = QVBoxLayout()
            vbox.addLayout(check_box_layout)
            vbox.addLayout(hbox)

            self.setLayout(vbox)
            self.setStyleSheet("""
                QWidget {
                    background-color: rgb(50,50,50);
                }
                QLineEdit {
                    border-color: 1px white;
                    border-radius: 3px;
                    padding: 0 8px;
                    selection-color: #85BF25;
                    background-color: white;
                }
                 QComboBox {
                    border: 1px black;
                    border-radius: 3px;
                    padding: 1px 18px 1px 3px;
                    min-width: 6em;
                }
                QComboBox::drop-down {
                    width: 15px;
                }
                QLabel#preferences {
                    color: #85BF25;
                    font: bold 14px;
                }
                QLabel#settings {
                    color: #85BF25;
                    font: bold 14px;
                }
                QLabel {
                    color: white;
                }
                QComboBox {
                    background-color: white;
                }
                QLabel#set_header {
                    color: white;
                    font: bold 14px;
                }
                QCheckBox {
                    color: white;
                }
                QListWidget {
                    color: white;
                }
                QPushButton {
                    background-color: rgb(50,50,50);
                    border-color: solid black;
                    border-width: 2px;
                    color: rgb(255,255,255);
                    font: bold 14px;
                }
                """)
            self.show()
        else:
            self.show()

    # Both Scanner and Options objects connect to loader with new settings.
    def toggle_click(self):
        bool_switch = not self.loader.click
        self.scanner.loader = self.loader = Uploader(self.client, self.trayIcon, click=bool_switch)

    def toggle_auto_upload(self):
        bool_switch = not self.loader.auto
        self.scanner.loader = self.loader = Uploader(self.client, self.trayIcon, auto=bool_switch)

    def toggle_auto_open(self):  # Doesn't affect upload process; no need to create new instance.
        bool_switch = not self.loader.auto_open
        self.loader.auto_open = bool_switch

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
