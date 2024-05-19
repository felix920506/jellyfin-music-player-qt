import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QLabel

# Custom Widgets
from placeholderwidget import PlaceholderWidget
from loginform import loginForm

# Other things
import sessioncontroller
import qt_material

app = QApplication(sys.argv)

window = QMainWindow()

# Add Widgets

mainWidget = QStackedWidget()
mainWidget.addWidget(loginForm())
mainWidget.setCurrentIndex(0)

mainWidget.addWidget(PlaceholderWidget())

if sessioncontroller.validateCurrentSession():
    mainWidget.setCurrentIndex(1)

window.setCentralWidget(mainWidget)

# TODO: Make theme a setting
qt_material.apply_stylesheet(app, theme='./themes/dark_amber.xml')

window.show()
app.exec()
