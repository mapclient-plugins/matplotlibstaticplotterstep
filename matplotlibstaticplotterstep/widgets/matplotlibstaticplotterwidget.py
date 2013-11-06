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
import numpy as np

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''

class MatplotlibStaticPlotterWidget(QDialog):
    '''
    Configure dialog to present the user with the options to configure this step.
    '''
    plotTypes = ('scatterplot', 'histogram', 'boxplot')
    colours = ('b', 'r', 'g', 'c', 'm', 'y', 'k', 'w')

    def __init__(self, plotData, parent=None):
        '''
        Constructor
        '''

        QDialog.__init__(self, parent)
        self._ui = Ui_Dialog()
        self._ui.setupUi(self)
        
        self.plotData = None

        self.setPlotData(plotData)
        self.populateMenus()
        self._makeConnections()

        self.setModal(True)
        
    def _makeConnections(self):
        self._ui.plotButton.clicked.connect(self.plot)
        self._ui.plotTypeComboBox.activated.connect(self._plotTypeChanged)

    def setPlotData(self, plotData):
        self.plotData = plotData

    def populateMenus(self):

        # set plot types
        for t in self.plotTypes:
            self._ui.plotTypeComboBox.addItem(t)
        # self._ui.plotTypeComboBox.setEnabled(False)

        # set data combo boxes
        self._ui.data1ComboBox.addItem('None')
        self._ui.data2ComboBox.addItem('None')
        for h in self.plotData.dataHeaders:
            self._ui.data1ComboBox.addItem(h)
            self._ui.data2ComboBox.addItem(h)
        # self._ui.data1ComboBox.isEditable(False)
        # self._ui.data2ComboBox.isEditable(False)

        # set classification combo box
        self._ui.classComboBox.addItem('None')
        for c in self.plotData.classifications.keys():
            self._ui.classComboBox.addItem(c)
        # self._ui.classComboBox.isEditable(False)
 
    def _plotTypeChanged(self):
        # grey out data2 combo box if not a scatterplot
        plotType = self._ui.plotTypeComboBox.currentText()
        if plotType != 'scatterplot':
            self._ui.data2ComboBox.setEnabled(False)
        else:
            self._ui.data1ComboBox.setEnabled(True)
            self._ui.data2ComboBox.setEnabled(True)

    def plot(self):

        # determine plot type
        plotType = self._ui.plotTypeComboBox.currentText()
        # print plotType

        if plotType == 'scatterplot':
            self._plotScatter()
        elif plotType == 'histogram':
            self._plotHistogram()
        elif plotType =='boxplot':
            self._plotBoxplot()
        else:
            raise ValueError, 'invalid plot type'

    def _plotScatter(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText()
        data2Name = self._ui.data2ComboBox.currentText()
        if (data1Name=='None') or (data2Name=='None'):
            raise ValueError, 'Data1 and Data2 cannot be None'

        data = []
        # check if classifications
        classificationName = self._ui.classComboBox.currentText()
        if classificationName=='None':
            data1 = self.plotData.getData(data1Name)
            data2 = self.plotData.getData(data2Name)
            data.append((data1,data2,'all'))
        else:
            classLabels = self.plotData.getLabelsForClass(classificationName)
            for label in classLabels:
                data1 = self.plotData.getData(data1Name, classificationName, label)
                data2 = self.plotData.getData(data2Name, classificationName, label)
                data.append((data1, data2, label))
            
        canvas = self._ui.matplotlibPlotterWidget.canvas 
        canvas.ax.clear()
        canvas.ax.set_title('{0} versus {1}'.format(data1Name, data2Name))
        canvas.ax.set_xlabel('{0} ({1})'.format(data1Name, self.plotData.getUnitsForHeader(data1Name)))
        canvas.ax.set_ylabel('{0} ({1})'.format(data2Name, self.plotData.getUnitsForHeader(data2Name)))
        plots = []
        for i, (data1, data2, label) in enumerate(data):
            plots.append( canvas.ax.scatter(data1, data2, s=40, c=self.colours[i], picker=True) )
    
        # point picker
        # def onPickScatterPoint(event):
        #     ind = event.ind

        # canvas.mpl_connect('pick_event', onPickScatterPoint)
        
        
        if classificationName!='None':
            canvas.ax.legend(plots, classLabels, loc=0)
        canvas.draw()


    def _plotHistogram(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText()
        if data1Name=='None':
            raise ValueError, 'Data1 cannot be None'

        data = []
        # check if classifications
        classificationName = self._ui.classComboBox.currentText()
        if classificationName=='None':
            data1 = self.plotData.getData(data1Name)
            data.append((data1,'all'))
            classLabels = None
        else:
            classLabels = self.plotData.getLabelsForClass(classificationName)
            for label in classLabels:
                data1 = self.plotData.getData(data1Name, classificationName, label)
                data.append((data1, label))
            
        canvas = self._ui.matplotlibPlotterWidget.canvas 
        canvas.ax.clear()
        canvas.ax.set_title('{0} Distribution'.format(data1Name))
        canvas.ax.set_xlabel('{0} ({1})'.format(data1Name, self.plotData.getUnitsForHeader(data1Name)))
        canvas.ax.set_ylabel('Frequency')

        plots = []
        histData = [d[0] for d in data]
        plots.append(canvas.ax.hist(histData, label=classLabels))

        # plots = []
        # for i, (data1, label) in enumerate(data):
        #     plots.append( canvas.ax.hist(data1, color=self.colours[i]) )

        if classificationName!='None':
            # canvas.ax.legend(plots, classLabels, loc=0)
            canvas.ax.legend()
        canvas.draw()
        
    def _plotBoxplot(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText()
        if data1Name=='None':
            raise ValueError, 'Data1 cannot be None'

        data = []
        # check if classifications
        classificationName = self._ui.classComboBox.currentText()
        if classificationName=='None':
            data1 = self.plotData.getData(data1Name)
            data.append((data1,'all'))
        else:
            classLabels = self.plotData.getLabelsForClass(classificationName)
            for label in classLabels:
                data1 = self.plotData.getData(data1Name, classificationName, label)
                data.append((data1, label))
            
        canvas = self._ui.matplotlibPlotterWidget.canvas 
        canvas.ax.clear()
        canvas.ax.set_title('{0} Distribution'.format(data1Name))
        
        canvas.ax.set_ylabel('{0} ({1})'.format(data1Name, self.plotData.getUnitsForHeader(data1Name)))

        plots = []
        boxData = np.array([d[0] for d in data]).T
        plots.append(canvas.ax.boxplot(boxData))

        if classificationName!='None':
            canvas.ax.set_xlabel(classificationName)
            canvas.ax.set_xticklabels([d[1] for d in data])

        linewidth = 5.0
        for box in plots:
            for part in box.keys():
                for line in box[part]:
                    line.set_linewidth(linewidth)

        canvas.draw()

