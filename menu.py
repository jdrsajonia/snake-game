from gameLogic import snakeGameObject, KeyboardController

class menuObject:

    def __init__(self):

        self.stack=[]
        self.path=[]

        self.properties={"dimension":(10,30), "speed": 8}
        self.size_board="Small"
        self.speed="Normal"

        self._game_object=None

        self.magenta = "\033[35m"
        self.light_green = "\033[92m"
        self.cian="\033[96m"
        self.light_red="\033[91m"
        self.reset = "\033[0m"
        self.clear="\033[H\033[J"

        self.banner3 = rf"""{self.light_green}  
{self.magenta}███████╗███╗   ██╗ █████╗ ██╗  ██╗██╗   ██╗{self.light_green}██████╗ ██╗   ██╗{self.reset}
{self.magenta}██╔════╝████╗  ██║██╔══██╗██║ ██╔╝╚██╗ ██╔╝{self.light_green}██╔══██╗╚██╗ ██╔╝{self.reset}
{self.magenta}███████╗██╔██╗ ██║███████║█████╔╝  ╚████╔╝ {self.light_green}██████╔╝ ╚████╔╝ {self.reset}
{self.magenta}╚════██║██║╚██╗██║██╔══██║██╔═██╗   ╚██╔╝  {self.light_green}██╔═══╝   ╚██╔╝  {self.reset}
{self.magenta}███████║██║ ╚████║██║  ██║██║  ██╗   ██║   {self.light_green}██║        ██║   {self.reset}
{self.magenta}╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {self.light_green}╚═╝        ╚═╝   {self.reset}
    Made by: jdrsajonia

"""

        self.menu_options=rf"""
{self.light_green}[1]{self.reset} Start game
{self.light_green}[2]{self.reset} Settings

{self.light_green}[3]{self.reset} Exit
"""

        self._game_options=rf"""
{self.light_green}[1]{self.reset} Change dimensions
{self.light_green}[2]{self.reset} Change speed

{self.light_green}[0]{self.reset} Back
"""

        self.change_dimenions=rf"""
{self.light_green}[1]{self.reset} Small board
{self.light_green}[2]{self.reset} Middle board
{self.light_green}[3]{self.reset} Big board
{self.light_green}[4]{self.reset} Set custom (x,y) ¡NOT AVAILABLE!

{self.light_green}[0]{self.reset} Back
"""

        self.change_speed=rf"""
{self.light_green}[1]{self.reset} Slow
{self.light_green}[2]{self.reset} Normal
{self.light_green}[3]{self.reset} Fast
{self.light_green}[4]{self.reset} Set custom [1,10] ¡NOT AVAILABLE!

{self.light_green}[0]{self.reset} Back
"""


    def _get_path_prompt(self,path : list):
        return rf"""{self.magenta}[{"/".join(path)+"] >> "}{self.reset}"""

    def _get_str_properties(self):
        return rf"""{self.cian}[Board: {self.size_board}] [Speed: {self.speed}]{self.reset}"""

    def _go_to(self,function, label : str):
        self.stack.append(function)
        self.path.append(label)
        function()


    def _go_back_(self):
        self.path.pop()
        self.stack.pop()
        self.stack[-1]()



    def _init_menu(self):
        print(self.clear, end="") 
        print(self.banner3+self._get_str_properties()+self.menu_options)

        option=str(input(self._get_path_prompt(self.path)))
        match option:
            case "1":
                self._go_to(self._game, "in game")
                pass # iniciar aqui el juego de la serpiente
            case "2":
                self._go_to(self._options_menu, "settings")
            case "3":
                exit()
            case _:
                self._init_menu()



    def _options_menu(self):
        print(self.clear, end="") 
        print(self.banner3+self._get_str_properties()+self._game_options)
        
        option=str(input(self._get_path_prompt(self.path)))
        match option:
            case "1":
                self._go_to(self._board_menu, "board settings")
            case "2":
                self._go_to(self._speed_menu, "speed settings")
            case "0":
                self._go_back_()
            case _: 
                self._options_menu() 
    


    def _board_menu(self):
        print(self.clear, end="") 
        print(self.banner3+self._get_str_properties()+self.change_dimenions)

        option=str(input(self._get_path_prompt(self.path)))
        match option:
            case "1":
                self.properties["dimension"]=(10,30)
                self.size_board="Small"
                self._board_menu()
            case "2":
                self.properties["dimension"]=(15,40)
                self.size_board="Middle"
                self._board_menu()
            case "3":
                self.properties["dimension"]=(20,50)
                self.size_board="Big"
                self._board_menu()
            case "4":
                self._board_menu()
                 # meter aqui la opcion de board custom 
            case "0":
                self._go_back_()
            case _: 
                self._board_menu() 
                

    def _speed_menu(self):
        print(self.clear, end="") 
        print(self.banner3+self._get_str_properties()+self.change_speed)

        option=str(input(self._get_path_prompt(self.path)))
        match option:
            case "1":
                self.properties["speed"]=3
                self.speed="Slow"
                self._speed_menu()
            case "2":
                # meter valor de speed
                self.properties["speed"]=8
                self.speed="Normal"
                self._speed_menu()
            case "3":
                # meter valor de speed
                self.properties["speed"]=10
                self.speed="Fast"
                self._speed_menu()
            case "4":
                self._speed_menu()
                # meter aqui la opcion de speed custom 
            case "0":
                self._go_back_()

            case _: 
                self._speed_menu() 


    def _game(self):
        print(self.clear, end="")
        game=snakeGameObject(controller=KeyboardController())
        game.set_properties(self.properties)

        game.start()
        

        print(f"{self.light_red}¡GAME FINISHED!{self.reset} \n{self.light_green}Score: {game.snake.long}{self.reset}\n{self.light_green}{self.light_green}[1]{self.reset} restart, {self.light_green}[0]{self.reset} back menu\n{self.reset}")
        
        option=str(input(self._get_path_prompt(self.path)))
        match option:
            case "1":
                self._game()          # se ejecuta a si mismo, no es necesario añadir al stack
            case _:
                self._go_back_()
            


    def start(self):
        self._go_to(self._init_menu, "menu")


    def set_game(self,game_object):
        self._game_object=game_object

    # def set_properties(self, properties): ??? poner en la clase Juego
    #     self.properties=properties


menu=menuObject()
menu.start()