from classes.bricks.Brick import Brick
from colorama import Fore, Back


class UnbreakableBrick(Brick):
	def __init__(self, x_position, y_position):
		super().__init__(x_position, y_position)
		self._strength = 1

	def get_string(self):
		return "| * |", (Back.RED, Fore.BLUE)

	def get_position(self):
		return self._position

	def is_destroyed(self):
		return self._broken

	def decrease_life(self, game, ball_velocity):
		power_ups = game.get_power_ups()
		thru_ball_activated = False
		for power_up in power_ups:
			if power_up.get_type() == "thru" and power_up.is_activated():
				thru_ball_activated = True

		if thru_ball_activated:
			self._strength = self._strength - 1
			if self._strength == 0:
				self._broken = True

	@staticmethod
	def get_type():
		return "U"

