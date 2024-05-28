from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from placeholderwidget import PlaceholderWidget
from libviewmainwidget import LibViewMainWidget


class LibViewWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.addWidget(PlaceholderWidget())
        layout.addWidget(LibViewMainWidget())
        self.setLayout(layout)
