from kivy.uix.gridlayout import GridLayout

from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from settings import *
from dropdown_button import Dropdown_Button


class InputWidget(GridLayout):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.cols = 2
        
        self.add_widget(Label(text='Material'))
        list_of_choises = list(DB_JSON['materials'].keys())
        self.material = Dropdown_Button(list_of_choises, 'Select material')
        self.add_widget(self.material)
        
        self.add_widget(Label(text='DN'))
        list_of_choises = list(DB_JSON['dn'].keys())
        self.dn = Dropdown_Button(list_of_choises, 'Select DN')
        self.add_widget(self.dn)
        
        self.add_widget(Label(text='Wall thickness en = [mm]', halign='left', strip=True))
        list_of_choises = list(DB_JSON['walls'])
        self.wall_thickness = Dropdown_Button(list_of_choises, 'Select wall thickness')
        self.add_widget(self.wall_thickness)
        
        self.add_widget(Label(text='Design temperature tc = [°C]'))
        self.calc_temp = TextInput(hint_text='type only INT value', text='100', input_filter='int', multiline=False, halign='center')
        self.add_widget(self.calc_temp)
        
        self.add_widget(Label(text='Design pressure pc = [MPa]'))
        self.calc_pressure = TextInput(hint_text='type value', text='2.4', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.calc_pressure)
        
        self.add_widget(Label(text='Corrosion allowance c0 = [mm]'))
        self.corrosion_allowance = TextInput(hint_text='type value', text='2', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.corrosion_allowance)
        
        self.add_widget(Label(text='Thining allowance c2 = [mm]'))
        self.thining_allowance = TextInput(hint_text='type value', text='0', input_filter='float', multiline=False, halign='center')
        self.add_widget(self.thining_allowance)
        
        self.add_widget(Label(text='Joint coeficient z = [mm]'))
        list_of_choises = list(DB_JSON['joint_coefficient'].keys())
        self.joint_coefficient = Dropdown_Button(list_of_choises, 'Select joint coefficient')
        self.add_widget(self.joint_coefficient)
        
        self.add_widget(Label(text='Creep duration [H]'))
        list_of_choises = list(DB_JSON['creep_durations'].keys())
        self.creep_duration = Dropdown_Button(list_of_choises, 'Select creep duration')
        self.add_widget(self.creep_duration)
    