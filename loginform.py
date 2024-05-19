from PyQt6.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit, QFormLayout,
                             QStackedWidget, QCheckBox, QSizePolicy)
from PyQt6.QtCore import QThread, pyqtSignal, QObject
from internationalization import translate
import sessioncontroller
import popupmessage


resArea: str


class loginForm(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.addWidget(loginFormNormal())
        self.addWidget(QLabel('Test'))
        self.setCurrentIndex(0)


class loginFormNormal(QWidget):

    loginCompleteSignal = pyqtSignal(str)

    def __init__(self):
        super(loginFormNormal, self).__init__()

        self.workerThread: QThread | None = None

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

        self.loginButton = QPushButton(translate('loginConnectAndLogin'))
        self.loginButton.clicked.connect(self.login)
        layout.addRow(self.loginButton)

        testButton = QPushButton('Test')
        testButton.clicked.connect(
            lambda: popupmessage.warningMessageBox('Test', 'Test Message').exec()
        )
        layout.addRow(testButton)

        self.setLayout(layout)

    def login(self):

        self.loginButton.setEnabled(False)

        server = self.serverField.text()
        user = self.userField.text()
        password = self.passwordField.text()

        self.workerThread = loginThread(server, user, password)
        self.workerThread.start()
        self.workerThread.finished.connect(self.handleLoginRes)

    def handleLoginRes(self, res: str):
        match res:
            case 'Success':
                self.parent().parent().setCurrentIndex(1)
            case 'BadCredentials':
                popupmessage.warningMessageBox(translate('loginBadCredentials'), res).exec()
            case 'UnknownError':
                popupmessage.warningMessageBox(translate('loginUnknownError'), res).exec()
            case 'InvalidUrl':
                popupmessage.warningMessageBox(translate('loginInvalidUrl'), res).exec()

        self.loginButton.setEnabled(True)


class loginThread(QThread):
    finished = pyqtSignal(str)

    def __init__(self, server: str, user: str, password: str):
        super().__init__()
        self.server = server
        self.user = user
        self.password = password

    def run(self):
        # global resArea
        self.finished.emit(
            sessioncontroller.loginUsername(self.server, self.user, self.password)
        )
        self.quit()
        self.deleteLater()



