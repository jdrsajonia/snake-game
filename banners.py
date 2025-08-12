

# ANSI color codes
MAGENTA = "\033[35m"
LIGHT_GREEN = "\033[92m"
RESET = "\033[0m"

CLEAR="\033[H\033[J"

banner3 = rf"""{LIGHT_GREEN}  
{MAGENTA}███████╗███╗   ██╗ █████╗ ██╗  ██╗██╗   ██╗{LIGHT_GREEN}██████╗ ██╗   ██╗{RESET}
{MAGENTA}██╔════╝████╗  ██║██╔══██╗██║ ██╔╝╚██╗ ██╔╝{LIGHT_GREEN}██╔══██╗╚██╗ ██╔╝{RESET}
{MAGENTA}███████╗██╔██╗ ██║███████║█████╔╝  ╚████╔╝ {LIGHT_GREEN}██████╔╝ ╚████╔╝ {RESET}
{MAGENTA}╚════██║██║╚██╗██║██╔══██║██╔═██╗   ╚██╔╝  {LIGHT_GREEN}██╔═══╝   ╚██╔╝  {RESET}
{MAGENTA}███████║██║ ╚████║██║  ██║██║  ██╗   ██║   {LIGHT_GREEN}██║        ██║   {RESET}
{MAGENTA}╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   {LIGHT_GREEN}╚═╝        ╚═╝   {RESET}
    Made by: jdrsajonia
"""


menu_options=rf"""
{LIGHT_GREEN}[1]{RESET} Start game
{LIGHT_GREEN}[2]{RESET} Game options

{LIGHT_GREEN}[3]{RESET} Exit
"""


game_options=rf"""
{LIGHT_GREEN}[1]{RESET} Change dimensions
{LIGHT_GREEN}[2]{RESET} Change speed

{LIGHT_GREEN}[0]{RESET} Back
"""

change_dimenions=rf"""
{LIGHT_GREEN}[1]{RESET} Small board
{LIGHT_GREEN}[2]{RESET} Middle board
{LIGHT_GREEN}[3]{RESET} Big board
{LIGHT_GREEN}[4]{RESET} Set custom (x,y)

{LIGHT_GREEN}[0]{RESET} Back
"""

change_speed=rf"""
{LIGHT_GREEN}[1]{RESET} Slow
{LIGHT_GREEN}[2]{RESET} Normal
{LIGHT_GREEN}[3]{RESET} Fast
{LIGHT_GREEN}[4]{RESET} Set custom

{LIGHT_GREEN}[0]{RESET} Back
"""

def main():

    stack=[]
    path=[]
    dimensions=()
    speed=None



    def get_path_prompt(path : list):
        return rf"""{MAGENTA}[{"/".join(path)+"] >> "}{RESET}"""



    def go_to(function, label : str):
        stack.append(function)
        path.append(label)
        function()



    def go_back():
        path.pop()
        stack.pop()
        stack[-1]()



    def init_menu():
        print(CLEAR, end="") 
        print(banner3+menu_options)

        option=int(input(get_path_prompt(path)))
        match option:
            case 1:
                go_to(game, "in game")
                pass # iniciar aqui el juego de la serpiente
            case 2:
                go_to(options_menu, "options")
            case 3:
                exit()



    def options_menu():
        print(CLEAR, end="") 
        print(banner3+game_options)
        
        option=int(input(get_path_prompt(path)))
        match option:
            case 1:
                go_to(board_menu, "board settings")
            case 2:
                go_to(speed_menu, "speed settings")
            case 0:
                go_back()
    


    def board_menu():
        print(CLEAR, end="") 
        print(banner3+change_dimenions)

        option=int(input(get_path_prompt(path)))
        match option:
            case 1:
                dimensions=(10,20)
                board_menu()
            case 2:
                dimensions=(15,30)
                board_menu()
            case 3:
                dimensions=(20,40)
                board_menu()
            case 4:
                pass # meter aqui la opcion de board custom 

            case 0:
                go_back()
                

    def speed_menu():
        print(CLEAR, end="") 
        print(banner3+change_speed)

        option=int(input(get_path_prompt(path)))
        match option:
            case 1:
                # meter valor de speed
                speed_menu()
            case 2:
                # meter valor de speed
                speed_menu()
            case 3:
                # meter valor de speed
                speed_menu()
            case 4:
                pass # meter aqui la opcion de speed custom 
            case 0:
                go_back()


    def game():
        print(CLEAR, end="")

        print("game started")
        # import controller
        print("game FINISHED: [1] restart, [0] back menu")
        #ejecutar juego como funcion
        option=int(input(get_path_prompt(path)))

        match option:
            case 1:
                game()          # se ejecuta a si mismo, no es necesario añadir al stack
            case 0:
                go_back()


    go_to(init_menu, "menu")
    
    

    

main()