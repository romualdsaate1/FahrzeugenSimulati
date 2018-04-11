
class Car(object):
	Vehicle = property()

	def __init__(self, i, v_ref, v, s_ref, dt, a, b, x, l, delta, length):
		# Initialisiere Car mit Startwerten.
		#
		# * i : temporaere Variable, die verhindert, dass die Autos gleiche
		# * Koordinaten haben
		#
		self.super(i, v_ref, v, s_ref, dt, a, b, x, l, delta, length)
		self.setColorOfCar(Color.blue)