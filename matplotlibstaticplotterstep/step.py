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
import string
import random
from PySide import QtGui

from mountpoints.workflowstep import WorkflowStepMountPoint
from matplotlibstaticplotterstep.widgets.matplotlibstaticplotterwidget import MatplotlibStaticPlotterWidget

class MatplotlibStaticPlotterStep(WorkflowStepMountPoint):
    '''
    Skeleton step which is intended to be used as a starting point
    for new steps.
    '''
    
    def __init__(self, location):
        super(MatplotlibStaticPlotterStep, self).__init__('Static Data Plotter', location)
        self._state = StepState()
        self._icon = QtGui.QImage(':/autosegmentation/images/autoseg.png')
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port', 'http://physiomeproject.org/workflow/1.0/rdf-schema#uses', 'ju#tabledata'))
           
        # The widget will be the interface widget for the user to see the
        # autosegmentation step and interact with it.
        self._widget = None
        
        # This step only requires an identifier which we can generate from
        # a char set.  This make the configuration of the step trivial.
        self._identifier = generateIdentifier()
        self._configured = True
        
    def configure(self):
        return self._configured
    
    def getIdentifier(self):
        return self._identifier
     
    def setIdentifier(self, identifier):
        self._identifier = identifier
     
    def serialize(self, location):
        '''There is nothing to be done here for this step.
        '''
        pass
     
    def deserialize(self, location):
        '''There is nothing to be done here for this step.
        '''
        pass

    def execute(self, dataIn):
        if not self._widget:
            self._widget = MatplotlibStaticPlotterWidget(dataIn)
            self._widget._ui.closeButton.clicked.connect(self._doneExecution)
            self._widget.setModal(True)

        self._setCurrentWidget(self._widget)
     
class StepState(object):
    '''
    This class holds the step state, for use with serialization
    /deserialization.
    '''
    
    def __init__(self):
        pass
    
def generateIdentifier(char_set=string.ascii_uppercase + string.digits):
    return ''.join(random.sample(char_set*6,6))
