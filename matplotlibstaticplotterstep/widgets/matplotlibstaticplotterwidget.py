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
        self._ui.data1ComboBox.addItem('None')
        self._ui.data2ComboBox.addItem('NoneTa')
        for h in self.plotData.dataHeaders:
            self._ui.data1ComboBox.addItem(h)
            self._ui.data2ComboBox.addItem(h)
        self._ui.data1ComboBox.isEditable(False)
        self._ui.data2ComboBox.isEditable(False)

        # set classification combo box
        self._ui.classComboBox.addItem('None')
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
        else:
            raise ValueError, 'invalid plot type'

    def _plotScatter(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText.text()
        data2Name = self._ui.data2ComboBox.currentText.text()

        if (data1Name=='None') or (data2Name=='None'):
            raise ValueError, 'Data1 and Data2 cannot be None'

        data = []
        # check if classifications
        classificationName = self._ui.classComboBox.currentText.text()
        if classificationName=='None':
            data1 = self.plotData.getData(data1Name)
            data2 = self.plotData.getData(data2Name)
            data.append((data1,data2, 'all'))
        else:
            classLabels = self.plotData.getLabelsForClass(classifcationName)
            for label in classLabels:
                data1 = self.plotData.getData(data1Name, classifcationName, label)
                data2 = self.plotData.getData(data2Name, classifcationName, label)
                data.append((data1, data2, label))
            
        canvas = self._ui.matplotlibPlotterWidget.canvas 
        canvas.ax.clear()
        canvas.ax.set_title('{d1Name} versus {d2Name}'.format(data1Name, data2Name))
        canvas.ax.set_xlabel('{dName} ({dUnit})'.format(data1Name, self.plotData.getUnitsForHeader(data1Name)))
        canvas.ax.set_ylabel('{dName} ({dUnit})'.format(data2Name, self.plotData.getUnitsForHeader(data2Name)))
        plots = []
        for data1, data2 in data:
            plots.append( canvas.ax.scatter(data1, data2) )

        if classficationName!='None':
            canvas.fig.legend(plots, classLabels, loc=8)
        canvas.draw()


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


