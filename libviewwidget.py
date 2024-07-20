from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QScrollArea
from placeholderwidget import PlaceholderWidget
from libviewmainwidget import LibViewMainWidget


class LibViewWidget(QScrollArea):
    def __init__(self):
        super().__init__()

        # layout.addWidget(PlaceholderWidget())
        # layout.addWidget(LibViewMainWidget())
        # self.setLayout(layout)
        self.setWidgetResizable(True)
        self.setWidget(LibViewMainWidget())
