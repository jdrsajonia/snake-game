from collections import deque
from random import randint

class node:
    # probablemente quitar esta clase, ya que solo estamos trabajando con coordenadas
    def __init__(self, position: tuple):
        self.type=None
        self.x, self.y = position
    
    def get_position(self):
        return self.x, self.y
    
    def set_position(self, position: tuple):
        self.x, self.y = position

    def set_type(self, arg: str):
        self.type=arg


class snakeObject:
    def __init__(self, warp_dimensions: tuple):

        self.long=1
        self.body=deque()
        self.head=node((0,0))
        self.body.append(self.head.get_position())

        self.warp_x, self.warp_y = warp_dimensions

        self.keys={ 
                    "w":(-1,0),     # arriba
                    "a":(0,-1),     # izquierda
                    "s":(1,0),      # abajo
                    "d":(0,1)       # derecha
                    }
        
        self.current_direction=(0,1)
    
    @staticmethod
    def _sum_vectors(vector1:tuple, vector2:tuple):
        new_vector = tuple((v1+v2) for v1, v2 in zip(vector1, vector2)) #AQUI SE PUEDE METER EL MODULO PARA ARREGLAR EL PROBLEMA DE LOS LIMITES
        return new_vector
    

    def get_direction(self, key:str):
        self.current_direction=self.keys[key]  #!! controlador en la serpiente
        return self.current_direction


    def set_head_position(self, coordenates: tuple):
        self.head.set_position(coordenates)
    

    def get_head_position(self):
        return self.head.get_position()
    
    
    def _normalize_position(self,coordenate: tuple):
        current_x,current_y=coordenate
        current_x=current_x%self.warp_x
        current_y=current_y%self.warp_y
        return current_x, current_y
    
    def increment(self):
        self.long+=1
        tail_position=self.body[0]
        self.body.append(tail_position)
        

    def detect_colition(self, new_coordenate):
        if new_coordenate in self.body:
            raise ValueError("LA SERPIENTE HA CHOCADO CON SU PROPIO CUERPO!!!")

    def move_to(self, direction_key:str, grow_up=False):
        actual_position=self.get_head_position()
        current_direction=self.get_direction(direction_key) 

        if grow_up:
            self.increment()

        new_position=self._sum_vectors(actual_position,current_direction)

        new_position=self._normalize_position(new_position)
        self.detect_colition(new_position)
       
        self.body.pop()     #NOTA: tambien con esto se podría incrementar el tamaño, simplemente bypaseando la linea con grow_up con (if not grow_up)
        self.set_head_position(new_position)
        self.body.appendleft(new_position)
        

    
    

    



class boardObject:
    
    def __init__(self,dimension):
        self.x, self.y = dimension
        self.matrix=self._generate_matrix(self.y, self.x)
        self.apples_coordenates=set()

        self.horizontal_character="="
        self.vertical_character="|"
        self.serpent_character="\033[95m■\033[0m"
        self.apple_character="▫"
        self.space_character=" "
        self.borders_character="+"
        self.horizontal_margin=self.borders_character+2*self.horizontal_character*(self.y)+self.borders_character


    @staticmethod
    def _generate_matrix(row:int,column:int):
        space=None

        rows=[space for i in range(row)]
        matrix=[rows.copy() for j in range(column)]
        return matrix

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
    

    def current_game(self, snake: snakeObject=None):

        ascci_string=""


        ascci_string+=self.horizontal_margin+"\n"

        for i in range(self.x):
            ascci_string+=self.vertical_character
            for j in range(self.y):
                coordenate=(i,j)
                if coordenate in snake.body:
                    ascci_string+=self.serpent_character+" "
                elif coordenate in self.apples_coordenates:
                    ascci_string+=self.apple_character+" "
                else:
                    ascci_string+=self.space_character+" "
            ascci_string+=self.vertical_character+"\n"

        ascci_string+=self.horizontal_margin+"\n"
        return ascci_string