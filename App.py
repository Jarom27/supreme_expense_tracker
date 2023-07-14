from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
from database.CategoryHelper import *
Builder.load_file("./views/app.kv")


class RootWidget(TabbedPanel):
    pass
class MyApp(App):
    def build(self):
        Window.set_title("Supreme Expense Tracker")
        Window.clearcolor = (13/255,2/255,33/255,1)
        return RootWidget()

def main():
    MyApp().run()

if __name__ == "__main__":
    main()