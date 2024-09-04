from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label

from settings import *
    
class MiddleWidget(BoxLayout):
    def __init__(self, main_widget, **kwargs) -> None:
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        # self.orientation = 'vertical'
        self.padding = (0, dp(5))
        
        self.calculate_btn = Button(text='Calculate')
        # self.calculate_btn.size_hint_x = 0.5
        self.calculate_btn.background_color = (0.4, 1, 0.4, 1)
        self.calculate_btn.bind(on_release=main_widget.calculate_values)
        self.add_widget(self.calculate_btn)
        
        self.message = Label(text='Press Calculate button to perform calculation')
        self.message.size_hint_x = 4
        self.message.color = MESSAGE_COLOR
        self.add_widget(self.message)
        