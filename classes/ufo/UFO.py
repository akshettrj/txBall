import numpy as np


class UFO:

	def __init__(self, position):
		self.__health = 100
		self.__position = position
		self.__layers_used = [False, False]
		self.__shape = [
			(0, 0),
			(5, 0),
			(-5, 0)
		]

	def get_health(self):
		return self.__health

	def decrease_health(self):
		self.__health -= 2

	def get_layout(self):
		return self.__shape

	def get_position(self):
		return self.__position

	def add_protective_layer(self, game):
		if (50 < self.__health < 75) and not self.__layers_used[0]:
			game.add_boss_layer()
			self.__layers_used[0] = True
		elif (25 < self.__health < 50) and not self.__layers_used[1]:
			game.add_boss_layer()
			self.__layers_used[1] = True

	def move_with_paddle(self, game):
		paddle = game.get_paddle()
		self.__position = paddle.get_position() - np.array([0, 33])
		self.__position[0] = min(self.__position[0], game.get_dimensions()[0] - 6*2)
		self.__position[0] = max(self.__position[0], 12)
