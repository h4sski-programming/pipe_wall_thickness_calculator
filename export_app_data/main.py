import json
from kivy.app import App
from kivy.metrics import dp

from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar


from settings import *
from dropdown_button import Dropdown_Button


class CalculationValues():
    def __init__(self) -> None:
        ## initial values, for debugging purpouse
        ## to be comment out when on production
        # self.material = '20MnNb6 1.0471'
        # self.dn = 25
        # self.calc_temp = 125
        # self.calc_pressure = 10.5
        # self.corrosion_allowance = 2
        # self.joint_coefficient = 1
        # ###
        # self.strenght_calc_temp = 1
        pass
    
    def get_strenght_calc_temp(self) -> float:
        material_dict = DB_JSON['materials'][self.material]['strenght_at_temp']
        
        # Initial values
        lower_temp = int(list(material_dict.keys())[0])
        strenght_lower_temp = list(material_dict.values())[0]
        for temp, strenght in material_dict.items():
            temp = int(temp)
            if self.calc_temp < temp:
                higher_temp = temp
                strenght_higher_temp = strenght
                break
            lower_temp = temp
            strenght_lower_temp = strenght
        
        temp_ratio = (self.calc_temp - lower_temp) / (higher_temp - lower_temp)
        strenght_delta = strenght_lower_temp - strenght_higher_temp
        return strenght_lower_temp - temp_ratio * strenght_delta
    
    
    def update_values(self, input) -> None:
        #### input values
        self.material = input.material.text
        self.dn = int(input.dn.text)
        # Do outer diameter [mm]
        self.od = DB_JSON['dn'][f'{self.dn}']['od']
        # en nominal wall thickness [mm]
        self.nominal_wall_thickness = float(input.wall_thickness.text)
        # tc calculation temperature [C]
        self.calc_temp = int(input.calc_temp.text)
        # pc calculation pressure [MPa]
        self.calc_pressure = float(input.calc_pressure.text)
        # c0 corrosion allowance [mm]
        self.corrosion_allowance = float(input.corrosion_allowance.text)
        # c2 thining allowance [mm]
        self.thining_allowance = float(input.thining_allowance.text)
        # z joint coefficient [-]
        self.joint_coefficient = DB_JSON['joint_coefficient'][f'{input.joint_coefficient.text}']
        
        #### calculeted values
        # Di inner diameter [mm]
        self.id = self.od - 2*self.nominal_wall_thickness
        # Rp [MPa]
        self.strenght_calc_temp = self.get_strenght_calc_temp()
        # f = Rp / 1.5 [MPa]
        self.reduced_strenght_calc_temp = self.strenght_calc_temp / 1.5
        # e = (pc * Do) / (2* f * z + pc) minimum required wall thickness [mm]
        self.min_required_thickness = (self.calc_pressure*self.od) / (2*self.reduced_strenght_calc_temp*self.joint_coefficient + self.calc_pressure)
        # c1 = min(12.5%*en, 0.4mm) [mm]
        self.allowance_c1 = min(0.4, self.nominal_wall_thickness*0.125)
        # ecalc = e + c0 + c1 + c2 calculated minimal wall thickness [mm]
        self.calculated_wall_thickness = self.min_required_thickness+self.corrosion_allowance+self.allowance_c1+self.thining_allowance
        
        # final output [bool]
        self.correct_thickness = self.calculated_wall_thickness <= self.nominal_wall_thickness
        
    #### Debug purpouse
    # def print_values(self) -> None:
    #     print(f'{self.material = }')
    #     print(f'{self.dn = }')
    #     print(f'{self.calc_temp = }')
    #     print(f'{self.calc_pressure = }')
    #     print(f'{self.corrosion_allowance = }')
    #     print(f'{self.joint_coefficient = }')



class InputWidget(GridLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='Material'))
        self.material = Dropdown_Button(DB_JSON['materials'].keys(), 'Select material')
        self.add_widget(self.material)
        
        self.add_widget(Label(text='DN'))
        self.dn = Dropdown_Button(DB_JSON['dn'].keys(), 'Select DN')
        self.add_widget(self.dn)
        
        self.add_widget(Label(text='Wall thickness en = [mm]', halign='left', strip=True))
        self.wall_thickness = Dropdown_Button(DB_JSON['walls'], 'Select wall thickness')
        self.add_widget(self.wall_thickness)
        
        self.add_widget(Label(text='Design temperature tc = [°C]'))
        self.calc_temp = TextInput(hint_text='type only INT value', input_filter='int', multiline=False, halign='center')
        self.add_widget(self.calc_temp)
        
        self.add_widget(Label(text='Design pressure pc = [MPa]'))
        self.calc_pressure = TextInput(hint_text='type value', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.calc_pressure)
        
        self.add_widget(Label(text='Corrosion allowance c0 = [mm]'))
        self.corrosion_allowance = TextInput(hint_text='type value', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.corrosion_allowance)
        
        self.add_widget(Label(text='Thining allowance c2 = [mm]'))
        self.thining_allowance = TextInput(hint_text='type value', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.thining_allowance)
        
        self.add_widget(Label(text='Joint coeficient z = [mm]'))
        self.joint_coefficient = Dropdown_Button(DB_JSON['joint_coefficient'].keys(), 'Select joint coefficient')
        self.add_widget(self.joint_coefficient)
    
    
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
        self.message.size_hint_x = 3
        self.message.color = MESSAGE_COLOR
        self.add_widget(self.message)
        
    
