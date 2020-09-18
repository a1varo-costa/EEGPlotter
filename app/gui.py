from .uigen import mainWindowUI as mainWinUI
from .      import plotter, rect

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
        
        self.rectGridLayout = QGridLayout(self.ui.keyboardWidget)

        for setting in self.settings:
            blkrect = rect.BlinkRect(label=setting[0], freq=setting[1])
            self.rectGridLayout.addWidget(blkrect, setting[2], setting[3])

    def closeEvent(self, evt):
        if self.stream is not None:
            self.stream.close()
        super().closeEvent(evt)

