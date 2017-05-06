# -*- coding: utf-8 -*-
"""
Created on Tue May 02 00:55:48 2017

@author: jaycb
"""

def binary_search(data,target,low,high):
    #low=data[0]
    #high=data[-1]
    mid=(high+low)//2
    if data[mid]==target:
        return "Found"
    elif data[mid]>target:z
        high=mid-1
        return binary_search(data,target,low,mid-1)
    else :
        return binary_search(data, target, mid + 1, high)
    

    
binary_search([1,2,3,4,5],5,0,4)