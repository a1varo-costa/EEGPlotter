from . import filters

from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import numpy as np


class Plotter(object):
    def __init__(self, ui, stream, f):
        super().__init__()
        self.ui = ui
        self.stream = stream

        self.pltFilter = self.ui.plotWidget.addPlot(row=0, col=0)
        self.pltFFT = self.ui.plotWidget.addPlot(row=1, col=0)
        
        self.curveFilter = self.pltFilter.plot()
        self.curveFilter = self.pltFFT.plot()

        self.filterOpt = ''
        self.lpfCutoff = 99999.99
        self.hpfCutoff = 0.000001
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
        if self.filterOp == 'Low Pass':
            y = filters.lowPass(self.stream.buf, 
                                self.samplingFreq,
                                self.lpfCutoff)
            self.curveFilter.setData(y)

        elif self.filterOp == 'High Pass':
            y = filters.highPass(self.stream.buf, 
                                 self.samplingFreq,
                                 self.hpfCutoff)
            self.curveFilter.setData(y)

        else:
            self.curveFilter.setData(self.stream.buf)
        
        x, y = filters.fftUtil(np.arange(self.stream.buf_max_size), 
                               self.stream.buf, 
                               1/self.samplingFreq)
        self.curveFilter.setData(x, y)
    
    def _onCBoxTextChanged(self, t):
        self.filterOp = t
        
        if self.filterOp == 'Low Pass':
            self.ui.cutoffSpinBox.setValue(self.lpfCutoff)
        
        elif self.filterOp == 'High Pass':
            self.ui.cutoffSpinBox.setValue(self.hpfCutoff)
        
        else:
            self.ui.cutoffSpinBox.setValue(0.0)
        
        print('Selected filter => %s' % t)

    def _onSBoxValueChanged(self, d):
        if self.filterOp == 'Low Pass':
            self.lpfCutoff = d
            
            print('LPF Cut-Off = %f' % self.lpfCutoff)
        
        elif self.filterOp == 'High Pass':
            self.hpfCutoff = d
           
            print('HPF Cut-Off = %f' % self.hpfCutoff)
    
    def _connectSlots(self):
        self.ui.filterComboBox.\
            currentTextChanged.connect(self._onCBoxTextChanged)
        self.ui.cutoffSpinBox.\
            valueChanged.connect(self._onSBoxValueChanged)
