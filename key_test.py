import curses
from time import sleep

def purge(screen, y, x):
    screen.clear()
    screen.move(y, x)

def main(screen):
    screen.nodelay(1)
    screen.clear()
    #curses.echo()
    curses.cbreak()
    screen.move(int(curses.LINES/2), int(curses.COLS/2))

    
    key = screen.getkey()
    #print('aaa')
    while key != 'q':

        key = screen.getkey()
        screen.addstr( key)
        screen.refresh()
        sleep(0.3)
        purge(screen, int(curses.LINES/2), int(curses.COLS/2))
        #screen.refresh()

curses.wrapper(main)
