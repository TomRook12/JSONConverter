from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("converter.kv")

class MyLayout(Widget):
    pass

class ConverterApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    ConverterApp().run()

#https://www.youtube.com/watch?v=YlRd4rw_vBw&ab_channel=Codemy.com