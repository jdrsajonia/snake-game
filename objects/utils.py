class colors:
    def __init__(self):
        self.is_colorized=True
    
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
            "light_black": 90,
            "light_red": 91,
            "light_green": 92,
            "light_yellow": 93,
            "light_blue": 94,
            "light_magenta": 95,
            "light_cyan": 96,
            "light_white": 97,
            "":37
        }

        if not self.is_colorized:
            return char
        color=str(colors[color])
        return "\033["+color+"m"+char+"\033[0m"
    

