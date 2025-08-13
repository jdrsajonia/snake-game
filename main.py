from main_menu import menuObject
from snake_game import snakeGameObject
from objects import KeyboardController

menu=menuObject()

def game():
    snakegame=snakeGameObject(controller=KeyboardController())
    snakegame.set_properties(menu.properties)
    snakegame.start()

menu.set_game(game)
menu.start()