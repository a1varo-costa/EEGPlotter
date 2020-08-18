from . import filters
from .ui import mainwindow_ui as main_ui

from PyQt5 import Qt, QtCore, QtGui, QtWidgets

import numpy as np


class Plotter(QtWidgets.QMainWindow):
    def __init__(self, stream=None, sfreq=1000.0, **kwargs):
        super(Plotter, self).__init__(**kwargs)

        self.sampling_freq = sfreq
        self.stream = stream
        self.lpf_freq = 1000.0
        self.hpf_freq = 0.0001

        self._load_layout()
        self._connect_slots()

    def start(self):
        if self.stream is not None:
            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self._update)
            self.stream.open()
            self.timer.start(0)
        self.show()
        print('>> Plotting...\n')

    def _update(self):
       
        if self.filter_op == 'Low Pass':
            y = filters.low_pass(self.stream.buf, 
                                 self.sampling_freq,
                                 self.lpf_freq)
            self.curve_filter.setData(y)

        elif self.filter_op == 'High Pass':
            y = filters.high_pass(self.stream.buf, 
                                  self.sampling_freq,
                                  self.hpf_freq)
            self.curve_filter.setData(y)

        else:
            self.curve_filter.setData(self.stream.buf)
        
        x, y = filters.fft_util(np.arange(self.stream.buf_max_size), 
                                self.stream.buf, 
                                1/self.sampling_freq)
        self.curve_fft.setData(x, y)

    def closeEvent(self, event):
        if self.stream is not None:
            self.stream.close()
        
        super().closeEvent(event)
    
    def _on_text_changed(self, t):
        self.filter_op = t
        
        if self.filter_op == 'Low Pass':
            self.ui.freq_lineEdit.setText(str(self.lpf_freq))
        
        elif self.filter_op == 'High Pass':
            self.ui.freq_lineEdit.setText(str(self.hpf_freq))
        
        else:
            self.ui.freq_lineEdit.setText('')
        
        print('Selected filter => %s' % t)

    def _on_editing_finished(self):
        if self.filter_op == 'Low Pass':
            t = self.ui.freq_lineEdit.text()
            t = t.replace(',', '.')
            
            self.lpf_freq = float(t)
            
            print('LPF Cut-Off = %f' % self.lpf_freq)
        
        elif self.filter_op == 'High Pass':
            t = self.ui.freq_lineEdit.text()
            t = t.replace(',', '.')
           
            self.hpf_freq = float(t)
           
            print('HPF Cut-Off = %f' % self.hpf_freq)

    def _load_layout(self):
        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.plt_filter = self.ui.plotWidget.addPlot(row=0, col=0)
        self.plt_fft = self.ui.plotWidget.addPlot(row=1, col=0)
        
        self.curve_filter = self.plt_filter.plot()
        self.curve_fft = self.plt_fft.plot()
    
    def _connect_slots(self):
        self.ui.filter_comboBox.currentTextChanged.connect(self._on_text_changed)
        self.filter_op = ''

        self.ui.freq_lineEdit.editingFinished.connect(self._on_editing_finished)
        validator = Qt.QDoubleValidator(bottom=0.0)
        self.ui.freq_lineEdit.setValidator(validator)
