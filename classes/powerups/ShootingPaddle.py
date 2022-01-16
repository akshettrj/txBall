import numpy as np
from classes.powerups.PowerUp import PowerUp
import time


class ShootingPaddle(PowerUp):

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		super().__init__(x_position, y_position, velocity)

	def get_string(self):
		if self._is_activated:
			return "H ({})".format(int(self._power_up_time - (time.time() - self._activated_at)))
		else:
			return "H"

	def get_type(self):
		return "shoot"

	def activate(self, game):
		super().activate()

	def deactivate(self, game):
		super().deactivate()
