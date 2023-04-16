
###Author: [Naufil Bin Imran]
###Assignment / Part: HW10 - Q1 
###Date due: 2022-04-28
##I pledge that I have completed this assignment without
##collaborating with anyone else, in conformance with the
##NYU School of Engineering Policies and Procedures on
##Academic Misconduct.

import random

class Weapon:
    def __init__(self, weapon_name, strength):
        self.weapon_name= weapon_name
        self.strength= strength
    def __str__(self):
        final_string = ("'{}' Weapon object (strength:{}) ".format(self.weapon_name,self.strength))
        return final_string
    def does_break(self):
        random_strength= random.random()
        if random_strength < 0.5* self.strength:
            return True
        return False



