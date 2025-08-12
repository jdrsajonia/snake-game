from objects import snakeObject, spaceObject
from time import sleep
from pynput import keyboard
from math import sqrt


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



class snakeGameObject:
    def __init__(self, controller : KeyboardController = None):
        self.properties={"dimension":(10,20), "speed":6}
        
        self.snake=snakeObject(self.properties["dimension"])
        self.spaceboard=spaceObject(self.properties["dimension"])
        self.controller=controller

        
    def set_properties(self,properties):
        self.properties=properties
        self.snake=snakeObject(self.properties["dimension"])
        self.spaceboard=spaceObject(self.properties["dimension"])
        


    def game_logic(self):
        clear="\033[H\033[J"
        
        print(clear, end="")

        speed_level=self.properties["speed"]
        snake1=self.snake
        space=self.spaceboard
        space.put_apple(2)
        
        while True:
            should_grown=space.detect_apple(snake1, self.controller.last_key)
            snake1.move_to(self.controller.last_key, should_grown)
            print(space.render_str_game(snake1))

            if snake1.colition or self.controller.quit:
                print(clear, end="")
                snake1.serpent_character = snake1.colorize("x", "b_red")
                print(space.render_str_game(snake1))
                break

            self.speed(speed_level)                     
            print(clear, end="")


    def start(self):
        self.controller.start()
        self.game_logic() 
        self.controller.listener.stop()
       
    
    def speed(self, x : list):
        if not x in range(1,11):
            return sleep(0.1)
        y=-x/17+0.65
        sleep(y)
        pass

    # 


if __name__=="__main__":
    
    # controller_input=KeyboardController()
    game=snakeGameObject()
    game.start()
    

