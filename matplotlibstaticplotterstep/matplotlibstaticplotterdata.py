

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

	def addClassification(class):
		self.classfications[class.name] = class

	def addData(self, headers, units, dataArray):
		self.dataHeaders = headers
		self.dataUnits = units
		self.dataArray = dataArray
