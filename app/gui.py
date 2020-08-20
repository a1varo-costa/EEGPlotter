from .ui import mainWindowUI as mainWinUI
from .   import plotter

from PyQt5.QtWidgets import QMainWindow


class MainUI(QMainWindow):
    def __init__(self, stream, sfreq):
        super().__init__()
        self.stream = stream
        self.samplingFreq = sfreq
        self._loadUI()
    
    def _loadUI(self):
        self.ui = mainWinUI.Ui_MainWindow()
        self.ui.setupUi(self)

        self.plt = plotter.Plotter(self.ui, self.stream, self.samplingFreq)
