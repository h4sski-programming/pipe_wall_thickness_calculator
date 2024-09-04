from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp

from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

from settings import *
from calculation_values import CalculationValues


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
        
        self.add_widget(Label(text='Strenght at calc temp \nR_p [Mpa]'))
        self.strenght_calc_temp = Label(text='-')
        self.add_widget(self.strenght_calc_temp)
        
        self.add_widget(Label(text='Reduced strenght at calc temp \nf_str = max( R_p/1.5, R_m/2.4 ) [Mpa]'))
        self.reduced_strenght_calc_temp = Label(text='-')
        self.add_widget(self.reduced_strenght_calc_temp)
        
        self.add_widget(Label(text='Creep strenght at calc temp \nS_RTt [Mpa]'))
        self.creep_strenght_calc_temp = Label(text='-')
        self.add_widget(self.creep_strenght_calc_temp)
        
        self.add_widget(Label(text='Reduced creep strenght at calc temp \nf_cr = S_RTt/1.5 [Mpa]'))
        self.reduced_creep_strenght_calc_temp = Label(text='-')
        self.add_widget(self.reduced_creep_strenght_calc_temp)
        
        self.add_widget(Label(text='Final reduced strenght\nf = min( f_str , f_cr ) [Mpa]'))
        self.final_reduced_strength = Label(text='-')
        self.add_widget(self.final_reduced_strength)
        
        self.add_widget(Label(text='Minimum required wall thickness \ne = (pc * D_o) / (2* f * z + p_c) [mm]'))
        self.min_required_thickness = Label(text='-')
        self.add_widget(self.min_required_thickness)
        
        self.add_widget(Label(text='Allowance c1 \nc1 = max(en * 12.5%, 0.4mm) [mm]'))
        self.allowance_c1 = Label(text='-')
        self.add_widget(self.allowance_c1)
        
        self.add_widget(Label(text='Calculated minimal wall thickness \ne_calc = e + c_0 + c_1 + c_2 [mm]'))
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
        self.creep_strenght_calc_temp.text = f'{calc_val.creep_strength:.2f}'
        self.reduced_creep_strenght_calc_temp.text = f'{calc_val.reduced_creep_strength:.2f}'
        self.final_reduced_strength.text = f'{calc_val.reduced_strenght:.2f}'
        self.min_required_thickness.text = f'{calc_val.min_required_thickness:.4f}'
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
        