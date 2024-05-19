from PyQt6.QtWidgets import QWidget, QVBoxLayout
from playerwidget import PlayerWidget
from placeholderwidget import PlaceholderWidget


class mainUIWidget(QWidget):
    def __init__(self):
        super(mainUIWidget, self).__init__()

        layout = QVBoxLayout()

        layout.addWidget(PlaceholderWidget())
        layout.addWidget(PlaceholderWidget())
        layout.addWidget(PlayerWidget())

        self.setLayout(layout)
