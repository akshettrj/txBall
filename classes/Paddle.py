from colorama import Fore, Back
import numpy


class Paddle:
	def __init__(self, width, x_position, y_position):
		self.__width = width
		self.__position = numpy.array([x_position, y_position])
		self.__speed = 5

	def get_string(self):
		return "I" * self.__width

	def get_position(self):
		return self.__position

	def get_width(self):
		return self.__width

	def move_left(self):
		self.__position[0] = max(self.__position[0] - self.__speed, 1 + int((self.__width - 1)/2))

	def move_right(self, game):
		self.__position[0] = min(self.__position[0] + self.__speed, game.get_dimensions()[0] - int((self.__width - 1)/2))

	def increase_size(self):
		self.__width += 2

	def decrease_size(self):
		self.__width = max(self.__width - 2, 3)
