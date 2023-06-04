import curses

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(1)


    character_row = 10
    character_col = 20

    while True:
        stdscr.erase()

        key = stdscr.getch()
        if key == ord('q'):
            break

        if key == curses.KEY_UP:
            character_row -= 1
        elif key == curses.KEY_DOWN:
            character_row += 1
        elif key == curses.KEY_LEFT:
            character_col -= 1
        elif key == curses.KEY_RIGHT:
            character_col += 1
        
        stdscr.addch(character_row, character_col, 's')

        stdscr.refresh()

curses.wrapper(main)
