import numpy

class Element:
	def __init__(self, name, parameters: dict, initalConcentration):
		self.name = name
		self.parameters = parameters
		self.concentration = initalConcentration

class Reservoir:
	def __init__(self, name, elements: list):
		self.name = name
		self.elements = elements

	def getElement(slef, name):
		for e in self.elements:
			if e.name == name:
				return e
		return null

class Flux:
	def __init__(self, name, source: Reservoir, sink: Reservoir, fluxFunction):
		self.name = name
		self.source = source
		self.sink = sink
		self.function = fluxFunction

class ReservoirModel():
	def __init__(self, time, reservoirs, fluxes):
		self.time = time
		self.reservoirs = reservoirs
		self.fluxes = fluxes
		self.adjMatrix = self.generateAdjMatrix()
		# self.ODESystem = self.assembleODESystem()

	def generateAdjMatrix(self):
		nReservoirs = len(self.reservoirs)
		adjMatrix = numpy.zeros(shape=(nReservoirs,nReservoirs))
		for flux in self.fluxes:
			source = flux.source
			sink = flux.sink
			sourceReservoirIndex = self.findReservoirIndex(source)
			sinkReservoirIndex = self.findReservoirIndex(sink)
			adjMatrix[sourceReservoirIndex][sinkReservoirIndex] = 1
		return adjMatrix

	def findReservoirIndex(self, resKey):
		for index, reservoir in enumerate(self.reservoirs):
			if reservoir.name == resKey:
				return index
		return -1

	# def assembleODESystem(self):
	# 	for reservoir in reservoirs:

	def assembleOutfluxVector(self, reservoir):
		outfluxVector = numpy.zeros(shape=(len(self.reservoirs)))
		outfluxes = [flux for flux in self.fluxes if flux.source == reservoir]
		for outflux in outfluxes:
			resIndex = self.findReservoirIndex(outflux.sink)
			outfluxVector[resIndex] = 1
		return outfluxVector

	def assembleInfluxVector(self, reservoir):
		influxVector = numpy.zeros(shape=(len(self.reservoirs)))
		influxes = [flux for flux in self.fluxes if flux.sink == reservoir]
		for influx in influxes:
			resIndex = self.findReservoirIndex(influx.source)
			influxVector[resIndex] = 1
		return influxVector


