# -*- coding: utf-8 -*-
"""
Created on Tue May 02 18:22:52 2017

@author: jaycb
"""

def fib(start1,start2,length):
    seq=[start1,start2]
    for l in range(length):
        start1,start2= start2,start2+start1
        seq.append(start2)
    return seq

fib(2,3,10)    
    