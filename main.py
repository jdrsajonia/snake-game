from objects.menu import menuObject
from objects.snake_game import snakeGameObject
from objects.controller import KeyboardController

menu=menuObject()

def game():
    snakegame=snakeGameObject(controller=KeyboardController())
    snakegame.set_properties(menu.properties)
    snakegame.start()

menu.set_game(game)
menu.start()