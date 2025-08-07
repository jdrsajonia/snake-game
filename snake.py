import os
import random
import time
from collections import deque



def generate_matrix(row:int,column:int):
    rows=["-" for i in range(row)]
    matrix=[rows.copy() for j in range(column)]
    return matrix

def put_apple(matrix):

    column=len(matrix)
    row=len(matrix[0])

    random_x=random.randint(1, column-1)
    random_y=random.randint(1,row-1)
    # apple=node(random_x,random_y)
    # apple.set_type("W")
    matrix[random_y][random_x]="W"

def print_matrix(matrix):
    x=len(matrix)
    y=len(matrix[0])
    for i in range(x):
        for j in range(y):
            print(matrix[i][j], end=" ")
        print()


class node:

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
    def __init__(self):

        self.long=1

        self.body=deque()

        self.head=node((0,0))
        self.body.append(self.head.get_position())

        # self.tail=node((0,0))

        self.keys={ 
                    "w":(-1,0),     # arriba
                    "a":(0,-1),     # izquierda
                    "s":(1,0),      # abajo
                    "d":(0,1)       # derecha
                    }
    
    @staticmethod
    def _sum_vectors(vector1:tuple, vector2:tuple):
        new_vector = tuple(v1+v2 for v1, v2 in zip(vector1, vector2))
        return new_vector
    

    def get_direction(self, key:str):
        return self.keys[key]

    def set_head_position(self, coordenates: tuple):
        self.head.set_position(coordenates)
    
    def get_head_position(self):
        return self.head.get_position()
    
    def move_to(self, direction_key:str, crecer=False):
        actual_position=self.get_head_position()
        # pedazo de codigo de prueba
        if crecer:
            self.increment()
            pass
        # borrar despues 
        new_position=self._sum_vectors(actual_position,self.keys[direction_key])
        self.detect_colition(new_position)
        self.body.pop()     # eliminar punta de la cola
        self.set_head_position(new_position)
        self.body.appendleft(new_position)
        pass
    

    def increment(self):
        # al incrementar, necesitamos añadir la posicion actual DE LA COLA
        self.long+=1
        tail_position=self.body[0]
        self.body.append(tail_position)
        pass

    def detect_colition(self, new_coordenate):
        if new_coordenate in self.body:
            raise ValueError("LA SERPIENTE HA CHOCADO CON SU PROPIO CUERPO!!!")
        pass

    

class boardObject:
    def __init__(self,dimension):
        self.x, self.y = dimension
        self.matrix=self._generate_matrix(self.y, self.x)

        self.apples_coordenates=set()

    @staticmethod
    def _generate_matrix(row:int,column:int):
        rows=["-" for i in range(row)]
        matrix=[rows.copy() for j in range(column)]
        return matrix
    
    def print_matrix_snake(self,snake: snakeObject=None):
        # intenetar retornar un string y con _str_ formatear el print (pensar que hacer con snakeObject)
        x=len(self.matrix)
        y=len(self.matrix[0])
        for i in range(x):
            for j in range(y):
                coordenate=(i,j)
                if coordenate in snake.body:
                    print("S", end=" ")
                else:
                    print(self.matrix[i][j], end=" ")
            print()


    def put_apple(self, quantity):
        for i in range(quantity):
            random_x=random.randint(1,self.x-1)
            random_y=random.randint(1,self.y-1)

            new_apple_coordenates=(random_x,random_y)
            self.apples_coordenates.add(new_apple_coordenates)

            self.matrix[random_x][random_y]="W"
        pass


    def tmp_detect_apple(self, snake: snakeObject=None):
        head=snake.get_head_position()
        if head in self.apples_coordenates:
            snake.increment()
            self.apples_coordenates.remove(head)
            x,y=head
            self.matrix[x][y]="-"

        pass




def move_test_v2():
    board=boardObject((10,10))
    snake=snakeObject()

    board.put_apple(5)

    while True:
        print(snake.body)
        print(f"apples = {board.apples_coordenates}")
        print(f"head = {snake.get_head_position()}")
        board.print_matrix_snake(snake)
        board.tmp_detect_apple(snake)
        input_direction=input("(W A S D) >> ")
        
        snake.move_to(input_direction)
        
        os.system("cls")
        
    pass



move_test_v2()


