from .utils import colors
from collections import deque
from random import randint


class snakeObject:
    def __init__(self, warp_dimensions: tuple):
        self.long=1
        self.body=deque()
        self.head_position=(0,0)
        self.body.append(self.head_position)
        self.serpent_character=colors().colorize("■","magenta")
        self.warp_x, self.warp_y = warp_dimensions

        self.up, self.left, self.down, self.right = ("w", "a", "s", "d")
        self.keys={ 
                    self.up:(-1,0),     
                    self.left:(0,-1),   
                    self.down:(1,0),      
                    self.right:(0,1),  
                    }
        
        self.last_key="d"

        self.current_direction=(0,1)
        self.collision=False
        
    
    @staticmethod
    def _sum_vectors(vector1:tuple, vector2:tuple):
        new_vector = tuple((v1+v2) for v1, v2 in zip(vector1, vector2)) 
        return new_vector


    #NOTA: intentar que la dirección actualizada sea un atributo de la serpiente para que board no requiera este metodo prestado, sino el atributo ya actualizado de la serpiente
    def adjust_direction(self, key:str):
        new_direction=self.keys[key]  #!! controlador en la serpiente
        if new_direction[0]==-self.current_direction[0] and new_direction[1]==-self.current_direction[1]:
            return self.current_direction
        self.current_direction=new_direction 
        return new_direction

   
    def get_head_position(self):
        return self.head_position
    

    def set_head_position(self, coordinates: tuple):
        self.head_position=coordinates
    

    def _normalize_position(self,coordinate: tuple):
        current_x,current_y=coordinate
        current_x=current_x%self.warp_x
        current_y=current_y%self.warp_y
        return current_x, current_y
    

    def detect_collision(self, new_coordinate):
        if new_coordinate in self.body:
            self.collision=True
            


    def next_coordinate(self,direction_key):
        actual_position=self.get_head_position()
        current_direction=self.adjust_direction(direction_key) 
        new_position=self._sum_vectors(actual_position,current_direction)
        new_position=self._normalize_position(new_position)
        return new_position

    def move_to(self, direction_key:str, grow_up=False): 
        new_position=self.next_coordinate(direction_key)
        self.detect_collision(new_position)
        if not grow_up:
            self.body.pop()     # crece = no elimina su cola al moverse
        else:
            self.long+=1 

        self.set_head_position(new_position)
        self.body.appendleft(new_position)


    def change_serpent_char(self,character, color):
        self.serpent_character=colors().colorize(character,color)
        
        
    

class spaceObject:
    def __init__(self,dimension):
        self.x, self.y = dimension
        self.apples_coordinates=set()
        self.is_colorized=True
        self.char={
            "h_line"            : colors().colorize("═","white"),
            "v_line"            : colors().colorize("║","white"),
            "apple"             : colors().colorize("▪","green"),
            "space"             : colors().colorize(" ",""),
            "corner"            : colors().colorize("+","green"),
        }
        self.horizontal_margin=self.char["corner"]+2*self.char["h_line"]*(self.y)+self.char["corner"]

   
    def put_apple(self, quantity, coordinate_restrictions: set=None):
        for i in range(quantity):
            if coordinate_restrictions==None:
                random_x, random_y = randint(0,self.x-1), randint(0,self.y-1)
                new_apple_coordinates=(random_x,random_y)
            else:
                while True:
                    random_x, random_y = randint(0,self.x-1), randint(0,self.y-1)
                    new_apple_coordinates=(random_x,random_y)

                    if new_apple_coordinates in coordinate_restrictions:
                        continue
                    break
            self.apples_coordinates.add(new_apple_coordinates)


    def detect_apple(self, snake: snakeObject, direction: str): 
        next_coordinates=snake.next_coordinate(direction)
        should_grown=next_coordinates in self.apples_coordinates
        if should_grown:
            self.apples_coordinates.remove(next_coordinates)
            quantity_apples=randint(1,2)
            self.put_apple(quantity_apples)
        return should_grown
    

    def render_str_game(self, snake: snakeObject=None): 
        ascci_string=""
        ascci_string+=self.horizontal_margin+"\n"

        for i in range(self.x):
            ascci_string+=self.char["v_line"]
            for j in range(self.y):
                coordinate=(i,j)
                if coordinate in snake.body:
                    ascci_string+=snake.serpent_character+" "
                elif coordinate in self.apples_coordinates:
                    ascci_string+=self.char["apple"]+" "
                else:
                    ascci_string+=self.char["space"]+" "
            ascci_string+=self.char["v_line"]+"\n"

        ascci_string+=self.horizontal_margin+"\n"
        return ascci_string
    


