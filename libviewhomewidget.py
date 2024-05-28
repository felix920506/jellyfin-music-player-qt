from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
import sessioncontroller
from internationalization import translate


class LibViewHomeWidget(QWidget):
    def __init__(self):
        super().__init__()

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
