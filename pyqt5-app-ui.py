#!/usr/bin/python3
# Initialize PyQT
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
# The fondamental for working with python
import sys, signal

class MainWindow ( QMainWindow):
    # Create settings for the software
    settings = QSettings('Your Name', 'Name of the software')
    settings.setFallbacksEnabled(False)
    version = 'Your version'

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        # Load the ui file
        self.ui = uic.loadUi("mainwindow.ui", self)
        # Set the MainWindow Title
        self.ui.setWindowTitle('Name of the software - ' + self.version)
        # When the software are closed on console the software are closed
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        # Show the form
        self.ui.show()


def main():
    # Start the software
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    # Add the close feature at the program with the X
    sys.exit(app.exec_())



# Execute the software
main()
