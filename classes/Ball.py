import numpy as np
import random
from utils.playSound import play_sound


class Ball:

	def __init__(self, x_position, y_position, x_velocity, y_velocity, stick_to_paddle=True, clone_id=None):
		self.__position = np.array([x_position, y_position])
		self.__velocity = np.array([x_velocity, y_velocity])
		self.__is_attached = stick_to_paddle
		self.__is_destroyed = False
		self.__char = "█"
		self.__grabbed = False
		self.__clone_id = clone_id

	def get_string(self):
		return self.__char

	def get_position(self):
		return self.__position

	def get_velocity(self):
		return self.__velocity

	def is_cloned(self):
		return True if self.__clone_id else False

	def is_destroyed(self):
		return self.__is_destroyed

	def set_position(self, x, y):
		self.__position[0] = x
		self.__position[1] = y

	def set_velocity(self, v_x, v_y):
		self.__velocity[0] = v_x
		self.__velocity[1] = v_y

	def is_attached(self):
		return self.__is_attached

	def move_with_paddle(self, paddle):
		paddle_position = paddle.get_position()
		self.set_position(paddle_position[0], paddle_position[1] - 1)

	def release_from_paddle(self, grab=False):
		self.__is_attached = False
		if not self.__grabbed:
			new_velocity = np.random.rand(2) + np.array([0, -2])
			x_velocity_is_positive = bool(random.getrandbits(1))
			if x_velocity_is_positive:
				new_velocity += np.array([1, 0])
			else:
				new_velocity += np.array([-2, 0])
			self.set_velocity(new_velocity[0], new_velocity[1])
		self.__grabbed = False

	def move(self, game):
		if not self.__grabbed:
			original_velocity = self.__velocity.copy()
			power_ups = game.get_power_ups()
			thru_ball_power = False
			paddle_grab_power = False
			for power_up in power_ups:
				if power_up.get_type() == "thru" and power_up.is_activated():
					thru_ball_power = True
				elif power_up.get_type() == "grab" and power_up.is_activated():
					paddle_grab_power = True

			new_position = self.get_position() + self.get_velocity()

			# Handle collision with paddle
			paddle = game.get_paddle()
			bricks = game.get_bricks()
			current_position = self.__position
			if (
					(current_position[1] - paddle.get_position()[1]) * (new_position[1] - paddle.get_position()[1]) <= 0
					and
					(
							int(abs(current_position[0] - paddle.get_position()[0])) <= int((paddle.get_width() - 1) / 2)
							or
							int(abs(new_position[0] - paddle.get_position()[0])) <= int((paddle.get_width() - 1) / 2)
					)
			):
				if paddle_grab_power:
					self.__grabbed = True
					self.__is_attached = True
					self.move_with_paddle(paddle)
				self.set_velocity(self.__velocity[0] + self.__position[0] - paddle.get_position()[0], -self.__velocity[1])
				play_sound("sounds/collision.mp3")

			# Handle collisions with walls
			elif new_position[0] >= game.get_dimensions()[0] or new_position[0] <= 0:
				self.set_velocity(-self.__velocity[0], self.__velocity[1])
				play_sound("sounds/collision.mp3")
			elif new_position[1] <= 5:
				self.set_velocity(self.__velocity[0], -self.__velocity[1])
				play_sound("sounds/collision.mp3")
			elif new_position[1] > game.get_dimensions()[1] - 2:
				self.__is_destroyed = True

			# Handle collision with bricks
			for brick_number in range(len(bricks)):
				brick = None
				if self.__velocity[1] > 0:
					brick = bricks[brick_number]
				elif self.__velocity[1] < 0:
					brick = bricks[len(bricks) - brick_number - 1]
				brick_position = brick.get_position()
				brick_string, brick_color = brick.get_string()
				# From top
				if (
						(current_position[1] - brick_position[1]) * (new_position[1] - brick_position[1]) <= 0
						and
						(
								int(abs(current_position[0] - brick_position[0])) <= int((len(brick_string) - 1) / 2)
								or
								int(abs(new_position[0] - brick_position[0])) <= int((len(brick_string) - 1) / 2)
						)
				):
					if (
						int(self.__position[0]) in [int(brick_position[0]) - 3, int(brick_position[0]) + 3]
						and
						int(self.__position[1]) == int(brick_position[1])
					):
						if not thru_ball_power:
							self.set_velocity(-self.__velocity[0], self.__velocity[1])
							play_sound("sounds/collision.mp3")
					else:
						if not thru_ball_power:
							self.set_velocity(self.__velocity[0], -self.__velocity[1])
							play_sound("sounds/collision.mp3")
					if thru_ball_power:
						brick_strength = brick.get_strength()
						for i in range(brick_strength):
							brick.decrease_life(game, original_velocity)
					else:
						brick.decrease_life(game, original_velocity)
					break
			if game.get_level() == 3:
				ufo_bricks, boss = game.get_ufo_bricks()
				boss_position = boss.get_position()
				for brick_number in range(len(ufo_bricks)):
					brick = None
					if self.__velocity[1] > 0:
						brick = ufo_bricks[brick_number]
					elif self.__velocity[1] < 0:
						brick = ufo_bricks[len(ufo_bricks) - brick_number - 1]
					brick_position = brick.get_position() + boss_position
					brick_string, brick_color = brick.get_string(boss)
					# From top
					if (
						(current_position[1] - brick_position[1]) * (new_position[1] - brick_position[1]) <= 0
						and
						(
							int(abs(current_position[0] - brick_position[0])) <= int((len(brick_string) - 1) / 2)
							or
							int(abs(new_position[0] - brick_position[0])) <= int((len(brick_string) - 1) / 2)
						)
					):
						if (
							int(self.__position[0]) in [int(brick_position[0]) - 3, int(brick_position[0]) + 3]
							and
							int(self.__position[1]) == int(brick_position[1])
						):
							if not thru_ball_power:
								self.set_velocity(-self.__velocity[0], self.__velocity[1])
								play_sound("sounds/collision.mp3")
						else:
							if not thru_ball_power:
								self.set_velocity(self.__velocity[0], -self.__velocity[1])
								play_sound("sounds/collision.mp3")
						boss.decrease_health()
						break

			new_position = self.get_position() + self.get_velocity()
			self.set_position(new_position[0], new_position[1])

	def destroy(self):
		self.__is_destroyed = True

	def get_clone_id(self):
		if not self.__grabbed:
			return None
		return self.__clone_id
