from classes.bricks.Brick import Brick
from colorama import Fore, Back


class NormalBrick(Brick):
	def __init__(self, x_position, y_position):
		super().__init__(x_position, y_position)
		self._strength = 2

	def get_string(self):
		return "| 2 |".format(self._strength), self._colors[max(self._strength - 1, 0)]

	def get_position(self):
		return self._position

	def is_destroyed(self):
		return self._broken

	def decrease_life(self, game, ball_velocity):
		super().decrease_life(game, ball_velocity)

		if self._strength == 0:
			game.increase_score(20)

	@staticmethod
	def get_type():
		return "N"

