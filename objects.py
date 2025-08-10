from collections import deque
from random import randint


class snakeObject:
    def __init__(self, warp_dimensions: tuple):

        self.long=1
        self.body=deque()
        self.head_position=(0,0)
        self.body.append(self.head_position)

        self.is_colorized=True
        self.serpent_character=self.colorize("■","magenta")

        self.warp_x, self.warp_y = warp_dimensions

        self.up, self.left, self.down, self.right = ("w", "a", "s", "d")

        self.keys={ 
                    self.up:(-1,0),     
                    self.left:(0,-1),   
                    self.down:(1,0),      
                    self.right:(0,1)       
                    }
        
        self.current_direction=(0,1)
        self.colition=False
    

    # def set_controls(self,up, left, down, right):
    #     self.up, self.left, self.down, self.right = up, left, down, right
    #     self.keys={ 
    #                 self.up:(-1,0),     
    #                 self.left:(0,-1),    
    #                 self.down:(1,0),      
    #                 self.right:(0,1)       
    #                 }

    def colorize(self, char: str, color:str):
        colors = {
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "magenta": 35,
            "cyan": 36,
            "white": 37,
            "b_black": 90,
            "b_red": 91,
            "b_green": 92,
            "b_yellow": 93,
            "b_blue": 94,
            "b_magenta": 95,
            "b_cyan": 96,
            "b_white": 97,
            "":37
        }
        if not self.is_colorized:
            return char
        color=str(colors[color])
        return "\033["+color+"m"+char+"\033[0m"
    
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
    

    def set_head_position(self, coordenates: tuple):
        self.head_position=coordenates
    

    def _normalize_position(self,coordenate: tuple):
        current_x,current_y=coordenate
        current_x=current_x%self.warp_x
        current_y=current_y%self.warp_y
        return current_x, current_y
    

    def detect_colition(self, new_coordenate):
        if new_coordenate in self.body:
            self.colition=True


    def move_to(self, direction_key:str, grow_up=False):
        actual_position=self.get_head_position()
        current_direction=self.adjust_direction(direction_key) 

        new_position=self._sum_vectors(actual_position,current_direction)

        new_position=self._normalize_position(new_position)
        self.detect_colition(new_position)

        if not grow_up:
            self.body.pop()     # crece = no elimina su cola al moverse
        else:
            self.long+=1 

        self.set_head_position(new_position)
        self.body.appendleft(new_position)
        
    
class boardObject:
    
    def __init__(self,dimension):
        # self.matrix=self._generate_matrix(self.y, self.x)
        self.x, self.y = dimension
        self.apples_coordenates=set()
        self.is_colorized=True

        # self.serpent_character    = self.colorize("■","magenta")
    
        self.char={
            "h_line"            : self.colorize("=",""),
            "v_line"            : self.colorize("|",""),
            "serpent"           : self.colorize("■","magenta"),
            "apple"             : self.colorize("▫","green"),
            "space"             : " ",
            "corner"            : self.colorize("+","green"),
        }

        self.horizontal_margin=self.char["corner"]+2*self.char["h_line"]*(self.y)+self.char["corner"]

    def colorize(self, char: str, color:str):
        colors = {
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "magenta": 35,
            "cyan": 36,
            "white": 37,
            "b_black": 90,
            "b_red": 91,
            "b_green": 92,
            "b_yellow": 93,
            "b_blue": 94,
            "b_magenta": 95,
            "b_cyan": 96,
            "b_white": 97,
            "":37
        }
        if not self.is_colorized:
            return char
        color=str(colors[color])
        return "\033["+color+"m"+char+"\033[0m"

    # @staticmethod
    # def _generate_matrix(row:int,column:int):
    #     space=None

    #     rows=[space for i in range(row)]
    #     matrix=[rows.copy() for j in range(column)]
    #     return matrix

    # los metodos relacionados con las manzanas, es posible que toque colocarlos en un controlador a parte para evitar el acoplamiento
    def put_apple(self, quantity, coordenate_restrictions: set=None):
        for i in range(quantity):
            if coordenate_restrictions==None:
                random_x, random_y = randint(0,self.x-1), randint(0,self.y-1)
                new_apple_coordenates=(random_x,random_y)
            else:
                while True:
                    random_x, random_y = randint(0,self.x-1), randint(0,self.y-1)
                    new_apple_coordenates=(random_x,random_y)

                    if new_apple_coordenates in coordenate_restrictions:
                        continue
                    break

            self.apples_coordenates.add(new_apple_coordenates)
            # self.matrix[random_x][random_y]="▫"
    

    def str_current_game(self, snake: snakeObject=None): # metodo que renderiza la escena (ver si se puede separar de boardObject)
        ascci_string=""
        ascci_string+=self.horizontal_margin+"\n"

        for i in range(self.x):
            ascci_string+=self.char["v_line"]
            for j in range(self.y):
                coordenate=(i,j)
                if coordenate in snake.body:
                    ascci_string+=snake.serpent_character+" "
                elif coordenate in self.apples_coordenates:
                    ascci_string+=self.char["apple"]+" "
                else:
                    ascci_string+=self.char["space"]+" "
            ascci_string+=self.char["v_line"]+"\n"

        ascci_string+=self.horizontal_margin+"\n"
        return ascci_string
    


    def detect_apple(self, snake: snakeObject, direction: str): 
                                                                                #next coordenates se puede dejar como atributo de snake, y este atributo se puede rescatar aqui
        next_coordenates=snake._sum_vectors(snake.get_head_position(), snake.adjust_direction(direction))
        should_grown=next_coordenates in self.apples_coordenates
        if should_grown:
            # x,y=next_coordenates
            self.apples_coordenates.remove(next_coordenates)
            quantity_apples=randint(1,2)
            self.put_apple(quantity_apples)
        return should_grown