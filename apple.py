import random

class Apple:
    def __init__(self, icon: str, colmun = random.randint(0,80), row = random.randint(0,19)) -> None:
        
        self.icon = icon
        self.column = colmun
        self.row = row

    def rand_position(self):
        self.column = random.randint(0,80)
        self.row = random.randint(0,19)
        return self.column, self.row
    
    def position_apple(self, screen):
        screen.addstr(self.row, self.column, self.icon)