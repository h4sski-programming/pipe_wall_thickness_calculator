from kivy.app import App

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

from settings import *
from input_widget import InputWidget
from middle_widget import MiddleWidget
from output_widget import OutputWidget
from calculation_values import CalculationValues


class MainWidget(BoxLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        # self.padding = dp(10), dp(5)
        self.calc_val = CalculationValues()
        # self.size_hint_y = None
        
        #### Input
        self.input = InputWidget()
        # self.input.size_hint_y = 1
        # self.input.size_hint_y = None
        # self.input.size = (1, dp(300))
        # self.input.height = dp(300)
        self.input_title = Button(text='Input')
        self.input_title.size_hint = TITLE_LABEL_SIZE_HINT
        self.input_title.size = TITLE_LABEL_SIZE
        self.input_title.background_color = TITLE_LABEL_BG_COLOR
        self.add_widget(self.input_title)
        self.add_widget(self.input)
        
        #### Middle
        self.middle = MiddleWidget(main_widget=self)
        self.middle.size_hint_y = 0.25
        # self.middle.size_hint_y = None
        # self.middle.height = dp(80)
        self.add_widget(self.middle)
        
        #### Output
        self.output = OutputWidget()
        self.output.size_hint_y = 1.4
        # self.output.size_hint = (1, None)
        # self.output.height = dp(300)
        self.output_title = Button(text='Output')
        self.output_title.size_hint = TITLE_LABEL_SIZE_HINT
        self.output_title.size = TITLE_LABEL_SIZE
        self.output_title.background_color = TITLE_LABEL_BG_COLOR
        self.add_widget(self.output_title)
        self.add_widget(self.output)
        
    def get_temp_range_for_material(self, material: str) -> list[int]:
        material_db = DB_JSON['materials'][material]['strenght_at_temp']
        min_temp = min(int(i) for i in material_db.keys() if int(i)>0)
        max_temp = max(int(i) for i in material_db.keys() if material_db[i]>0)
        return [min_temp, max_temp]
    
    def valid_input(self, input: InputWidget) -> bool:
        new_material = input.material.text
        if not new_material in DB_JSON['materials'].keys():
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = 'You must select Material from the list'
            return False
        
        new_dn = input.dn.text
        if not new_dn in DB_JSON['dn'].keys() or new_dn == 'Select DN':
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = 'You must select DN from the list'
            return False
        
        new_wall_thickness = input.wall_thickness.text
        if new_wall_thickness == 'Select wall thickness':
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = 'You must select Wall thickness from the list'
            return False
        if not float(new_wall_thickness) in list(DB_JSON['walls']):
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = 'You must select Wall thickness from the list'
            return False
        
        new_temp = input.calc_temp.text
        min_temp, max_temp = self.get_temp_range_for_material(new_material)
        if not new_temp:
        # if not new_temp or not (min_temp <= int(new_temp) <= max_temp):
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'Incorrect temperature value.'
            # self.middle.message.text = f'Incorrect temp value. For {new_material} range is {min_temp} ~ {max_temp}.'
            return False
        
        new_pressure = input.calc_pressure.text
        if not new_pressure or not float(new_pressure)>0:
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'Incorrect pressure value, it must be positive.'
            return False
        
        new_corrosion_allowance = input.corrosion_allowance.text
        if not new_corrosion_allowance or not float(new_corrosion_allowance)>=0:
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'Incorrect corrosion allowance value, it must be positive.'
            return False
        
        new_thining_allowance = input.thining_allowance.text
        if not new_thining_allowance or not float(new_thining_allowance)>=0:
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'Incorrect thining allowance value, it must be positive.'
            return False
        
        new_joint_coefficient = input.joint_coefficient.text
        if not new_joint_coefficient in DB_JSON['joint_coefficient'].keys():
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'You must select Joint coefficient from the list.'
            return False
        
        new_creep_duration = input.creep_duration.text
        if not new_creep_duration in DB_JSON['creep_durations'].keys():
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'You must select Creep duration from the list.'
            return False
        
        return True
    
        
    def calculate_values(self, btn) -> None:
        if self.valid_input(self.input):
            # Reset message label to the default values
            self.middle.message.color = MESSAGE_COLOR
            self.middle.message.text = 'Press Calculate button to perform calculation'
            
            self.calc_val.update_values(self.input)
            self.output.update(self.calc_val)


class CalculatorApp(App):
    def build(self):
        self.title = 'Pipe Wall Thickness Calculator @ EN 13480-3 || Coded by h4sski'
        Window.size = (800, 700)
        Window.top = 50
        Window.left = 50
        main_layout = MainWidget()
        return main_layout
    
    
if __name__ == '__main__':
    calculator = CalculatorApp()
    calculator.run()
    # CalculatorApp().run()
    