from .uigen import mainWindowUI as mainWinUI
from .      import plotter

from PyQt5.QtWidgets import QMainWindow, QGridLayout, QLabel, QSizePolicy


class MainUI(QMainWindow):
    def __init__(self, stream, sfreq, settings):
        super().__init__()
        self.stream = stream
        self.samplingFreq = sfreq

        self.settings = settings
        
        self._loadUI()
    
    def _loadUI(self):
        self.ui = mainWinUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.plt = plotter.Plotter(self.ui, self.stream, self.samplingFreq)
        
    def closeEvent(self, evt):
        if self.stream is not None:
            self.stream.close()
        super().closeEvent(evt)

