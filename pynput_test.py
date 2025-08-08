from pynput import keyboard


keys={ 
        "w":(-1,0),     # arriba
        "a":(0,-1),     # izquierda
        "s":(1,0),      # abajo
        "d":(0,1)       # derecha
        }

def on_press(key):
    try:
        print(f"Key: {key.char}")
        # print(keys[key.char])
    except AttributeError:
        print(f"special key: {key.char}")

def on_release(key):
    print(f"Key released: {key.char}")
    if key==keyboard.Key.esc:
        return False
    
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

