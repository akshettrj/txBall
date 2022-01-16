from classes.powerups.PowerUp import PowerUp
import numpy as np
import time


class ThruBall(PowerUp):

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		super().__init__(x_position, y_position, velocity)

	def get_string(self):
		if self._is_activated:
			return "T ({})".format(int(self._power_up_time - (time.time() - self._activated_at)))
		else:
			return "T"

	def get_type(self):
		return "thru"

	def activate(self, game):
		super().activate()

	def deactivate(self, game):
		super().deactivate()
