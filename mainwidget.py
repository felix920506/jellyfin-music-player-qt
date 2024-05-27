from PyQt6.QtWidgets import QWidget, QVBoxLayout
from playerwidget import PlayerWidget
from placeholderwidget import PlaceholderWidget
from libviewwidget import LibViewWidget


class mainUIWidget(QWidget):
    def __init__(self):
        super(mainUIWidget, self).__init__()

        layout = QVBoxLayout()

        layout.addWidget(LibViewWidget())
        layout.addWidget(PlayerWidget())

        self.setLayout(layout)
