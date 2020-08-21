from app import serialport as ser
from app import gui

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app = QApplication([])

    stream = ser.SerialReader('COM4', 9600, 0.1, 1024)
    settings = [('A', 3, 0, 0), ('B', 6, 0, 1)]
    plot = gui.MainUI(stream, 1/(30*10e-3), settings)
    plot.show()

    sys.exit(app.exec_())
    
