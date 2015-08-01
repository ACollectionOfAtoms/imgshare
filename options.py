from PyQt5.QtWidgets import QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon


class OptionsWindow(QWidget):

    def __init__(self, client):
        super(OptionsWindow, self).__init__()
        self.client = client
        self.albums = self.get_album_dict()

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
            QPushButton {
                background-color: rgb(50,50,50);
                border-color: solid black;
                border-width: 2px;
                color: rgb(255,255,255);
                font: bold 14px;
            }
            """)

    def get_album_dict(self):
        return {str(album.title): str(album.id) if album.title else 'untitled' for album in self.client.get_account_albums('me')}

    def set_album(self, default, path=''):
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
