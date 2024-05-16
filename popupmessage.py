from PyQt6.QtWidgets import QMessageBox


class warningMessageBox(QMessageBox):
    def __init__(self, title: str, message: str) -> None:
        super(warningMessageBox, self).__init__()
        self.setIcon(QMessageBox.Icon.Warning)

        self.setWindowTitle(title)
        self.setText(message)
