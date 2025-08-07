import os
import queue


def generate_matrix(row:int,column:int):
    rows=["-" for i in range(row)]
    matrix=[rows.copy() for j in range(column)]
    return matrix


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

        self.head=node((0,0))
        self.tail=None

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
    
    def move_to(self, direction_key:str):
        actual_position=self.get_position()
        direction=self.keys[direction_key]
        new_position=self._sum_vectors(actual_position,direction)
        self.set_position(new_position)
        pass



def move_test():

    matrix=generate_matrix(10,10)
    
    snake=snakeObject()

    init_position=snake.get_position()
    x,y=init_position

    matrix[x][y]="S"

    
    while True:
        
        print_matrix(matrix)
        input_direction=input("(W A S D) >> ")

        old_position=snake.get_position()

        snake.move_to(input_direction)
        
        actual_position=snake.get_position()

        x,y=old_position
        matrix[x][y]="-"

        x,y=actual_position
        matrix[x][y]="S"


        os.system("cls")

        print(x,y)



move_test()
