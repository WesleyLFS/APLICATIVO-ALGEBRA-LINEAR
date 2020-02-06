from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class Gerenciador(ScreenManager):
    pass

class Inicio(Screen):
    pass

class Main(App):

    def build(self):
        return Gerenciador()


if __name__ == '__main__':
    Main().run()