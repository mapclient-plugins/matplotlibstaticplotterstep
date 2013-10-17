# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlibstaticplotterwidget.ui'
#
# Created: Thu Oct 17 14:13:17 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(875, 496)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtGui.QGroupBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.classLabel = QtGui.QLabel(self.groupBox)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 3, 0, 1, 1)
        self.plotTypeComboBox = QtGui.QComboBox(self.groupBox)
        self.plotTypeComboBox.setObjectName("plotTypeComboBox")
        self.gridLayout.addWidget(self.plotTypeComboBox, 0, 1, 1, 1)
        self.data2Label = QtGui.QLabel(self.groupBox)
        self.data2Label.setObjectName("data2Label")
        self.gridLayout.addWidget(self.data2Label, 2, 0, 1, 1)
        self.classComboBox = QtGui.QComboBox(self.groupBox)
        self.classComboBox.setObjectName("classComboBox")
        self.gridLayout.addWidget(self.classComboBox, 3, 1, 1, 1)
        self.plotButton = QtGui.QPushButton(self.groupBox)
        self.plotButton.setObjectName("plotButton")
        self.gridLayout.addWidget(self.plotButton, 5, 1, 1, 1)
        self.plotTypeLabel = QtGui.QLabel(self.groupBox)
        self.plotTypeLabel.setObjectName("plotTypeLabel")
        self.gridLayout.addWidget(self.plotTypeLabel, 0, 0, 1, 1)
        self.data1Label = QtGui.QLabel(self.groupBox)
        self.data1Label.setObjectName("data1Label")
        self.gridLayout.addWidget(self.data1Label, 1, 0, 1, 1)
        self.data1ComboBox = QtGui.QComboBox(self.groupBox)
        self.data1ComboBox.setObjectName("data1ComboBox")
        self.gridLayout.addWidget(self.data1ComboBox, 1, 1, 1, 1)
        self.spaceLabel = QtGui.QLabel(self.groupBox)
        self.spaceLabel.setText("")
        self.spaceLabel.setObjectName("spaceLabel")
        self.gridLayout.addWidget(self.spaceLabel, 4, 0, 1, 1)
        self.data2ComboBox = QtGui.QComboBox(self.groupBox)
        self.data2ComboBox.setObjectName("data2ComboBox")
        self.gridLayout.addWidget(self.data2ComboBox, 2, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(self.groupBox)
        self.closeButton.setObjectName("closeButton")
        self.gridLayout.addWidget(self.closeButton, 7, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.matplotlibPlotterWidget = matplotlibPlotterWidget(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.matplotlibPlotterWidget.sizePolicy().hasHeightForWidth())
        self.matplotlibPlotterWidget.setSizePolicy(sizePolicy)
        self.matplotlibPlotterWidget.setObjectName("matplotlibPlotterWidget")
        self.gridLayout_3.addWidget(self.matplotlibPlotterWidget, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.classLabel.setText(QtGui.QApplication.translate("Dialog", "Classification:", None, QtGui.QApplication.UnicodeUTF8))
        self.data2Label.setText(QtGui.QApplication.translate("Dialog", "Data 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.plotButton.setText(QtGui.QApplication.translate("Dialog", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTypeLabel.setText(QtGui.QApplication.translate("Dialog", "Plot Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.data1Label.setText(QtGui.QApplication.translate("Dialog", "Data 1:", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibplotterwidget import matplotlibPlotterWidget
