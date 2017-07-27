# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 13:12:00 2017

@author: M179100
"""

""" MAP using dictionary """
class Map:    
    def __init__(self):
        self.map={}
        self.len=0
        
    def isEmpty(self):
        return self.len==0
    
    def add_item(self,k,v):
        self.map[k]=v
        self.len+=1
    def del_item(self,k):
        self.map[k]=None
        self.len-=1
    def get_item(self,k):
        return self.map[k]
    def map_keys(self):
        return self.map.keys()
    def map_len(self):
        return self.len
    def map_print(self):
        for it in self.map.keys():
            print "key:",it, "value:",self.map[it]

m=Map()
m.isEmpty()
m.add_item("id1","Mark")
m.add_item("id2","Jay")
m.add_item("id3","Carl")
m.map_len()
m.del_item("id3")
m.map_len()
m.map_print()
