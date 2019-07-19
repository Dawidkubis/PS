from blessed import Terminal

term = Terminal()
with term.fullscreen():
    term.clear()
    with term.location(0, term.height-1):
        print('Hello There')

    with term.cbreak():
        term.inkey()
