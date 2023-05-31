#!/usr/bin/python3
# Initialize PyQT
from PySide2.QtCore import *
from PySide2.QtUiTools import *
from PySide2.QtWidgets import *
# The fondamental for working with python
import sys, signal

class MainWindow ( QMainWindow):
    # Create settings for the software
    settings = QSettings('Your Name', 'Name of the software')
    settings.setFallbacksEnabled(False)
    version = 'Your version'

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        loader = QUiLoader()
        # Load the ui file
        ui_file = QFile('mainwindow.qml')
        self.ui = loader.load(ui_file)
        ui_file.close()
        # Set the MainWindow Title
        self.ui.setWindowTitle('Name of the software - ' + self.version)
        # When the software are closed on console the software is closed
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
