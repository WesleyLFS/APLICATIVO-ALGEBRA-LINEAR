from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Main(App):
    def build(self):
        lb = Label(text='hello,world!')
        bt = Button(text='press')
        box = BoxLayout()
        box.add_widget(lb)
        box.add_widget(bt)
        return box

if __name__ == "__main__":
    Main().run()
