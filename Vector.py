# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 15:29:47 2017

@author: jaycb
"""

"""
Vector class for mutlti dimensional support
"""
class Vector:
    def __init__(self,v):
        self._vec=v
    def __len__(self):
        return len(self._vec)
    def __str__(self):
        return "<"+str(",".join(self._vec))+">"
    def __eq__(self,other):
        return self._vec==other
    def __add__(self,other):
        if (len(self._vec)!=len(other)):
            raise ValueError("Dimesions are not equal")
        return [a+b for a,b in zip(self._vec,other)] 
    def __mul__(self,other):
        if (len(self._vec)!=len(other)):
            raise ValueError("Dimesions are not equal")
        return [a*b for a,b in zip(self._vec,other)] 
    def __getitem__(self,i):
        return self._vec[i]
    def __setitem__(self,j,val):
        self._vec[j]=val
    
v1=Vector([1,2,3,4,5])
v2=Vector([1,2,3,4,5])
v1==v2
v1*v2
    
