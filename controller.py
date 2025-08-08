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
        # board.matrix[x][y]=" "
        board.apples_coordenates.remove(next_coordenates)
        board.put_apple(2)
    return should_grown


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
    # system("cls")
    print("\033[H\033[J", end="")
    snake=snakeObject(DIMENSION)
    board=boardObject(DIMENSION)
    board.put_apple(2)

    while True:
        should_grown=detect_apple(board,snake,last_key)
        snake.move_to(last_key, should_grown)
        print(f"Longitud: {snake.long}")
        print(board.current_game(snake))

        sleep(0.3)
        # system("cls")
        print("\033[H\033[J", end="")  



controller()