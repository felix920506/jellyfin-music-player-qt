from PyQt6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit, QFormLayout, QStackedWidget
from internationalization import translate

class loginForm(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.addWidget(loginFormNormal())
        self.addWidget(QLabel('Test'))
        self.setCurrentIndex(0)


class loginFormNormal(QWidget):
    def __init__(self):
        super(loginFormNormal, self).__init__()

        layout = QFormLayout()

        self.serverField = QLineEdit()
        self.userField = QLineEdit()
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addRow(translate('loginServer'), self.serverField)
        layout.addRow(translate('loginUser'), self.userField)
        layout.addRow(translate('loginPassword'), self.passwordField)

        self.setLayout(layout)