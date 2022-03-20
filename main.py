from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.lang import Builder

import os

Window.size = (1920, 1080)

class OpenDialog(FloatLayout):
    export = ObjectProperty(None)
    cancel = ObjectProperty(None)


class ExportDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    openfile = ObjectProperty(None)
    exportfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def show_open(self):
        content = OpenDialog(open=self.open, cancel = self.dismiss_popup)
        self._popup(title="Open File", content=content,
                    size_hint=(0.9, 0.9))

    def show_export(self):
        content = ExportDialog(export=self.export, cancel=self.dismiss_popup)
        self._popup = popup(title="Export File", content=content,
                            size_hint=(0.9,0.9))


class ConverterApp(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('OpenDialog', cls=OpenDialog)
Factory.register('ExportDialog', cls=ExportDialog)

if __name__ == "__main__":
    ConverterApp().run()

