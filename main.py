import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '900')
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.clock import Clock


class GameScreen(Widget):
    player = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.player.pos = (0, 0)
        self.player.speed = [0, 0]

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print(keycode[1])
        if keycode[1] == 'w' and self.player.speed[1] < 5:
            self.player.speed[1] += 1
        if keycode[1] == 's' and self.player.speed[1] > -5:
            self.player.speed[1] -= 1
        if keycode[1] == 'a' and self.player.speed[0] > -5:
            self.player.speed[0] -= 1
        if keycode[1] == 'd' and self.player.speed[0] < 5:
            self.player.speed[0] += 1
        return True

    def update(self, dt):
        if 0 <= (self.player.pos[0] + self.player.speed[0]) < 800:
            self.player.pos[0] += self.player.speed[0]
            if self.player.speed[0] > 0:
                self.player.speed[0] -= 0.25
            elif self.player.speed[0] < 0:
                self.player.speed[0] += 0.25
        else:
            self.player.speed[0] = 0
        if 0 <= (self.player.pos[1] + self.player.speed[1]) < 800:
            self.player.pos[1] += self.player.speed[1]
            if self.player.speed[1] > 0:
                self.player.speed[1] -= 0.25
            elif self.player.speed[1] < 0:
                self.player.speed[1] += 0.25
        else:
            self.player.speed[1] = 0


class Player(Widget):
    pass


class SonicGameApp(App):
    def build(self):
        self.load_kv('main.kv')
        game = GameScreen()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    SonicGameApp().run()
