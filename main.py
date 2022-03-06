from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from JSONconverter import
import os

Window.size = (1920, 1080)


Builder.load_file("converter.kv")

class MyLayout(Widget):
    pass

class ConverterApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    ConverterApp().run()
