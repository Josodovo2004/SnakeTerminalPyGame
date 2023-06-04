import curses

class Snake:
    def __init__(self, headcell: str, bodycell: str, column: int = 20, row: int =10, ) -> None: 

        self.headcell = headcell
        self.bodycell = bodycell
        self.column = column
        self.row = row
        self.direction = curses.KEY_RIGHT


    def positionate(self, screen):
        if self.column > 79:
            self.column = 0
        if self.column < 0:
            self.column = 79
        if self.row > 19:       #here wr check if the head of the snake is out of limits
            self.row = 0        #and if it is, it appears at the other side of the screen 
        if self.row < 0:
            self.row = 19
        screen.addstr(self.row, self.column, self.headcell)

    def body_len(self, points: int, body: list):
        while len(body) <= points -1:
            body.append(self.bodycell)
    
    def body_x_y(self, body, head_last_spot, cordinates):
        if len(cordinates) > 0:
            cordinates.pop()
        while len(cordinates) < len(body):
            cordinates.insert(0, head_last_spot)



    def movement(self, key):

        if key == curses.KEY_UP and self.direction != curses.KEY_DOWN:
            self.direction = curses.KEY_UP
        elif key == curses.KEY_DOWN and self.direction != curses.KEY_UP:
            self.direction = curses.KEY_DOWN
        elif key == curses.KEY_LEFT and self.direction != curses.KEY_RIGHT:
            self.direction = curses.KEY_LEFT
        elif key == curses.KEY_RIGHT and self.direction != curses.KEY_LEFT:
            self.direction = curses.KEY_RIGHT

        if self.direction == curses.KEY_UP:
             self.row -= 1
        elif self.direction == curses.KEY_DOWN:
             self.row += 1
        elif self.direction == curses.KEY_LEFT:
             self.column -= 1
        elif self.direction == curses.KEY_RIGHT:
             self.column += 1

        return self.column, self.row
    