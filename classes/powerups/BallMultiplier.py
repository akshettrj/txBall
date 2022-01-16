from classes.powerups.PowerUp import PowerUp
from classes.Ball import Ball
import time
import numpy as np


class BallMultiplier(PowerUp):

	def __init__(self, x_position, y_position, velocity=np.array([0,0])):
		super().__init__(x_position, y_position, velocity)

	def get_string(self):
		if self._is_activated:
			return "M ({})".format(int(self._power_up_time - (time.time() - self._activated_at)))
		else:
			return "M"

	def get_type(self):
		return "multiply"

	def activate(self, game):
		super().activate()
		balls = game.get_balls()
		new_balls = []
		for ball in balls:
			ball_position = ball.get_position()
			ball_velocity = ball.get_velocity()
			new_ball = Ball(
				ball_position[0],
				ball_position[1],
				ball_velocity[0],
				- ball_velocity[1],
				clone_id=id(self),
				stick_to_paddle=ball.is_attached()
			)
			new_ball.set_velocity(ball_velocity[0], - ball_velocity[1])
			new_balls.append(new_ball)
		for new_ball in new_balls:
			game.add_ball(new_ball)

	def deactivate(self, game):
		super().deactivate()
		balls = game.get_balls()
		for ball in balls:
			if ball.is_cloned() and ball.get_clone_id() == id(self) and len(balls) > 1:
				ball.destroy()
