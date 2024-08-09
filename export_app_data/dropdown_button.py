from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class Dropdown_Button(Button):
    def __init__(self, list_of_choises: list, btn_text:str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.text = btn_text
        self.dropdown_btn = DropDown()
        for choise in list_of_choises:
            btn = Button(text=str(choise), size_hint=(1, None), size=(1, dp(22)))
            # btn = Button(text=str(choise), size_hint=(None, None), size=(dp(400), dp(22)))
            btn.bind(on_release=lambda btn: self.dropdown_btn.select(btn.text))
            self.dropdown_btn.add_widget(btn)
        self.bind(on_release=self.dropdown_btn.open)
        self.dropdown_btn.bind(on_select=lambda instance, x: setattr(self, 'text', x))
