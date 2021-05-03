from cellular_automaton.render import game
from time import sleep

game = game.Game((100, 100))
while 1:
    game.loop()
    sleep(1)
