# -*- coding: utf-8 -*-
"""
Created on Mon May 01 22:34:21 2017

@author: jaycb
"""

class Progression(object):
    def __init__(self,start=0):
        self.current=start
    def __advance__(self):
        self.current+=1
    def next(self):
        if self.current is None:
            raise StopIteration()
        else:
            val=self.current
            self.__advance__()
            return val
    def __iter__(self):
        return self
    def print_Pro(self,length):
        print(' '.join(str(next(self)) for i in range(length)))
        
Progression(5).print_Pro(4)  

class Geom(Progression):
    def __init__(self,start=0,base=1):
        super(Geom,self).__init__(start)
        self.base=base
    def __advance__(self):
        self.current=self.current*self.base   
class Power(Progression):
    def __init__(self,start=0,power=1):
        super(Power,self).__init__(start)
        self.power=power
    def __advance__(self):
        self.current=self.current**self.power  
        
Power(5,2).print_Pro(6)      
    