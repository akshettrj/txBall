import numpy as np
from classes.powerups.PowerUp import PowerUp
import time
import numpy as np


class FastBall(PowerUp):

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		super().__init__(x_position, y_position, velocity)

	def get_string(self):
		if self._is_activated:
			return "F ({})".format(int(self._power_up_time - (time.time() - self._activated_at)))
		else:
			return "F"

	def get_type(self):
		return "fast"

	def activate(self, game):
		super().activate()
		balls = game.get_balls()
		for ball in balls:
			ball_velocity = ball.get_velocity()
			ball_velocity_directions = np.array([(v / abs(v)) if v != 0 else 0 for v in ball_velocity])
			new_ball_velocity = ball_velocity + ball_velocity_directions
			ball.set_velocity(new_ball_velocity[0], new_ball_velocity[1])

	def deactivate(self, game):
		super().deactivate()
		balls = game.get_balls()
		for ball in balls:
			ball_velocity = ball.get_velocity()
			ball_velocity_directions = np.array([(v / abs(v)) if v != 0 else 0 for v in ball_velocity])
			new_ball_velocity = ball_velocity - ball_velocity_directions
			ball.set_velocity(new_ball_velocity[0], new_ball_velocity[1])
