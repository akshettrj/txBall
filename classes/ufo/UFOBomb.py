import numpy as np
from colorama import Back, Fore


class UFOBomb:

	def __init__(self, position):
		self._position = position
		self._is_wasted = False
		self._is_used = False
		self._velocity = np.array([0, 1])

	def get_string(self):
		return "§", Fore.YELLOW

	def wasted(self):
		return self._is_wasted

	def used(self):
		return self._is_used

	def waste(self):
		self._is_wasted = True

	def use(self):
		self._is_used = True

	def get_position(self):
		return np.copy(self._position)

	def move(self, game):
		new_position = self._position + self._velocity
		paddle = game.get_paddle()
		paddle_position = paddle.get_position()
		if self._position[1] <= paddle_position[1] <= new_position[1] \
			and \
			abs(self._position[0] - paddle_position[0]) <= int(paddle.get_width()/2):
			game.decrease_lives()
			self.use()
		elif new_position[1] > game.get_dimensions()[1]:
			self._is_wasted = True
		self._position = new_position
