import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel
from placeholderwidget import PlaceholderWidget
from loginform import loginForm

app = QApplication(sys.argv)

window = QMainWindow()

mainWidget = QStackedWidget()
mainWidget.addWidget(loginForm())
mainWidget.setCurrentIndex(0)

mainWidget.addWidget(PlaceholderWidget())
window.setCentralWidget(mainWidget)
window.show()

app.exec()
