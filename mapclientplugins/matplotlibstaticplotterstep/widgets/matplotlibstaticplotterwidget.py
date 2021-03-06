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

from mapclientplugins.matplotlibstaticplotterstep.widgets.ui_matplotlibstaticplotterwidget import Ui_Dialog
import numpy as np

REQUIRED_STYLE_SHEET = 'border: 1px solid red; border-radius: 3px'
DEFAULT_STYLE_SHEET = ''
import pdb

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

        self._scatterPickLabel = None
        self._pickHandlerID = None
        
    def _makeConnections(self):
        self._ui.plotButton.clicked.connect(self.plot)
        self._ui.saveFigButton.clicked.connect(self._saveFig)
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
        for h in self.plotData.getHeaders():
            self._ui.data1ComboBox.addItem(h)
            self._ui.data2ComboBox.addItem(h)
        # self._ui.data1ComboBox.isEditable(False)
        # self._ui.data2ComboBox.isEditable(False)

        # set classification combo box
        self._ui.classComboBox.addItem('None')
        for c in list(self.plotData._classifications.keys()):
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
            raise ValueError('invalid plot type')

    def _plotScatter(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText()
        data2Name = self._ui.data2ComboBox.currentText()
        if (data1Name=='None') or (data2Name=='None'):
            raise ValueError('Data1 and Data2 cannot be None')

        data = []
        # check if classifications
        classificationName = self._ui.classComboBox.currentText()
        if classificationName=='None':
            data1 = self.plotData.getData(data1Name)
            data2 = self.plotData.getData(data2Name)
            dataLabels = self.plotData.getRowLabels()
            data.append((data1, data2, dataLabels, 'all'))
        else:
            classLabels = self.plotData.getLabelsForClass(classificationName)
            for label in classLabels:
                data1 = self.plotData.getData(data1Name, classificationName, label)
                data2 = self.plotData.getData(data2Name, classificationName, label)
                dataLabels = self.plotData.getRowLabels(classificationName, label)
                data.append((data1, data2, dataLabels, label))
            
        canvas = self._ui.matplotlibPlotterWidget.canvas 
        canvas.ax.clear()
        canvas.ax.set_title('{0} versus {1}'.format(data1Name, data2Name))
        canvas.ax.set_xlabel('{0} ({1})'.format(data1Name, self.plotData.getUnitsForHeader(data1Name)))
        canvas.ax.set_ylabel('{0} ({1})'.format(data2Name, self.plotData.getUnitsForHeader(data2Name)))
        plots = []
        self._scatterPickLabel = None
        for i, (data1, data2, dataLabels, label) in enumerate(data):
            picker = self._makePicker(data1, data2, dataLabels)
            plots.append( canvas.ax.scatter(data1, data2, s=40, c=self.colours[i], picker=picker) )
    
        if classificationName!='None':
            canvas.ax.legend(plots, classLabels, loc=0)

        canvas.draw()

    def _makePicker(self, data1, data2, labels):
        ax = self._ui.matplotlibPlotterWidget.canvas.ax
        maxDistX = (data1.max()-data1.min())*1e-2
        maxDistY = (data2.max()-data2.min())*1e-2
        print('maxDist', maxDistX, maxDistY)

        def _getLabel(x,y):
            distx = np.abs(x-data1)
            disty = np.abs(y-data2)
            matchInds = np.where( (distx<maxDistX) & (disty<maxDistY) )[0]
            if len(matchInds) > 0:
                return labels[matchInds[0]]
            else:
                return None
            # return labels[np.where(dists<maxDist)[0][0]]

        def _picker(artist, event):
            offset = 1.005
            x = event.xdata * offset
            y = event.ydata * offset
            label = _getLabel(event.xdata, event.ydata)
            
            if label:
                print('Pick event:', label, x, y)
                if self._scatterPickLabel==None:
                    self._scatterPickLabel = ax.text(x, y, label, bbox=dict(facecolor='red', alpha=0.5))
                else:
                    self._scatterPickLabel.set_x(x)
                    self._scatterPickLabel.set_y(y)
                    self._scatterPickLabel.set_text(label)

                self._ui.matplotlibPlotterWidget.canvas.draw()
            
            return None, None

        return _picker

    def _plotHistogram(self):
        # get data to plot
        data1Name = self._ui.data1ComboBox.currentText()
        if data1Name=='None':
            raise ValueError('Data1 cannot be None')

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
            raise ValueError('Data1 cannot be None')

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
            for part in list(box.keys()):
                for line in box[part]:
                    line.set_linewidth(linewidth)

        canvas.draw()


    def _saveFig(self):
        filename = self._ui.saveFigFilenameLineEdit.text()
        dpi = int(self._ui.saveFigDpiLineEdit.text())
        self._ui.matplotlibPlotterWidget.canvas.fig.savefig( filename, dpi=dpi, bbox_inches='tight' )