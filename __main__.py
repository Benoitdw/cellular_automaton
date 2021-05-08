from cellular_automaton.src import game
from time import sleep
from utils import SPEED

game = game.Game((1000, 1000))


if game.is_new:
    game.start()
if not game.is_new:
    game.play()
