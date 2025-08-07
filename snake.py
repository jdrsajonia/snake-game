import os
import random
import time
from collections import deque
# usar append y popleft


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


# def update_matrix(matrix):
#     row=len(matrix[0])
#     column=len(matrix)
#     for i in range(column):
#         for j in range(row):
#             if (i,j) in 
#             matrix[i][j]="O"
#     pass




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

    def set_position(self, coordenates: tuple):
        self.head.set_position(coordenates)
    
    def get_position(self):
        return self.head.get_position()
    


    def move_to(self, direction_key:str, crecer=False):

        actual_position=self.get_position()

        


        # pedazo de codigo de prueba
        if crecer:
            self.increment()
            pass
        # borrar despues
        

        new_position=self._sum_vectors(actual_position,self.keys[direction_key])
        
        self.detect_colition(new_position)
        self.body.pop()     # eliminar punta de la cola

        

        self.set_position(new_position)

        self.body.appendleft(new_position)
        pass
    

    def increment(self):
        self.long+=1

        # al incrementar, necesitamos añadir la posicion actual DE LA COLA

        tail_position=self.body[0]

        self.body.append(tail_position)
        pass

    def detect_colition(self, new_coordenate):
        if new_coordenate in self.body:
            raise ValueError("LA SERPIENTE HA CHOCADO CON SU PROPIO CUERPO!!!")

        pass



def print_matrix_snake(matrix, snake: snakeObject):
    x=len(matrix)
    y=len(matrix[0])
    for i in range(x):
        for j in range(y):
            
            coordenate=(i,j)
            if coordenate in snake.body:
                print("S", end=" ")
            else:
                print(matrix[i][j], end=" ")
           
        print()


# def move_test():

#     matrix=generate_matrix(10,10)
#     put_apple(matrix)
#     snake=snakeObject()

#     init_position=snake.get_position()
#     x,y=init_position

#     matrix[x][y]="S"

    
#     while True:
        
#         print_matrix(matrix)
#         input_direction=input("(W A S D) >> ")
#         input_crecer=bool(int(input("True/False (1/0) >> ")))

#         old_position=snake.get_position()

#         snake.move_to(input_direction, input_crecer)
        
#         actual_position=snake.get_position()

#         x,y=old_position
#         matrix[x][y]="-"

#         x,y=actual_position
#         matrix[x][y]="S"


#         os.system("cls")

#         print(x,y)
#         print(snake.body)


def move_test_v2():
    matrix=generate_matrix(10,10)
    snake=snakeObject()

    while True:
        print(snake.body)
        print_matrix_snake(matrix, snake)
        input_direction=input("(W A S D) >> ")
        input_crecer=bool(int(input("True/False (1/0) >> ")))

        snake.move_to(input_direction, input_crecer)
        os.system("cls")
        
    pass


# move_test()
move_test_v2()
