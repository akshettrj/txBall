from classes.powerups.PowerUp import PowerUp
from utils.playSound import play_sound
import numpy as np
import time


class ShrinkPaddle(PowerUp):

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		super().__init__(x_position, y_position, velocity)
		self.__sound = "sounds/shrink.mp3"

	def get_string(self):
		if self._is_activated:
			return "S ({})".format(int(self._power_up_time - (time.time() - self._activated_at)))
		else:
			return "S"

	def get_type(self):
		return "shrink"

	def activate(self, game):
		super().activate()
		paddle = game.get_paddle()
		paddle.decrease_size()
		play_sound(self.__sound)

	def deactivate(self, game):
		super().deactivate()
		paddle = game.get_paddle()
		paddle.increase_size()
