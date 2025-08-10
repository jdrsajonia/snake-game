from objects import snakeObject, boardObject
from time import sleep
from pynput import keyboard

last_key="d"

DIMENSION=(11,30)

def on_press(key):
    global last_key
    try: 
        new_key=key.char.lower()
        if new_key in ("w","a","s","d"):
            last_key=new_key
        
    except AttributeError:
        pass

listener=keyboard.Listener(on_press=on_press)
listener.start()


# ver si se pueden dejar los controles como un objeto y pasarselo a la serpiente por el constructor o por un metodo builder
def controller():
    print("\033[H\033[J", end="")
    snake=snakeObject(DIMENSION)
    print(snake.keys)
    # snake.set_controls("t","f","g","h")

    print(snake.keys)
    board=boardObject(DIMENSION)
    board.put_apple(2)

    while True: #probar si se pueden añadir mas serpientes y tableros
        
        ##### tmp
        # current_coordenate=snake.adjust_direction2(last_key)
        # snake.set_current_direction(current_coordenate) # se actualiza la actual direccion de la serpiente

        ##### tmp

        should_grown=board.detect_apple(snake,last_key)
        snake.move_to(last_key, should_grown) #esto define el ritmo del juego
        print(board.str_current_game(snake))
        
        if snake.colition:
            print("\033[H\033[J", end="")
            snake.serpent_character=snake.colorize("x","b_red")
            print(board.str_current_game(snake))
            break

        sleep(0.1)
        print("\033[H\033[J", end="")  



controller()