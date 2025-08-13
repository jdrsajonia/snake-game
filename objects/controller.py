from pynput import keyboard

class KeyboardController:
    def __init__(self):
        self.last_key="d"
        self.listener=None
        self.quit=False

    def on_press(self,key):
        try: 
            new_key=key.char.lower()
            if new_key in ("w","a","s","d"):
                self.last_key=new_key
            elif new_key=="q":
                self.quit=True

        except AttributeError:
            pass
    
    def start(self):
        self.listener=keyboard.Listener(on_press=self.on_press, suppress=True)
        self.listener.start()