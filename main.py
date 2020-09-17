from app import serialport as ser
from app import gui

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app = QApplication([])

    stream = ser.SerialReader('COM4', 9600, 0.1, 1024)
    settings = [('A', 3, 0, 0), ('B', 6, 0, 1), ('C', 10, 0, 2)]
    plot = gui.MainUI(stream, 1/(5000e-6), settings)

    plot.show()

    sys.exit(app.exec_())
    
