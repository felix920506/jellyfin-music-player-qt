from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QProgressBar, QPushButton, QSlider, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtCore import QThread, pyqtSignal


import sessioncontroller
import requests


class PlayerWidget(QWidget):
    def __init__(self):
        super(PlayerWidget, self).__init__()

        self.res: QNetworkReply | None = None
        self.workerThread: getImageThread | None = None

        # Construct Layout
        layout = QHBoxLayout()

        self.image = QPixmap()
        self.imageWidget = QLabel()
        self.imageWidget.setPixmap(self.image)

        songInfoLayout = QVBoxLayout()
        self.title = QLabel('Innocence')
        self.artist = QLabel('Powerless feat. Sennzai')
        songInfoLayout.addWidget(self.title)
        songInfoLayout.addWidget(self.artist)

        self.progress = QSlider(Qt.Orientation.Horizontal)

        playButton = QPushButton('⏯')
        nextButton = QPushButton('⏭')

        playButton.setFlat(True)
        nextButton.setFlat(True)

        self.volume = QSlider(Qt.Orientation.Horizontal)

        layout.addWidget(self.imageWidget)
        layout.addLayout(songInfoLayout)
        layout.addWidget(self.progress)
        layout.addWidget(playButton)
        layout.addWidget(nextButton)
        layout.addWidget(self.volume)

        # Set Layout
        self.setLayout(layout)

    def setImageFromHttp(self, url: str):
        self.workerThread = getImageThread(url)
        self.workerThread.start()
        self.workerThread.finished.connect(self.setImageFromData)

    def setImageFromData(self, data):
        self.image.loadFromData(data)
        self.imageWidget.setPixmap(self.image.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio))


class getImageThread(QThread):
    finished = pyqtSignal(bytes)

    def __init__(self, url: str):
        super(getImageThread, self).__init__()
        self.url = url

    def run(self):
        res = requests.get(self.url)

        self.finished.emit(res.content)

        self.quit()
        self.deleteLater()

