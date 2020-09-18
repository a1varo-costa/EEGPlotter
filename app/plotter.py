from .processing import filters, average

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import mkPen

import numpy as np


class Plotter(object):
    def __init__(self, ui, stream, f):
        super().__init__()
        self.ui     = ui
        self.stream = stream

        self.pltFilter = self.ui.plotWidget.addPlot(row=0, col=0)
        self.pltFFT    = self.ui.plotWidget.addPlot(row=1, col=0)
        
        self.curveFilter  = self.pltFilter.plot()
        self.curveAverage = self.pltFilter.plot()
        self.curveFFT     = self.pltFFT.plot()

        if self.stream is not None:
            self.avrg = average.Averager(self.stream.buf_max_size, 5)
            self._penAvrg = mkPen('r') # red pen
        
        self.doFilter     = False
        self.ui.cutoffLowSpinBox.setEnabled(False)
        self.ui.cutoffHighSpinBox.setEnabled(False)

        self.lowCutoff    = f/2 - 0.01
        self.highCutoff   = 0.000001
        self.samplingFreq = f

        self._connectSlots()
        self._start()

    def _start(self):
        if self.stream is not None:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self._update)
            self.stream.open()
            self.timer.start(0)
            print('>> Plotting...\n')

    def _update(self):
        filtered = filters.butterworth(self.stream.buf, 
                                       self.samplingFreq, 
                                       (self.lowCutoff, self.highCutoff),
                                       2,
                                       fopt='bandpass')

        x, y = filters.fftUtil(np.arange(self.stream.buf_max_size), 
                               filtered, 
                               1/self.samplingFreq)

        self.curveFilter.setData(filtered)
        self.curveAverage.setData(self.avrg.calc(filtered), pen=self._penAvrg)
     
        y[0] = 0; # remove 0Hz bin
        self.curveFFT.setData(x, y)
    
    def _onCheckBoxStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.doFilter = True
            self.ui.cutoffLowSpinBox.setValue(self.lowCutoff)
            self.ui.cutoffLowSpinBox.setEnabled(True)
            self.ui.cutoffHighSpinBox.setValue(self.highCutoff)
            self.ui.cutoffHighSpinBox.setEnabled(True)
        
        else:
            self.doFilter = False
            self.ui.cutoffLowSpinBox.setEnabled(False)
            self.ui.cutoffHighSpinBox.setEnabled(False)

    def _onLowSpinBoxValueChanged(self, d):
        self.lowCutoff = d
    
    def _onHighSpinBoxValueChanged(self, d):
        self.highCutoff = d

    def _connectSlots(self):
        self.ui.filterCheckBox.\
            stateChanged.connect(self._onCheckBoxStateChanged)
        
        self.ui.cutoffLowSpinBox.\
            valueChanged.connect(self._onLowSpinBoxValueChanged)

        self.ui.cutoffHighSpinBox.\
            valueChanged.connect(self._onHighSpinBoxValueChanged)
