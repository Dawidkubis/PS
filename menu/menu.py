from blessed import Terminal
from time import sleep
import os
import sys

def initscr(term):
    term.clear()
    with term.location(x=int(term.width/6), y=int(term.height/5)):
        print(term.on_white(term.black(term.underline(' MENU '))))


def main():
    term = Terminal()
    with term.fullscreen():
        initscr(term)
        sleep(2)

if __name__=='__main__':
    main()
