"""module to take input"""
import signal
from utils.alarmexception import *


class _getChUnix:
	"""class to take input"""

	def __call__(self):
		"""def to call function"""
		import sys
		import tty
		import termios
		fedvar = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fedvar)
		try:
			tty.setraw(sys.stdin.fileno())
			charvar = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
		print("\033[%d;%dH" % (0, 0))
		return charvar


def alarmhandler(signum, frame):
	""" input method """
	raise AlarmException


def user_input(timeout=0.15):
	""" input method """
	signal.signal(signal.SIGALRM, alarmhandler)
	signal.setitimer(signal.ITIMER_REAL, timeout)

	try:
		text = _getChUnix()()
		signal.alarm(0)
		return text
	except AlarmException:
		pass
	signal.signal(signal.SIGALRM, signal.SIG_IGN)
	return '.'