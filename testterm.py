import curses

def main(screen):
    screen.clear()
    screen.nodelay(False)
    screen.box()
    h, w = screen.getmaxyx()

    key = 0
    point = [int(h/2), int(w/2)]
    move = point[:]
    while key != ord('q'):
        #print(h)
        move = point[:]
        key = screen.getch()
        if key == curses.KEY_LEFT:
            move[1] = point[1] - 1
        elif key == curses.KEY_RIGHT:
            move[1] = point[1] + 1
        elif key == curses.KEY_UP:
            move[0] = point[0] - 1
        elif key == curses.KEY_DOWN:
            move[0] = point[0] + 1
        if move[0] in range(0, h) and move[1] in range(0, w):
            if not (move[0] > h-2 and move[1]>93):
                point = move[:]


        screen.clear()
        screen.box()
        screen.addstr(*point, '<'+str(point))

curses.wrapper(main)
