import math

from settings import *
from data_base import get_dict_from_values


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
    
    def get_aproximated_strenght_by_calc_temp(self, material_dict: dict, calc_temp: int) -> float:
        # Require ordered dictionary
        
        lower_temp: int = min([int(t) for t in material_dict.keys()])
        higher_temp: int = max([int(t) for t in material_dict.keys()])
        # lower_temp: int = int(min(material_dict.keys()))
        # higher_temp: int = int(max(material_dict.keys()))
        
        if calc_temp > higher_temp:
            return 0.
        
        lower_temp_strength: int
        higher_temp_strength: int
        
        for temp, strength in material_dict.items():
            temp_int = int(temp)
            if calc_temp <= temp_int < higher_temp and strength > 0:
                higher_temp = temp_int
            elif lower_temp < temp_int < calc_temp:
                lower_temp = temp_int
        lower_temp_strength = material_dict[f'{lower_temp}']
        higher_temp_strength = material_dict[f'{higher_temp}']
        
        if calc_temp == higher_temp:
            return higher_temp_strength
        
        temp_ratio: float = (calc_temp - lower_temp) / (higher_temp - lower_temp)
        strength_delta: int = lower_temp_strength - higher_temp_strength
        return lower_temp_strength - temp_ratio*strength_delta
    
    
    def update_values(self, input) -> None:
        #### input values
        self.material = input.material.text
        material_db_dict = DB_JSON['materials'][self.material]
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
        self.strenght_calc_temp = self.get_aproximated_strenght_by_calc_temp(material_db_dict['strenght_at_temp'], self.calc_temp)
        # f = max( Rp / 1.5, Rm / 2.4) [MPa]
        # print(f'{self.strenght_calc_temp / 1.5 = }')
        # print(f"{DB_JSON['materials'][self.material]['tensile_strength_Rm'] / 2.4 = }")
        self.reduced_strenght_calc_temp = min(self.strenght_calc_temp / 1.5, DB_JSON['materials'][self.material]['tensile_strength_Rm'] / 2.4)
        # Creep strength, based on EN 10216-2 Table A.1
        if self.material_have_creep_values(material_db_dict) and self.temp_in_creep_range(self.calc_temp, material_db_dict['creep_strength']['creep_temps']):
            # if material_db_dict['creep_strength']['creep_temps'][0] <= self.calc_temp <= material_db_dict['creep_strength']['creep_temps'][0]:
            creep_duration = DB_JSON['creep_durations'][input.creep_duration.text]
            creep_dict = get_dict_from_values(material_db_dict['creep_strength']['creep_temps'], material_db_dict['creep_strength'][creep_duration])
            self.creep_strength = self.get_aproximated_strenght_by_calc_temp(creep_dict, self.calc_temp)
            self.reduced_creep_strength = self.creep_strength/1.5
        else:
            self.creep_strength = 0
            self.reduced_creep_strength = 0
        # Final reduced strength value
        if self.reduced_creep_strength == 0:
            self.reduced_strenght = self.reduced_strenght_calc_temp
        elif self.reduced_strenght_calc_temp == 0:
            self.reduced_strenght = self.reduced_creep_strength
        else:
            self.reduced_strenght = min(self.reduced_creep_strength, self.reduced_strenght_calc_temp)
        
        # Minimum required wall thickness
        if self.od/self.id <= 1.7:
            # e = (pc * Do) / (2* f * z + pc) minimum required wall thickness [mm]
            self.min_required_thickness = (self.calc_pressure*self.od) / (2*self.reduced_strenght*self.joint_coefficient + self.calc_pressure)
        else:
            # e = Do/2 * ( 1- sqrt( (f*z-pc) / (f*z+pc) ) )
            self.min_required_thickness = self.od/2 * ( 1- math.sqrt( (self.reduced_strenght*self.joint_coefficient - self.calc_pressure) / (self.reduced_strenght*self.joint_coefficient + self.calc_pressure) ) )
        # c1 = min(12.5%*en, 0.4mm) [mm]
        self.allowance_c1 = max(0.4, self.nominal_wall_thickness*0.125)
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
    
    def material_have_creep_values(self, material_db_dict: dict) -> bool:
        return 'creep_strength' in material_db_dict.keys()
    
    def temp_in_creep_range(self, calc_temp: int, creep_temps: list) -> bool:
        print(f'{min(creep_temps) = }')
        print(f'{max(creep_temps) = }')
        print(f'{calc_temp = }')
        return min(creep_temps) <= calc_temp <= max(creep_temps)

