import curses
import random
from time import sleep

class PlayGround:
    def __init__(self, screen):
        h, w = screen.getmaxyx()
        self.box = [[2,2],[h-2,w-2]]

    def __contains__(self, snake):
        assert(type(snake)==Snake), 'not a snake'

    def draw_box(horizontal='-', vertical = '|'):
        pass


class Snake:
    def __init__(self, body):
        self.body = body

    def move(point):
        pass

def main(screen):
    curses.curs_set(0)
    screen.clear()
    screen.nodelay(True)
    screen.keypad(True)
    h, w = screen.getmaxyx()

    playground = PlayGround(screen)
    snake = Snake([[10,32], [10,31], [10,30]])

    accepted_keys = [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]
    key = curses.KEY_RIGHT

    while True:
        x = screen.getch()
        if x == ord('q'):
            break
        key = x if x in accepted_keys else key


curses.wrapper(main)
