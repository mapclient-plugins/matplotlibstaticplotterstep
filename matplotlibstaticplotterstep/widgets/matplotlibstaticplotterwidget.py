'''
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland
    
This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
'''
import os

from PySide.QtGui import QDialog, QFileDialog, QDialogButtonBox, QAbstractItemView, QTableWidgetItem
from PySide.QtCore import Qt

from matplotlibstaticplotterstep.widgets.ui_matplotlibstaticplotterwidget import Ui_Dialog
from matplotlibstaticplotterstep.matplotlibstaticplotterdata import StepState

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''

class MatplotlibStaticPlotterWidget(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''
    plotTypes = ('scatterplot', 'historgram', 'boxplot')

    def __init__(self, state, plotData, parent=None):
        '''
        Constructor
        '''
        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        
        self.plotData = None

        self.setState(state)
        self.setPlotData(plotData)
        self.populateMenus()
        self._makeConnections()
        
    def _makeConnections(self):
        self._ui.plotButton.clicked.connect(self.plot)
 
    def setPlotData(self, plotData):
        self.plotData = plotData

    def populateMenus():

        # set plot types
        for t in self.plotTypes:
            self._ui.plotTypeComboBox.addItem(t)
        self._ui.plotTypeComboBox.isEditable(False)

        # set data combo boxes
        for h in self.plotData.dataHeaders:
            self._ui.data1ComboBox.addItem(h)
            self._ui.data2ComboBox.addItem(h)
        self._ui.data1ComboBox.isEditable(False)
        self._ui.data2ComboBox.isEditable(False)

        # set classification combo box
        for c in self.plotData.classification.keys():
            self._ui.classComboBox.addItem(c)
        self._ui.classComboBox.isEditable(False)

    def plot(self):

        # determine plot type
        plotType = self._ui.plotTypeComboBox.currentText().text()

        if plotType == 'scatterplot':
            self._plotScatter()
        elif plotType == 'historgram':
            self._plotHistogram()
        elif plotType = 'boxplot':
            self._plotBoxplot()


        #

    def _plotScatter(self):
        # get data to plot
        data1 = self._ui.data1ComboBox.currentText.text()
        data2 = self._ui.data2ComboBox.currentText.text()

    def _plotHistogram(self):
        # get data to plot
        data = self._ui.data1ComboBox.currentText.text()
        
   def _plotBoxplot(self):
        # get data to plot
        data1 = self._ui.data1ComboBox.currentText.text()
        data2 = self._ui.data2ComboBox.currentText.text()
         

    def setState(self, state):
        self.state = state
        self._ui.identifierLineEdit.setText(self.state._identifier)
    
    def getState(self):
        state = StepState()
        state._identifier = self._ui.identifierLineEdit.text()   
        return state


