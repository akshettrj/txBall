from classes.Paddle import Paddle
from classes.Layout import Layout
from classes.Ball import Ball
from classes.bricks.UnbreakableBrick import UnbreakableBrick
from classes.bricks.WeakBrick import WeakBrick
from classes.bricks.NormalBrick import NormalBrick
from classes.bricks.StrongBrick import StrongBrick
from classes.bricks.RainbowBrick import RainbowBrick
from classes.powerups.ExpandPaddle import ExpandPaddle
from classes.powerups.ShootingPaddle import ShootingPaddle
from classes.powerups.ShrinkPaddle import ShrinkPaddle
from classes.powerups.ThruBall import ThruBall
from classes.powerups.FastBall import FastBall
from classes.powerups.PaddleGrab import PaddleGrab
from classes.powerups.BallMultiplier import BallMultiplier
from classes.ufo.UFO import UFO
from classes.ufo.UFOBrick import UFOBrick
from classes.ufo.UFOBomb import UFOBomb
from math import floor
from utils.getch import user_input
import os
from utils.centerPrint import print_centered_text
from colorama import Fore, Back, Style
import time
import random
from utils.playSound import play_sound
import numpy as np
layout_manager = Layout()


class Game:
	def __init__(self):
		self.__start_time = None
		self.__boss_level = 3
		self.__boss_enemy = None
		self.__boss_bricks = []
		self.__lives = 5
		self.__score = 0
		self.__paddle = Paddle(11, 100, 43)
		self.__balls = []
		self.__bricks = []
		self.__ufo_bombs = []
		self.__level = 1
		self.__shoot_time = 0
		self.__power_ups = []
		self.__dimensions = [150, 45]
		self.__border_char = Fore.BLUE + "▓"
		self.__border_width = 2
		self.__frame = []
		self.__logo = [
			" ▄▄▄▄    ██▀███  ▓█████ ▄▄▄       ██ ▄█▀   ▄▄▄█████▓ ██░ ██ ▓█████  ███▄ ▄███▓    ▄▄▄       ██▓     ██▓    ",
			"▓█████▄ ▓██ ▒ ██▒▓█   ▀▒████▄     ██▄█▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▓██▒▀█▀ ██▒   ▒████▄    ▓██▒    ▓██▒    ",
			"▒██▒ ▄██▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓███▄░    ▒ ▓██░ ▒░▒██▀▀██░▒███   ▓██    ▓██░   ▒██  ▀█▄  ▒██░    ▒██░    ",
			"▒██░█▀  ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄    ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄ ▒██    ▒██    ░██▄▄▄▄██ ▒██░    ▒██░    ",
			"░▓█  ▀█▓░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒ █▄     ▒██▒ ░ ░▓█▒░██▓░▒████▒▒██▒   ░██▒    ▓█   ▓██▒░██████▒░██████▒",
			"░▒▓███▀▒░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░░ ▒░   ░  ░    ▒▒   ▓▒█░░ ▒░▓  ░░ ▒░▓  ░",
			"▒░▒   ░   ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░       ░     ▒ ░▒░ ░ ░ ░  ░░  ░      ░     ▒   ▒▒ ░░ ░ ▒  ░░ ░ ▒  ░",
			" ░    ░   ░░   ░    ░    ░   ▒   ░ ░░ ░      ░       ░  ░░ ░   ░   ░      ░        ░   ▒     ░ ░     ░ ░   ",
			" ░         ░        ░  ░     ░  ░░  ░                ░  ░  ░   ░  ░       ░            ░  ░    ░  ░    ░  ░",
			"      ░                                                                                                    ",
		]
		self.__bye = [
			" ▄▄▄▄ ▓██   ██▓▓█████     ▄▄▄▄ ▓██   ██▓▓█████ ",
			"▓█████▄▒██  ██▒▓█   ▀    ▓█████▄▒██  ██▒▓█   ▀ ",
			"▒██▒ ▄██▒██ ██░▒███      ▒██▒ ▄██▒██ ██░▒███   ",
			"▒██░█▀  ░ ▐██▓░▒▓█  ▄    ▒██░█▀  ░ ▐██▓░▒▓█  ▄ ",
			"░▓█  ▀█▓░ ██▒▓░░▒████▒   ░▓█  ▀█▓░ ██▒▓░░▒████▒",
			"░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░   ░▒▓███▀▒ ██▒▒▒ ░░ ▒░ ░",
			"▒░▒   ░▓██ ░▒░  ░ ░  ░   ▒░▒   ░▓██ ░▒░  ░ ░  ░",
			" ░    ░▒ ▒ ░░     ░       ░    ░▒ ▒ ░░     ░   ",
			" ░     ░ ░        ░  ░    ░     ░ ░        ░  ░",
			"      ░░ ░                     ░░ ░            "
		]

	def __initialize_bricks(self):
		self.__bricks = []
		if self.__level == self.__boss_level:
			self.reset_power_ups()
			self.reset_game_balls()
			self.__boss_enemy = UFO(self.__paddle.get_position() - np.array([0, 33]))
			boss_shape = self.__boss_enemy.get_layout()
			for brick in boss_shape:
				self.__boss_bricks.append(
					UFOBrick(brick[0], brick[1])
				)

		level_layout = layout_manager.get_layout(self.__level)

		for brick in level_layout:
			brick_position_x = brick["x"]
			brick_position_y = brick["y"]
			brick_type = brick["type"]

			if brick_type == "w":
				self.__bricks.append(WeakBrick(brick_position_x, brick_position_y))

			elif brick_type == "n":
				self.__bricks.append(NormalBrick(brick_position_x, brick_position_y))

			elif brick_type == "s":
				self.__bricks.append(StrongBrick(brick_position_x, brick_position_y))

			elif brick_type == "u":
				self.__bricks.append(UnbreakableBrick(brick_position_x, brick_position_y))

			elif brick_type == "r":
				self.__bricks.append(RainbowBrick(brick_position_x, brick_position_y))

	def start_game(self):
		"""
		This function will display the start screen of the game
		It will have the game logo, and options to start or
		quit the game.

		:return: None
		"""

		os.system("clear")
		os.system("stty -echo")
		print("\n" * 10)
		for logoLine in self.__logo:
			print_centered_text(logoLine, self.__dimensions[0], Fore.RED)
		print("\n"*3)
		print_centered_text('* PRESS "Q" KEY TO QUIT THE GAME', self.__dimensions[0], Fore.GREEN)
		print_centered_text('* PRESS "S" KEY TO START THE GAME', self.__dimensions[0], Fore.GREEN)
		while True:
			key = user_input()
			if key in ["q", "Q"]:
				self.quit_game()
			elif key in ["s", "S"]:
				return 0
			else:
				pass

	def play_game(self):

		self.__start_time = time.time()
		while self.__level <= self.__boss_level:

			level_start_time = time.time()
			level_ended = False

			# Initializing the ball
			self.reset_game_balls()
			self.reset_power_ups()
			self.__initialize_bricks()
			if self.__level == self.__boss_level:
				play_sound("sounds/boss.mp3")

			last_time_value = 0
			bomb_last_time = 0

			while not level_ended:

				current_time = time.time()
				level_time = current_time - level_start_time

				if level_time >= 50 and floor(level_time) % 5 == 0 and last_time_value != floor(level_time):
					last_time_value = floor(level_time)
					self.__make_bricks_fall()

				self.user_control()
				self.__remove_dead_balls()
				level_ended = self.__remove_dead_bricks()
				self.__manage_power_ups()
				self.__move_balls()
				self.__move_power_ups()

				self.__frame = []
				self.__add_frame_border()
				self.__add_frame_stats()
				self.__add_frame_paddle()
				self.__add_frame_bricks()
				self.__add_frame_power_ups()
				self.__add_shoots()

				if self.__level == self.__boss_level:
					self.__add_frame_ufo_bombs()
					self.__move_ufo_bombs()
					self.__remove_dead_bombs()
					self.__add_frame_boss_bricks()
					self.__move_ufo_bricks()
					level_ended = self.__check_ufo_health()
					if int(time.time() - level_start_time) % 5 == 0 and bomb_last_time != int(time.time() - level_start_time):
						self.__ufo_bombs.append(UFOBomb(self.__boss_enemy.get_position()))
						bomb_last_time = int(time.time() - level_start_time)

				self.__add_frame_balls()

				print("\033[%d;%dH" % (0, 0))

				for frame_line in range(len(self.__frame)):
					for i in range(len(self.__frame[frame_line])):
						print(self.__frame[frame_line][i], end="")
					print("")
			if self.__level == self.__boss_level:
				self.quit_game(force_quit=True)

		self.quit_game()

	def user_control(self):
		key_pressed = user_input(0.03)
		if key_pressed == ".":
			pass
		elif key_pressed == "q":
			self.quit_game(force_quit=True)
		elif key_pressed in ["a", "h"]:
			self.__paddle.move_left()
			for ball in self.__balls:
				if ball.is_attached():
					ball.move_with_paddle(self.__paddle)
		elif key_pressed in ["d", "l"]:
			self.__paddle.move_right(self)
			for ball in self.__balls:
				if ball.is_attached():
					ball.move_with_paddle(self.__paddle)
		elif key_pressed == " ":
			for ball in self.__balls:
				if ball.is_attached():
					ball.release_from_paddle()
		# Cheat Codes

		# Paddle Grab
		elif key_pressed == "g":
			power_up = PaddleGrab(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Multiply Ball
		elif key_pressed == "m":
			power_up = BallMultiplier(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Thru Ball
		elif key_pressed == "t":
			power_up = ThruBall(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Fast Speed
		elif key_pressed == "f":
			power_up = FastBall(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Shrink Paddle
		elif key_pressed == "c":
			power_up = ShrinkPaddle(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Expand Paddle
		elif key_pressed == "e":
			power_up = ExpandPaddle(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

		# Add Lives
		elif key_pressed == "L":
			self.__lives += 1

		elif key_pressed == "u":
			self.increase_level()

		# Rain Of Balls
		elif key_pressed == "b":
			power_up = ShootingPaddle(self.__paddle.get_position()[0], self.__paddle.get_position()[1] - 1)
			power_up.activate(self)
			self.__power_ups.append(power_up)

	def __move_balls(self):
		for ball in self.__balls:
			if not ball.is_attached():
				ball.move(self)

	def __check_ufo_health(self):
		ufo_health = self.__boss_enemy.get_health()
		self.__boss_enemy.add_protective_layer(self)
		if ufo_health < 0:
			return True

	def __move_power_ups(self):
		for power_up in self.__power_ups:
			if not power_up.is_activated() and not power_up.is_acquired():
				power_up.move(self)

	def __add_frame_border(self):
		for i in range(self.__border_width):
			frame_line = [self.__border_char for c in range(self.__dimensions[0] + 2 * self.__border_width)]
			self.__frame.append(frame_line)
		for i in range(self.__dimensions[1]):
			frame_line = \
				[self.__border_char for c in range(self.__border_width)] + \
				[" " for c in range(self.__dimensions[0])] + \
				[self.__border_char for c in range(self.__border_width)]
			self.__frame.append(frame_line)
		for i in range(self.__border_width):
			frame_line = [self.__border_char for c in range(self.__dimensions[0] + 2 * self.__border_width)]
			self.__frame.append(frame_line)

	def __add_shoots(self):
		for i in self.__power_ups:
			if i.get_type() == "shoot":
				if int(time.time() - self.__start_time) != self.__shoot_time and int(time.time() - self.__start_time) % 5 == 0:
					self.__shoot_time = int(time.time() - self.__start_time)
				new_ball_1 = Ball(
					self.__paddle.get_position()[0] - int((self.__paddle.get_width() - 1) / 2),
					self.__paddle.get_position()[1] - 2,
					0,
					1,
					False
				)
				self.__balls.append(new_ball_1)
				new_ball_2 = Ball(
					self.__paddle.get_position()[0] + int((self.__paddle.get_width() - 1) / 2),
					self.__paddle.get_position()[1] - 2,
					0,
					1,
					False
				)
				self.__balls.append(new_ball_2)

	def add_boss_layer(self):
		for i in range(10, self.__dimensions[0] - 10, 6):
			brick_already_there = False
			for brick in self.__bricks:
				if np.array_equal(brick.get_position(), np.array([i, 20])):
					brick_already_there = True
			if not brick_already_there:
				self.__bricks.append(WeakBrick(i, 20, give_power_up=False))

	def __add_frame_stats(self):
		for line_number in range(self.__border_width, self.__border_width + 5):
			for column_number in range(self.__border_width, self.__border_width + self.__dimensions[0]):
				self.__frame[line_number][column_number] = Back.RED + " "

		score_string = "Level: {}, Score: {}".format(self.__level, self.__score)
		for i in range(len(score_string)):
			self.__frame[self.__border_width + 1][self.__border_width + 1 + i] = Fore.YELLOW + Back.RED + score_string[i]

		time_string = "Time: {}s".format(floor(time.time() - self.__start_time) if self.__start_time else 0)
		for i in range(len(time_string)):
			self.__frame[self.__border_width + 2][self.__border_width + 1 + i] = Fore.YELLOW + Back.RED + time_string[i]

		lives_string = "Lives Left: {}, Power Ups: {}{}".format(
			"¤ " * self.__lives,
			[power_up.get_string() for power_up in self.__power_ups if power_up.is_activated()],
			", Boss Health: {}".format(self.__boss_enemy.get_health()) if (self.__level == self.__boss_level) else ""
		)
		for i in range(len(lives_string)):
			self.__frame[self.__border_width + 3][self.__border_width + 1 + i] = Fore.YELLOW + Back.RED + lives_string[i]

	def __make_bricks_fall(self):
		for brick in self.__bricks:
			brick.move_down()

	def __add_frame_paddle(self):
		paddle_string = self.__paddle.get_string()
		paddle_width = self.__paddle.get_width()
		paddle_position = [int(i) for i in self.__paddle.get_position()]
		paddle_color = Back.MAGENTA
		for power_up in self.__power_ups:
			if power_up.get_type() == "shoot":
				paddle_color = Back.RED
		for i in range(len(paddle_string)):
			self.__frame[
				self.__border_width - 1 + paddle_position[1]
			][
				self.__border_width - 1 + paddle_position[0] - int((paddle_width - 1)/2) + i
			] = paddle_color + paddle_string[i]

	def __add_frame_balls(self):
		thru_power_activated = False
		for power_up in self.__power_ups:
			if power_up.is_activated() and power_up.get_type() == "thru":
				thru_power_activated = True

		for ball in self.__balls:
			ball_position = [int(i) for i in ball.get_position()]
			self.__frame[
				self.__border_width - 1 + ball_position[1]
			][
				self.__border_width + ball_position[0] - 1
			] = (Fore.RED if thru_power_activated else Fore.GREEN) + ball.get_string()

	def __add_frame_bricks(self):
		for brick in self.__bricks:
			brick_string, brick_colors = brick.get_string()
			brick_width = int((len(brick_string) - 1) / 2)
			for i in range(-brick_width, brick_width + 1):
				self.__frame[
					brick.get_position()[1] + self.__border_width - 1
				][
					brick.get_position()[0] - 1 + self.__border_width + i
				] = brick_colors[0] + brick_colors[1] + Style.DIM + brick_string[i + brick_width]

	def __add_frame_power_ups(self):
		for power_up in self.__power_ups:
			if not power_up.is_activated() and not power_up.is_acquired():
				power_up_position = power_up.get_position()
				self.__frame[
					self.__border_width - 1 + int(power_up_position[1])
				][
					self.__border_width - 1 + int(power_up_position[0])
				] = power_up.get_string()

	def __add_frame_ufo_bombs(self):
		for bomb in self.__ufo_bombs:
			bomb_position = bomb.get_position()
			bomb_string, bomb_color = bomb.get_string()
			self.__frame[
				self.__border_width - 1 + int(bomb_position[1])
			][
				self.__border_width - 1 + int(bomb_position[0])
			] = bomb_color + bomb_string

	def __add_frame_boss_bricks(self):
		for brick in self.__boss_bricks:
			brick_position = brick.get_position() + self.__boss_enemy.get_position()
			brick_string, brick_colors = brick.get_string(self.__boss_enemy)
			brick_length = brick.get_length()
			brick_width = int((brick_length - 1)/2)
			for i in range(-brick_width, brick_width + 1):
				self.__frame[
					brick_position[1] + self.__border_width - 1
					][
					brick_position[0] - 1 + self.__border_width + i
					] = brick_colors[0] + brick_colors[1] + brick_string[i + brick_width]

	def __move_ufo_bombs(self):
		for bomb in self.__ufo_bombs:
			bomb.move(self)

	def reset_game_balls(self):
		ball_y_position = self.__paddle.get_position()[1] - 1
		paddle_side_length = int((self.__paddle.get_width() - 1)/2)
		ball_x_position = random.choice(
			list(
				range(
					self.__paddle.get_position()[0] - paddle_side_length,
					self.__paddle.get_position()[0] + paddle_side_length + 1
				)))
		starting_ball = Ball(ball_x_position, ball_y_position, 0, 0)
		self.__balls = [starting_ball]

	def reset_power_ups(self):
		for power_up in self.__power_ups:
			if power_up.is_activated():
				power_up.deactivate(self)
		self.__power_ups = []

	def get_ufo_bricks(self):
		return self.__boss_bricks, self.__boss_enemy

	def __remove_dead_balls(self):
		self.__balls = list(filter(lambda ball: not ball.is_destroyed(), self.__balls))
		if len(self.__balls) == 0:
			self.reset_power_ups()
			self.reset_game_balls()
			self.decrease_lives()

	def __remove_dead_bricks(self):
		self.__bricks = list(filter(lambda brick: not brick.is_destroyed(), self.__bricks))
		if len(self.__bricks) == 0:
			self.increase_level()
			return True

		return False

	def get_level(self):
		return self.__level

	def __move_ufo_bricks(self):
		self.__boss_enemy.move_with_paddle(self)

	def __manage_power_ups(self):
		def power_up_died(power_up):
			if power_up.is_wasted():
				return False
			elif power_up.is_activated() and power_up.time_left() <= 0:
				power_up.deactivate(self)
				return False
			return True

		self.__power_ups = list(filter(power_up_died, self.__power_ups))

		for power_up in self.__power_ups:
			if not power_up.is_activated() and power_up.is_acquired():
				power_up.activate(self)

	def increase_score(self, amount):
		self.__score += amount

	def increase_level(self):
		def power_up_filter(pu):
			if not pu.is_acquired():
				return True
			else:
				pu.deactivate(self)
		self.__level += 1
		self.__power_ups = list(filter(power_up_filter, self.__power_ups))
		self.__initialize_bricks()

	def get_dimensions(self):
		return self.__dimensions

	def get_paddle(self):
		return self.__paddle

	def get_balls(self):
		return self.__balls

	def get_bricks(self):
		return self.__bricks

	def get_power_ups(self):
		return self.__power_ups

	def decrease_lives(self):
		def power_up_filter(pu):
			if not pu.is_acquired():
				return True
			else:
				pu.deactivate(self)
		self.__lives = self.__lives - 1
		if self.__lives == 0:
			self.quit_game(force_quit=True)
		self.__power_ups = list(filter(power_up_filter, self.__power_ups))

	def add_power_up(self, power_up):
		self.__power_ups.append(power_up)

	def add_ball(self, ball):
		self.__balls.append(ball)

	def __remove_dead_bombs(self):
		self.__ufo_bombs = [bomb for bomb in self.__ufo_bombs if not bomb.wasted() and not bomb.used()]

	def quit_game(self, force_quit=False):
		if force_quit:
			os.system("clear")
			print("\n" * 10)
			for byeLine in self.__bye:
				print_centered_text(byeLine, self.__dimensions[0], Fore.RED)
			print("\n"*3)
			print_centered_text("Your final score: {}".format(self.__score), self.__dimensions[0], Fore.GREEN)
			print_centered_text("You took: {} seconds".format(floor(time.time() - self.__start_time)), self.__dimensions[0], Fore.GREEN)
			os.system("killall mpg123 >/dev/null 2>/dev/null")
		if self.__start_time:
			pass
		else:
			os.system("clear")
		print("\x1b[?25h")
		exit(0)