class OutputWidget(GridLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='OD [mm]'))
        self.od = Label(text='-')
        self.add_widget(self.od)
        
        self.add_widget(Label(text='ID [mm]'))
        self.id = Label(text='-')
        self.add_widget(self.id)
        
        self.add_widget(Label(text='Strenght at calc temp \nRp [Mpa]'))
        self.strenght_calc_temp = Label(text='-')
        self.add_widget(self.strenght_calc_temp)
        
        self.add_widget(Label(text='Reduced strenght at calc temp \nf = Rp / 1.5 [Mpa]'))
        self.reduced_strenght_calc_temp = Label(text='-')
        self.add_widget(self.reduced_strenght_calc_temp)
        
        self.add_widget(Label(text='Minimum required wall thickness \ne = (pc * Do) / (2* f * z + pc) [mm]'))
        self.min_required_thickness = Label(text='-')
        self.add_widget(self.min_required_thickness)
        
        self.add_widget(Label(text='Allowance c1 \nc1 = min(en * 12.5%, 0.4mm) [mm]'))
        self.allowance_c1 = Label(text='-')
        self.add_widget(self.allowance_c1)
        
        self.add_widget(Label(text='Calculated minimal wall thickness \necalc = e + c0 + c1 + c2 [mm]'))
        self.calculated_wall_thickness = Label(text='-')
        self.add_widget(self.calculated_wall_thickness)
        
        self.correct_thickness = Label(text='-', color=MESSAGE_COLOR)
        self.add_widget(self.correct_thickness)
        
        ## ProgressBar
        ## https://kivy.org/doc/stable/api-kivy.uix.progressbar.html
        self.pb_layout = BoxLayout(orientation='vertical')
        # self.pb_layout.size_hint_x = None
        # self.pb_layout.size[0] = dp(200)
        self.pb_layout.padding = dp(15), 0
        self.pb_label = Label(text='- / -')
        self.pb = ProgressBar(max=100, value=0)
        self.pb_layout.add_widget(self.pb_label)
        self.pb_layout.add_widget(self.pb)
        
        self.add_widget(self.pb_layout)
    
    
    def update(self, calc_val: CalculationValues) -> None:
        self.od.text = f'{calc_val.od:.2f}'
        self.id.text = f'{calc_val.id:.2f}'
        self.strenght_calc_temp.text = f'{calc_val.strenght_calc_temp:.2f}'
        self.reduced_strenght_calc_temp.text = f'{calc_val.reduced_strenght_calc_temp:.2f}'
        self.min_required_thickness.text = f'{calc_val.min_required_thickness:.2f}'
        self.allowance_c1.text = f'{calc_val.allowance_c1}'
        self.calculated_wall_thickness.text = f'{calc_val.calculated_wall_thickness:.4f}'
        if calc_val.correct_thickness:
            self.correct_thickness.color = MESSAGE_GREEN_COLOR
            self.pb_label.color = MESSAGE_GREEN_COLOR
            self.correct_thickness.text = 'Wall thicknes is correct'
        else:
            self.correct_thickness.color = MESSAGE_ERROR_COLOR
            self.pb_label.color = MESSAGE_ERROR_COLOR
            self.correct_thickness.text = 'Wall thicknes is NOT correct'
        
        calc_nominal_wall_ratio = calc_val.calculated_wall_thickness / calc_val.nominal_wall_thickness *100
        self.pb_label.text = f'{calc_val.calculated_wall_thickness:.2f} / {calc_val.nominal_wall_thickness:.2f} = {calc_nominal_wall_ratio:.2f}%'
        self.pb.value = calc_nominal_wall_ratio


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
        self.output.size_hint_y = 1.3
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
        if not new_temp or not (min_temp <= int(new_temp) <= max_temp):
            self.middle.message.color = MESSAGE_ERROR_COLOR
            self.middle.message.text = f'Incorrect temp value. For {new_material} range is {min_temp} ~ {max_temp}.'
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
        self.title = 'Pipe Wall Thickness Calculator || by h4sski'
        Window.size = (800, 800)
        Window.top = 100
        Window.left = 100
        main_layout = MainWidget()
        return main_layout
    
    
if __name__ == '__main__':
    calculator = CalculatorApp()
    calculator.run()
    # CalculatorApp().run()
    