from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager

class Gerenciador(ScreenManager):
    pass

class Inicio(Screen):
    pass

class Matriz(Screen):
    pass

class 1Matriz(Screen):
    pass

class 1M.Selecao(Screen):
    pass

class 1M.Valores(Screen):
    pass

class 1M.Resultado(Screen):
    pass

class 2Matriz(Screen):
    pass

class 2M.Selecao(Screen):
    pass

class 2M.Valores(Screen):
    pass

class 2M.Resultado(Screen):
    pass

class SL.Selecao(Screen):
    pass

class SL.Valores(Screen):
    pass

class SL.Resultado(Screen):
    pass

class Main(App):

    def build(self):
        return Gerenciador()


if __name__ == '__main__':
    Main().run()
