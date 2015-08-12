#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QWidget, QDesktopWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QGridLayout,
                             QLabel, QPushButton, QLineEdit, QComboBox, QFileDialog, QFrame)
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
            return {(str(album.title) if album.title else 'Main'): (str(album.id))
                    for album in self.client.get_account_albums('me')}

        except ImgurClientError as e:
            stat_code = str(e.status_code)
            err_msg = str(e.error_message)
            self.trayIcon.showMessage(stat_code, "Error: " + "\"" + err_msg + "\"" +
                                      "\nimgur is having issues! You may want to restart.")

    def initUI(self):
        if self.layout() is None:
            self.center()
            self.setWindowTitle('Options')
            # Grid for checkbox options
            pref_header = QLabel('Preferences')
            pref_header.setObjectName('preferences')  # In order to customize style in stylesheet

            set_header = QLabel('Settings')
            set_header.setObjectName('settings')
            h_line = QFrame()
            h_line.setFrameShape(QFrame.HLine)

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
            album_list = [alb for alb in self.albums.keys() if alb != 'Main']
            album_choice.addItems(album_list)

            album_choice.insertSeparator(len(album_list) + 1)
            album_choice.insertItem(len(album_list) + 2, 'Main')
            album_choice.setCurrentIndex(len(album_list) + 1)

            album_choice.activated[str].connect(self.set_album)

            set_dir_button = QPushButton("Set")
            set_dir_button.clicked.connect(lambda: self.select_dir(dir_field))
            set_dir_button.setMaximumWidth(80)

            options_layout = QGridLayout()
            options_layout.addWidget(pref_header, 0, 0)
            options_layout.addWidget(cb_click_send, 1, 0)
            options_layout.addWidget(cb_auto_send, 2, 0)
            options_layout.addWidget(cb_no_copy, 3, 0)
            options_layout.addWidget(cb_auto_open, 4, 0)
            options_layout.addWidget(h_line, 5, 0)
            options_layout.addWidget(cb_launch_start, 6, 0)

            options_layout.addWidget(set_header, 7, 0)
            options_layout.addWidget(set_dir, 8, 0)
            options_layout.addWidget(dir_field, 9, 0)
            options_layout.addWidget(set_dir_button, 10, 0)
            options_layout.addWidget(set_album, 11, 0)
            options_layout.addWidget(album_choice, 12, 0)
            ok_button = QPushButton("Ok")
            cancel_button = QPushButton("Cancel")

            # Window Layout
            hbox = QHBoxLayout()
            hbox.addWidget(ok_button)
            hbox.addWidget(cancel_button)
            hbox.addStretch(1)

            vbox = QVBoxLayout()
            vbox.addLayout(options_layout)
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
                    color: black;
                    background-color: white;
                    selection-background-color: rgb(50,50,50);
                    selection-color: #85BF25;
                    border: 1px black;
                    border-radius: 3px;
                    padding: 1px 18px 1px 3px;
                    min-width: 6em;
                }
                QComboBox QListView{
                    color: white;
                    border: 1px black;
                    border-radius: 3px;
                    padding: 1px 18px 1px 3px;
                    min-width: 6em;
                    border-color: #85BF25;
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
                    font: bold 12px;
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

    def set_album(self, album):
        self.loader.album = self.albums[album]

    def select_dir(self, field):
        str = QFileDialog.getExistingDirectory()
        if str != '':
            field.setText(str)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
