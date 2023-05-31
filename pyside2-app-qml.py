#!/usr/bin/python3
# Initialize PySyde
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtQml import QQmlApplicationEngine
import sys, signal

# Execute the software
app = QGuiApplication(sys.argv)

# Start the software
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('mainwindow.qml')

if len(engine.rootObjects()) == 0:
    quit()

# When the software are closed on console the software are closed
signal.signal(signal.SIGINT, signal.SIG_DFL)
# Add the close feature at the program with the X
sys.exit(app.exec_())
