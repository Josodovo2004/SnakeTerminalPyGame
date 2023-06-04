import curses
import snake
import apple

screen = curses.initscr()
snake = snake.Snake('#','o', 20, 10)
apple = apple.Apple("@")
curses.curs_set(0)
screen.nodelay(1) #this is because we want te snake to keep moving, otherwise it will wait untill we push some button


def main(screen):

    points = 0
    body = []
    cordinates = []

    while True:
        key = screen.getch()

        screen.erase()

        apple.position_apple(screen, cordinates)

        head_last_spot = (snake.row,snake.column)

        snake.movement(key)

        snake.positionate(screen)

        snake.body_len(points, body)

        snake.body_x_y(body, head_last_spot, cordinates)

        for n in range(0,len(body)):
            screen.addstr(cordinates[n][0],cordinates[n][1],body[n])

        curses.napms(100) #time in miliseconds

        if key == ord('q'):
            break

        if (snake.row, snake.column) in cordinates:
            break

        if apple.row == snake.row and apple.column == snake.column:
            points += 1
            apple.rand_position()
            apple.position_apple(screen)

        screen.addstr(20,0, "---------------------------------------------")
        screen.addstr(20, 45, f"POINTS : {points}")
        screen.addstr(20,56, "------------------------")

        screen.refresh()

    curses.endwin()


curses.wrapper(main)