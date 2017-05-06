# -*- coding: utf-8 -*-
"""
Created on Tue May 02 18:47:41 2017

@author: jaycb
"""

def Power(x,n):
    if (n==0):
        return 1
    else:
        partial=Power(x,n//2)
        result=partial*partial
        if n%2==1:
            result*=x
        
        return result   

Power(3,3)    
        