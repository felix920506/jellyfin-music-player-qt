from PyQt6.QtWidgets import QStackedWidget
from placeholderwidget import PlaceholderWidget
from libviewhomewidget import LibViewHomeWidget


class LibViewMainWidget(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.addWidget(LibViewHomeWidget())
        self.addWidget(PlaceholderWidget())
