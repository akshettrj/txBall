from classes.bricks.Brick import Brick
from colorama import Fore, Back


class UFOBrick(Brick):
	def __init__(self, x_position, y_position):
		super().__init__(x_position, y_position)
		self._strength = 3

	def get_string(self, ufo):
		if ufo.get_health() >= 75:
			back_color = Back.RED
		elif ufo.get_health() >= 50:
			back_color = Back.YELLOW
		elif ufo.get_health() >= 25:
			back_color = Back.GREEN
		else:
			back_color = Back.WHITE

		if ufo.get_health() >= 75:
			front_color = Fore.BLUE
		elif ufo.get_health() >= 50:
			front_color = Fore.BLUE
		elif ufo.get_health() >= 25:
			front_color = Fore.RED
		else:
			front_color = Fore.RED

		return "| U |".format(self._strength), [back_color, front_color]

	def get_position(self):
		return self._position

	def is_destroyed(self):
		return self._broken

	def decrease_life(self, game, ball_velocity):
		super().decrease_life(game, ball_velocity)

		if self._strength == 0:
			game.increase_score(30)

	def get_length(self):
		return len("| U |".format(self._strength))

	@staticmethod
	def get_type():
		return "B"

