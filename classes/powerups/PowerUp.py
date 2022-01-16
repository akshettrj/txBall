import time
import numpy as np


class PowerUp:

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		self._is_activated = False
		self._is_acquired = False
		self._activated_at = None
		self._power_up_time = 20
		self._position = np.array([x_position, y_position])
		self._type = ""
		self._velocity = velocity / np.linalg.norm(velocity)
		self._g = np.array([0, 0.1])
		self._is_wasted = False

	def is_wasted(self):
		return self._is_wasted

	def time_left(self):
		if not self._activated_at:
			return 1
		return self._power_up_time - time.time() + self._activated_at

	def is_acquired(self):
		return self._is_acquired

	def is_activated(self):
		return self._is_activated

	def activate(self):
		self._activated_at = time.time()
		self._is_activated = True

	def deactivate(self):
		self._is_activated = False

	def get_string(self):
		return ""

	def get_position(self):
		return self._position

	def set_position(self, position):
		self._position = position

	def increase_time(self, amount):
		self._power_up_time += amount

	def move(self, game):
		new_position = self._position + self._velocity
		self._velocity = self._velocity + self._g
		paddle = game.get_paddle()
		paddle_position = paddle.get_position()
		if self._position[1] <= paddle_position[1] <= new_position[1] \
			and \
			abs(self._position[0] - paddle_position[0]) <= int((paddle.get_width() - 1) / 2):
			self._is_acquired = True
			self._position = new_position
		elif new_position[1] <= 5:
			self._position[1] = 4
			self._velocity[1] *= -1
		elif new_position[1] > game.get_dimensions()[1]:
			self._is_wasted = True
			self._position = new_position
		elif new_position[0] >= game.get_dimensions()[0] or new_position[0] <= 0:
			self._velocity[0] *= -1
		else:
			self._position = new_position

	def get_type(self):
		return ""
