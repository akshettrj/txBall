class Layout:

	def __init__(self):

		self.__layout_level2 = [{
				"x": 78,
				"y": 12,
				"type": "u"
			}, {
				"x": 72,
				"y": 12,
				"type": "u"
			}, {
				"x": 84,
				"y": 12,
				"type": "u"
			}, {
				"x": 66,
				"y": 12,
				"type": "s"
			}, {
				"x": 90,
				"y": 12,
				"type": "s"
			}, {
				"x": 54,
				"y": 12,
				"type": "n"
			}, {
				"x": 102,
				"y": 12,
				"type": "n"
			}, {
				"x": 48,
				"y": 12,
				"type": "n"
			}, {
				"x": 108,
				"y": 12,
				"type": "n"
			}, {
				"x": 78,
				"y": 10,
				"type": "w"
			}, {
				"x": 78,
				"y": 14,
				"type": "w"
			}, {
				"x": 78,
				"y": 8,
				"type": "w"
			}, {
				"x": 78,
				"y": 16,
				"type": "w"
			}, {
				"x": 84,
				"y": 10,
				"type": "w"
			}, {
				"x": 84,
				"y": 14,
				"type": "w"
			}, {
				"x": 72,
				"y": 10,
				"type": "w"
			}, {
				"x": 72,
				"y": 14,
				"type": "w"
			}, {
				"x": 48,
				"y": 14,
				"type": "r"
			}, {
				"x": 48,
				"y": 10,
				"type": "r"
			}, {
				"x": 108,
				"y": 10,
				"type": "r"
			}, {
				"x": 108,
				"y": 14,
				"type": "r"
			}
		]
		self.__layout_level1 = [
			{
				"x": 78,
				"y": 10,
				"type": "s"
			}, {
				"x": 78,
				"y": 12,
				"type": "s"
			}, {
				"x": 78,
				"y": 8,
				"type": "s"
			}
		]

		self.__layout_level3 = [
			{
				"x": 45,
				"y": 15,
				"type": "u"
			}
		]

		# Each of the layout list above has its children as details about on brick
		# It will be a dictionary of the following type
		# brick = {
		#   "x" -> X position of the brick (Integer),
		#   "y" -> Y position of the brick (Integer),
		#   "type" -> It can take the following values:
		#       1. "w" for Weak Brick
		#       2. "n" for Normal Brick
		#       3. "s" for Strong Brick
		#       4. "u" for Unbreakable Brick
		# }

	def get_layout(self, level):

		if level == 1:
			return self.__layout_level1

		elif level == 2:
			return self.__layout_level2

		elif level == 3:
			return self.__layout_level3
