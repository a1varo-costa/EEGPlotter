from app import plotter as plt
from app import serialport as ser

from PyQt5.QtWidgets import QApplication

import sys

if __name__ == '__main__':
    app = QApplication([])

    s = ser.SerialReader('COM4', 9600, 0.1, 1024)
    p = plt.Plotter(s, 1/(30*10e-3))
    p.start()
    
    sys.exit(app.exec_())
    
