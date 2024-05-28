from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import sessioncontroller
from internationalization import translate
import mediacontroller


class LibViewHomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.worker1: updateLatestThread | None = None
        self.worker2: updateLibsThread | None = None

        layout = QVBoxLayout()

        layout.addWidget(QLabel(translate('homeLatestAlbums')))
        self.latestListLayout = QVBoxLayout()
        layout.addLayout(self.latestListLayout)

        layout.addWidget(QLabel(translate('homeMusicLibs')))
        self.libListLayout = QVBoxLayout()
        layout.addLayout(self.libListLayout)

        self.setLayout(layout)

    def updateLatest(self, latest: list[str]) -> None:
        pass

    def updateLibs(self, libs: list[str]) -> None:
        pass

    def runUpdate(self) -> None:
        self.worker1 = updateLatestThread()
        self.worker1.finished.connect(self.updateLatest)
        self.worker1.start()

        self.worker2 = updateLibsThread()
        self.worker2.finished.connect(self.updateLibs)
        self.worker2.start()


class updateLibsThread(QThread):
    finished = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        res = mediacontroller.getLibs()
        self.finished.emit(res)

        self.quit()
        self.deleteLater()


class updateLatestThread(QThread):
    finished = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):
        res = mediacontroller.getLatest()
        self.finished.emit(res)

        self.quit()
        self.deleteLater()
