from src.render import game
from time import sleep
from src.constantes import SPEED

game = game.Game((1000, 1000))
while 1:
    game.loop()
    sleep(SPEED)
