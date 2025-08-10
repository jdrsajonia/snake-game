from objects import snakeObject, spaceObject
from time import sleep
from pynput import keyboard


last_key="d"

DIMENSION=(15,40)

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
    space=spaceObject(DIMENSION)
    space.put_apple(2)

    while True: #probar si se pueden añadir mas serpientes y tableros
        
        should_grown=space.detect_apple(snake,last_key)
        snake.move_to(last_key, should_grown) #esto define el ritmo del juego
        print(space.render_str_game(snake))
        
        if snake.colition:
            print("\033[H\033[J", end="")
            snake.serpent_character=snake.colorize("x","b_red")
            print(space.render_str_game(snake))
            break

        sleep(0.1)
        print("\033[H\033[J", end="")  



controller()

















