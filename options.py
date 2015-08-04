from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QTabWidget, QListWidget
from PyQt5.QtGui import QIcon


class OptionsWindow(QWidget):

    def __init__(self, client):
        super(OptionsWindow, self).__init__()
        self.client = client
        self.albums = self.get_album_dict()

        self.setWindowTitle("Options")
        self.setWindowIcon(QIcon("ico.png"))
        self.layout = QVBoxLayout(self)

        tab_widget = QTabWidget()
        tab1 = QWidget()
        tab2 = QWidget()

        p1_vertical = QVBoxLayout(tab1)
        album_list = QListWidget()
        album_list.addItems(list(self.albums.keys()))
        p1_vertical.addWidget(album_list)
        p2_vertical = QVBoxLayout(tab2)

        tab_widget.addTab(tab1, "Settings")
        # tab_widget.addTab(tab2, "Preferences")

        self.layout.addWidget(tab_widget)

        self.setStyleSheet("""
            QWidget {
                background-color: rgb(50,50,50);
            }
            QLineEdit {
                border-color: solid black;
                selection-color: green;
            }
            QLabel {
                color: white;
            }
            QListWidget {
                color: white;
            }
            QTabWidget {
                background-color: rgb(50,50,50);
                border-color: solid black;
                border-width: 2px;
                color: rgb(255,255,255);
                font: bold 14px;
            }
            """)

    def get_album_dict(self):
        return {(str(album.title) if album.title else 'untitled'):
                (str(album.id))
                for album in self.client.get_account_albums('me')}

    def album(self, default, path=''):
        if "imgshare" in self.albums and default:
            self.album = self.albums["imgshare"]

        elif default:
            config ={
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
        self.resize(500, 320)
        self.center()
        self.setWindowTitle('Options')

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
