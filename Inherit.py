# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 12:25:29 2017

@author: jaycb
"""

class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def __display__(self):
        print("MODEL:",self.model)

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        super(ElectricCar, self).__init__(model, color, mpg)
        
        

car = ElectricCar('battery', 'ford', 'golden', 10)
car.__display__()