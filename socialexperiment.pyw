from pykeyboard import PyKeyboard, PyKeyboardEvent
from time import sleep
import random

keyboard = PyKeyboard()
event = PyKeyboardEvent()



while True:
	sleep(random.randint(0,360))
	keyboard.tap_key(keyboard.escape_key)