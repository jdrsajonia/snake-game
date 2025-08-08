from objects import snakeObject, boardObject
from os import system
from time import sleep
from pynput import keyboard

last_key="d"

DIMENSION=(11,20)

def detect_apple(board: boardObject, snake: snakeObject, direction: tuple):
    next_coordenates=snake._sum_vectors(snake.get_head_position(), snake.get_direction(direction))
    should_grown=next_coordenates in board.apples_coordenates
    if should_grown:
        x,y=next_coordenates
        board.matrix[x][y]=" "
        board.apples_coordenates.remove(next_coordenates)
        board.put_apple(2)
    return should_grown


def print_matrix_snake(board: boardObject,snake: snakeObject=None):

    ascci_string=""

    y=len(board.matrix)
    x=len(board.matrix[0])

    horizontal_character="="
    vertical_character="|"
    serpent_character="\033[95m■\033[0m"
    apple_character="▫"
    space_character=" "
    borders_character="+"
    horizontal_margin=borders_character+2*horizontal_character*(x)+borders_character
    
    ascci_string+=horizontal_margin+"\n"

    for i in range(y):
        ascci_string+=vertical_character
        for j in range(x):
            coordenate=(i,j)
            if coordenate in snake.body:
                ascci_string+=serpent_character+" "
            elif coordenate in board.apples_coordenates:
                ascci_string+=apple_character+" "
            else:
                ascci_string+=space_character+" "
        ascci_string+=vertical_character+"\n"

    ascci_string+=horizontal_margin+"\n"
    return ascci_string

    


def on_press(key):
    global last_key
    try: 
        new_key=key.char.lower()
        if new_key in ("w","a","s","d"):
            last_key=new_key
        print(f"key: {new_key}")
    except AttributeError:
        pass

listener=keyboard.Listener(on_press=on_press)
listener.start()



def controller():
    system("cls")
    snake=snakeObject(DIMENSION)
    board=boardObject(DIMENSION)
    board.put_apple(2)

    while True:
        should_grown=detect_apple(board,snake,last_key)
        snake.move_to(last_key, should_grown)
        print(print_matrix_snake(board, snake))

        sleep(0.3)
        system("cls")


controller()