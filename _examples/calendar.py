#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        calendar = QCalendarWidget()
        layout.addWidget(calendar)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
