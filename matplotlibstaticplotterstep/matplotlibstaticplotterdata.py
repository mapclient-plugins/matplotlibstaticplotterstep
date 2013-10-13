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

class Classification(object):

	def __init__(self, name, labelsDict, code):
		self.name = name
		self.labels = labelsDict
		self.code = code

class MatplotlibStaticPlotterData(object):

	def __init__(self, name):
		self.name = name
		self.classfications = {}
		self.dataHeaders = None
		self.dataUnits = None
		self.dataArray = None

	def addClassification(classification):
		self.classfications[classification.name] = classification

	def addData(self, headers, units, dataArray):
		self.dataHeaders = headers
		self.dataUnits = units
		self.dataArray = dataArray

	def getClasses(self):
		return self.classfications.keys()

	def getLabelsForClass(self, classifcationName):
		return self.classfications[classificationName].labels

	def getHeaders(self):
		return self.dataHeaders

	def getUnits(self):
		return self.dataUnits

	def getUnitsForHeader(self, header):
		return self.dataUnits[self.dataHeaders.index(header)]

	def getData(self, header, classificationName=None, classLabel=None):
		data = self.dataArray[self.dataHeaders.index[header]]
		if classificationName!=None:
			C = self.classfications[classificationName]
			data = data[C.code==C.labels[classLabel]]

		return data