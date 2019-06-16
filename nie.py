#!/usr/bin/python

from termcolor import cprint, COLORS
import random

while True:
    cprint('NIE!!',end='',color=random.choice(list(COLORS.keys())))
    
