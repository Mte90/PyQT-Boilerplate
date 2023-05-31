#!/usr/bin/python3
# Initialize PyQT
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import QQmlApplicationEngine
import sys, signal

# Execute the software
app = QGuiApplication(sys.argv)

# Start the software
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('mainwindow.qml')
# When the software are closed on console the software are closed
signal.signal(signal.SIGINT, signal.SIG_DFL)
# Add the close feature at the program with the X
sys.exit(app.exec())
