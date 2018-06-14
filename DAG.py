import numpy

class Reservoir:
	def __init__(self, name):
		self.name = name
class Flux:
	def __init__(self, name, source, sink, fluxFunction):
		self.name = name
		self.source = source
		self.sink = sink
		self.function = fluxFunction

class ReservoirModel():
	def __init__(self, reservoirs, fluxes):
		self.adjMatrix = self.generateAdjMatrix(reservoirs, fluxes)

	def generateAdjMatrix(self, reservoirs, fluxes):
		nReservoirs = len(reservoirs)
		adjMatrix = numpy.zeros(shape=(nReservoirs,nReservoirs))
		return adjMatrix
