from cellular_automaton.src import game
from time import sleep
from utils import SPEED

game = game.Game((1000, 1000))
while 1:
    game.loop()
    sleep(SPEED)
