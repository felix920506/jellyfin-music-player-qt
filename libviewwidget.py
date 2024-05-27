from PyQt6.QtWidgets import QWidget, QHBoxLayout
from placeholderwidget import PlaceholderWidget


class LibViewWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(PlaceholderWidget())
        layout.addWidget(PlaceholderWidget())
        self.setLayout(layout)