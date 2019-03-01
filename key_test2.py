import curses
from time import sleep

def main(screen):

    screen.nodelay(1)
    screen.clear()

    key = screen.getch()
    #print(key)
    print('test')
    sleep(1)

curses.wrapper(main)
