import colorama
from classes.Game import Game

colorama.init(autoreset=True)

# Hide the cursor
print("\x1b[?25l")

game = Game()

option_picked = game.start_game()

if option_picked == -1:
    game.quit_game()
else:
    # If the game has to be started
    game.play_game()
