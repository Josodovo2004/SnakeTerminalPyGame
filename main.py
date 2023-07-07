import curses
import snake
import apple

with open("highscore.txt", "r") as file:
    highscore = file.readline()
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
            screen.erase()
            screen.addstr(10, 40, "Game Over :c")
            screen.addstr(12, 30, f"Your score: {points}")
            screen.addstr(12, 50, f"Last high score: {highscore}")
            if points > int(highscore):
                with open("highscore.txt", "w") as file:
                    file.write(str(points))
                screen.addstr(14, 28, "Congratulations, that is a new high score!!")
            screen.refresh()
            curses.napms(2000)
            break

        if apple.row == snake.row and apple.column == snake.column:
            points += 1
            apple.rand_position()
            apple.position_apple(screen, cordinates)

        for i in range(0,20):
            screen.addstr(i,80,"|")
        screen.addstr(20,0, f"--------------- HIGH SCORE: {highscore} -------------")
        screen.addstr(20, 45, f"SCORE : {points}")
        screen.addstr(20,56, "------------------------")

        screen.refresh()

    curses.endwin()


curses.wrapper(main)