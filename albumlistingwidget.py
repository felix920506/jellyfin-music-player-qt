from PyQt6 import QtCore, QtGui, QtWidgets, QtGui
from pixmapFromHttp import PixmapFromHttp
import mediacontroller
import textwrap


class albumListingWidget(QtWidgets.QWidget):
    def __init__(self, albumid: str, artist: str = None, name: str = None):
        super(albumListingWidget, self).__init__()

        self.id = albumid
        self.image = PixmapFromHttp(mediacontroller.getImageUrl(self.id), synchronous=True)
        self.imageWidget = QtWidgets.QLabel()
        self.imageWidget.setPixmap(self.image.scaledToHeight(100))
        self.name = name
        self.artist = artist

        self.setLayout(QtWidgets.QHBoxLayout())
        self.layout().addWidget(self.imageWidget)
        self.layout().addWidget(QtWidgets.QLabel(f'{textwrap.shorten(self.artist, width=50)} - {self.name}'))

