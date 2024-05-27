import requests
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtGui import QPixmap


class PixmapFromHttp(QPixmap):
    def __init__(self, url: str = None) -> None:
        self.url: str | None = None
        self.workerThread: getImageThread | None = None
        super().__init__()

        self.setImageFromUrl(url)

    def setImageFromUrl(self, url: str) -> None:
        if url is None:
            return

        self.url = url
        self.workerThread = getImageThread(url)
        self.workerThread.start()
        self.workerThread.finished.connect(self.loadFromData)


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
