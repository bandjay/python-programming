# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 10:50:57 2017

@author: M179100
"""
from heapq import *
class priQ:  
    def __init__(self):
        self.heap=[]
        self.__len__=0
        
    def isEmpty(self):
        return self.__len__==0
    
    def add_val(self,inset):
        heappush(heap,inset)
        self.__len__+=1
        
    def get_top(self):        
        self.__len__-=1
        return heappop(heap)
    
    def get_len(self):
        return self.__len__
        
pq=priQ()   
pq.add_val((10,"task1"))  
pq.add_val((5,"task2")) 
pq.add_val((1,"task9"))
pq.add_val((3,"task10"))   
pq.get_len()
pq.get_top()
pq.get_top()
pq.get_len()
        
        
        
        
        
