import os
import random
import time
from collections import deque



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
        
        self.current_direction=(0,1)
    
    @staticmethod
    def _sum_vectors(vector1:tuple, vector2:tuple):
        new_vector = tuple((v1+v2)%10 for v1, v2 in zip(vector1, vector2)) #AQUI SE PUEDE METER EL MODULO PARA ARREGLAR EL PROBLEMA DE LOS LIMITES
        return new_vector
    

    def get_direction(self, key:str):
        self.current_direction=self.keys[key]       # ver si separamos la logica del controlador con la de la serpiente
        return self.current_direction

    def set_head_position(self, coordenates: tuple):
        self.head.set_position(coordenates)
    
    def get_head_position(self):
        return self.head.get_position()
    

    def detectar_manzana(): #??
        pass

    def move_to(self, direction_key:str, grow_up=False):
        actual_position=self.get_head_position()

        current_direction=self.get_direction(direction_key) #la ultima direccion se actualiza aqui


        # aqui se podría incrementar el tamaño
        if grow_up:
            self.increment()

        new_position=self._sum_vectors(actual_position,current_direction)
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

        #   CAMBIAR ESTRATEGIA DE IMPRESION (esta no permite que la serpiente rebase los limites y vuelva)
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


    # los metodos relacionados con las manzanas, es posible que toque colocarlos en un controlador a parte para evitar el acoplamiento

    def put_apple(self, quantity):
        for i in range(quantity):
            random_x=random.randint(1,self.x-1)
            random_y=random.randint(1,self.y-1)

            new_apple_coordenates=(random_x,random_y)
            self.apples_coordenates.add(new_apple_coordenates)

            self.matrix[random_x][random_y]="W"
        pass

    
  

def detect_apple(board: boardObject, snake: snakeObject, direction: tuple):
    next_coordenates=snake._sum_vectors(snake.get_head_position(), snake.get_direction(direction))
    should_grown = next_coordenates in board.apples_coordenates
    if should_grown:
        x,y=next_coordenates
        board.matrix[x][y]="-"
        board.apples_coordenates.remove(next_coordenates)

    return should_grown

def controller():
    #si en su proximo movimiento hay una manzana, crecer en uno
    os.system("cls")
    board=boardObject((10,10))
    snake=snakeObject()

    board.put_apple(5)

    while True:
        print(snake.body)
        print(f"apples = {board.apples_coordenates}")
        print(f"head = {snake.get_head_position()}")
        print(f"direction = {snake.current_direction}")
        board.print_matrix_snake(snake)
        

        input_direction=input("(W A S D) >> ")
        # grow_up=bool(int(input("1/0 >>")))

        grow=detect_apple(board,snake,input_direction)

        snake.move_to(input_direction, grow)
        # board.tmp_detect_apple(snake)
        
        os.system("cls")
        

controller()


