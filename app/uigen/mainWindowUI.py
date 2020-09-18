# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './designer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 626)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotGroupWidget = QtWidgets.QWidget(self.groupBox)
        self.plotGroupWidget.setObjectName("plotGroupWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.plotGroupWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.filterHLayout = QtWidgets.QHBoxLayout()
        self.filterHLayout.setObjectName("filterHLayout")
        self.cutoffLowLabel = QtWidgets.QLabel(self.plotGroupWidget)
        self.cutoffLowLabel.setObjectName("cutoffLowLabel")
        self.filterHLayout.addWidget(self.cutoffLowLabel)
        self.cutoffLowSpinBox = QtWidgets.QDoubleSpinBox(self.plotGroupWidget)
        self.cutoffLowSpinBox.setMaximum(99999.99)
        self.cutoffLowSpinBox.setObjectName("cutoffLowSpinBox")
        self.filterHLayout.addWidget(self.cutoffLowSpinBox)
        self.cutoffHighLabel = QtWidgets.QLabel(self.plotGroupWidget)
        self.cutoffHighLabel.setObjectName("cutoffHighLabel")
        self.filterHLayout.addWidget(self.cutoffHighLabel)
        self.cutoffHighSpinBox = QtWidgets.QDoubleSpinBox(self.plotGroupWidget)
        self.cutoffHighSpinBox.setEnabled(True)
        self.cutoffHighSpinBox.setMaximum(99999.99)
        self.cutoffHighSpinBox.setObjectName("cutoffHighSpinBox")
        self.filterHLayout.addWidget(self.cutoffHighSpinBox)
        self.filterCheckBox = QtWidgets.QCheckBox(self.plotGroupWidget)
        self.filterCheckBox.setObjectName("filterCheckBox")
        self.filterHLayout.addWidget(self.filterCheckBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.filterHLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.filterHLayout)
        self.plotWidget = GraphicsLayoutWidget(self.plotGroupWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout_2.addWidget(self.plotWidget)
        self.verticalLayout.addWidget(self.plotGroupWidget)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "PLOT"))
        self.cutoffLowLabel.setText(_translate("MainWindow", "Low Cut-Off"))
        self.cutoffHighLabel.setText(_translate("MainWindow", "High Cut-Off"))
        self.filterCheckBox.setText(_translate("MainWindow", "FILTER"))
from pyqtgraph import GraphicsLayoutWidget
