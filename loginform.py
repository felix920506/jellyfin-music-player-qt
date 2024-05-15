from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QFormLayout,
                             QStackedWidget, QCheckBox, QSizePolicy)
from internationalization import translate
import sessioncontroller


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
        layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

        self.serverField = QLineEdit()
        self.serverField.setPlaceholderText('https://jellyfin.example.com/path')
        self.userField = QLineEdit()
        self.userField.setPlaceholderText('user')
        self.passwordField = QLineEdit()
        self.passwordField.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addRow(translate('loginServer'), self.serverField)
        layout.addRow(translate('loginUser'), self.userField)
        layout.addRow(translate('loginPassword'), self.passwordField)

        self.pwCheckbox = QCheckBox(translate('loginShowPW'))
        self.pwCheckbox.setChecked(False)
        self.pwCheckbox.checkStateChanged.connect(lambda: self.passwordField.setEchoMode(
            QLineEdit.EchoMode.Normal if self.pwCheckbox.isChecked() else QLineEdit.EchoMode.Password
        ))

        layout.addRow(QLabel(), self.pwCheckbox)

        # TODO: Implement QuickConnect Login
        # QCButton = QPushButton(translate('loginQuickConnect'))
        # QCButton.clicked.connect(lambda: self.parent().setCurrentIndex(1))
        # layout.addRow(QCButton)

        loginButton = QPushButton(translate('loginConnectAndLogin'))
        layout.addRow(loginButton)

        self.setLayout(layout)

    def login(self):
        server = self.serverField.text()
        user = self.userField.text()
        password = self.passwordField.text()

        res = sessioncontroller.loginUsername(server, user, password)
        match res:
            case 'Success':
                pass
            case 'BadCredentials':
                pass
            case 'UnknownError':
                pass
            case 'InvalidCredentials':
                pass


