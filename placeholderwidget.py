from PyQt6 import QtWidgets


class PlaceholderWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PlaceholderWidget, self).__init__(parent)
        QtWidgets.QLabel("Placeholder", self)

# widget.children().append(label)
