import curses as cs
import stuff as st
import subprocess
import termcolor
import os
import sys

def cons_draw(screen):
    screen.addstr(int(cs.LINES/8), int(cs.COLS/6), ' MENU ', cs.A_STANDOUT)
    screen.refresh()

def main(screen):
    cons_draw(screen)
    #screen.clear()
    while True:
        key = screen.getch()

        screen.refresh()



# [exception handling]
try:
    if len(sys.argv) > 1:
        raise st.MError(f'Usage : {sys.argv[0]}'+ termcolor.colored('  # no arguments', color='yellow'))
    if __name__ in ('__main__','__console__'):
        cs.wrapper(main)
    else:
        raise st.MError('please dont import me :D')
except st.MError as me:
    print(me.msg)
    exit(termcolor.colored('\n\tFUCK--^\n', color='red'))
