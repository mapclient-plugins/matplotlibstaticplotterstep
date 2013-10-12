# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matplotlibstaticplotterwidget.ui'
#
# Created: Sat Oct 12 12:30:48 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(888, 496)
        self.matplotlibPlotterWidget = matplotlibPlotterWidget(Dialog)
        self.matplotlibPlotterWidget.setGeometry(QtCore.QRect(330, 10, 531, 471))
        self.matplotlibPlotterWidget.setObjectName("matplotlibPlotterWidget")
        self.gridLayoutWidget = QtGui.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.classLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 3, 0, 1, 1)
        self.plotTypeComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.plotTypeComboBox.setObjectName("plotTypeComboBox")
        self.plotTypeComboBox.addItem("")
        self.plotTypeComboBox.addItem("")
        self.plotTypeComboBox.addItem("")
        self.gridLayout.addWidget(self.plotTypeComboBox, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.data2Label = QtGui.QLabel(self.gridLayoutWidget)
        self.data2Label.setObjectName("data2Label")
        self.gridLayout.addWidget(self.data2Label, 2, 0, 1, 1)
        self.classComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.classComboBox.setObjectName("classComboBox")
        self.gridLayout.addWidget(self.classComboBox, 3, 1, 1, 1)
        self.plotButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.plotButton.setObjectName("plotButton")
        self.gridLayout.addWidget(self.plotButton, 5, 1, 1, 1)
        self.plotTypeLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.plotTypeLabel.setObjectName("plotTypeLabel")
        self.gridLayout.addWidget(self.plotTypeLabel, 0, 0, 1, 1)
        self.data1Label = QtGui.QLabel(self.gridLayoutWidget)
        self.data1Label.setObjectName("data1Label")
        self.gridLayout.addWidget(self.data1Label, 1, 0, 1, 1)
        self.data1ComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.data1ComboBox.setObjectName("data1ComboBox")
        self.gridLayout.addWidget(self.data1ComboBox, 1, 1, 1, 1)
        self.data2ComboBox = QtGui.QComboBox(self.gridLayoutWidget)
        self.data2ComboBox.setObjectName("data2ComboBox")
        self.gridLayout.addWidget(self.data2ComboBox, 2, 1, 1, 1)
        self.spaceLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.spaceLabel.setText("")
        self.spaceLabel.setObjectName("spaceLabel")
        self.gridLayout.addWidget(self.spaceLabel, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.classLabel.setText(QtGui.QApplication.translate("Dialog", "Classification:", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTypeComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Scatterplot", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTypeComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Histogram", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTypeComboBox.setItemText(2, QtGui.QApplication.translate("Dialog", "Boxplot", None, QtGui.QApplication.UnicodeUTF8))
        self.data2Label.setText(QtGui.QApplication.translate("Dialog", "Data 2:", None, QtGui.QApplication.UnicodeUTF8))
        self.plotButton.setText(QtGui.QApplication.translate("Dialog", "Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.plotTypeLabel.setText(QtGui.QApplication.translate("Dialog", "Plot Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.data1Label.setText(QtGui.QApplication.translate("Dialog", "Data 1:", None, QtGui.QApplication.UnicodeUTF8))

from matplotlibplotterwidget import matplotlibPlotterWidget
