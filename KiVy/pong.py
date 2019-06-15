import kivy
kivy.require('1.10.1')
from kivy.app import App
from kivy.uix.widget import Widget

class PongGame(Widget):
    pass

class PongApp(App):
    def build(self):
        return PongGame()

class PongBall(Widget):
    pass

if __name__ == '__main__':
    PongApp().run()
