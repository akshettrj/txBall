import numpy
import random
from utils.playSound import play_sound
from colorama import Back, Fore
from classes.powerups.ExpandPaddle import ExpandPaddle
from classes.powerups.ShrinkPaddle import ShrinkPaddle
from classes.powerups.ThruBall import ThruBall
from classes.powerups.FastBall import FastBall
from classes.powerups.PaddleGrab import PaddleGrab
from classes.powerups.BallMultiplier import BallMultiplier
from classes.powerups.ShootingPaddle import ShootingPaddle


class Brick:
	def __init__(self, x_position, y_position, give_power=True):
		self._position = numpy.array([x_position, y_position])
		self._strength = 3
		self._down_velocity = 2
		self._broken = False
		self._colors = [(Back.WHITE, Fore.RED), (Back.GREEN, Fore.RED), (Back.YELLOW, Fore.BLUE)]
		self._give_power_up = give_power

	def get_position(self):
		return self._position

	def is_destroyed(self):
		return self._broken

	def get_strength(self):
		return self._strength

	def get_string(self):
		return "| {} |".format(self._strength), self._colors[max(self._strength - 1, 0)]

	def decrease_life(self, game, ball_velocity):
		self._strength = self._strength - 1

		if self._strength == 0:
			self._broken = True
			play_sound("sounds/explosion.mp3")

			add_power_up_1 = bool(random.getrandbits(1))
			add_power_up_2 = bool(random.getrandbits(1))
			if add_power_up_1 or add_power_up_2 and self._give_power_up:
				power_up_types = [ExpandPaddle, ShrinkPaddle, ThruBall, FastBall, PaddleGrab, BallMultiplier, ShootingPaddle]
				power_up_type = random.choice(power_up_types)
				power_up = power_up_type(self._position[0], self._position[1], ball_velocity)
				game.add_power_up(power_up)

	def move_down(self):
		self._position = self._position + numpy.array([0, self._down_velocity])

	@staticmethod
	def get_type():
		return "A"

