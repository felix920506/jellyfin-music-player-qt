import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel
from placeholderwidget import PlaceholderWidget
from loginform import loginForm

app = QApplication(sys.argv)

window = QStackedWidget()
window.addWidget(loginForm())
window.setCurrentIndex(0)
window.show()

app.exec()
