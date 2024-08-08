import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label


class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
      super().__init__(**kwargs)
      button = Button(text='Calculate')
      self.add_widget(button)

class CalculatorApp(App):
    def build(self):
        return MainWidget()

class FirstKivyApp(App):
    def build(self):
        return MainWidget()
    
if __name__ == '__main__':
    calculator = CalculatorApp()
    calculator.run()
    # CalculatorApp().run()
    # FirstKivyApp().run()