from PyQt6.QtCore import QThread, pyqtSignal, QCoreApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea
import sessioncontroller
from internationalization import translate
import mediacontroller
from albumlistingwidget import albumListingWidget
import time


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
        self.runUpdate()

    def updateLatest(self, latest: list[str]) -> None:
        for i in latest:
            w = albumListingWidget(i['Id'], i['AlbumArtist'], i['Name'])
            self.latestListLayout.addWidget(w)
            QCoreApplication.processEvents()


        time.sleep(1)
        self.worker1.quit()
        self.worker1.deleteLater()

        pass

    def updateLibs(self, libs: list[str]) -> None:

        # TODO: mediacontroller.getlibs returning empty list

        # print(libs)
        # print()
        pass

    def runUpdate(self) -> None:
        self.worker1 = updateLatestThread(self)
        self.worker1.finished.connect(self.updateLatest)
        self.worker1.start()

        # self.worker2 = updateLibsThread()
        # self.worker2.finished.connect(self.updateLibs)
        # self.worker2.start()
        pass


class updateLibsThread(QThread):
    finished = pyqtSignal(list)

    def __init__(self):
        super().__init__()

    def run(self):

        # TODO: below call returning empty list

        res = mediacontroller.getLibs()
        self.finished.emit(res)

        self.quit()
        self.deleteLater()


class updateLatestThread(QThread):
    finished = pyqtSignal(list)

    def __init__(self, target: LibViewHomeWidget):
        super().__init__()
        self.target = target

    def run(self):
        res = mediacontroller.getLatest()
        self.finished.emit(res)
        # self.target.updateLatest(res)
