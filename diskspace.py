# -*- coding: utf-8 -*-
"""
Created on Tue May 02 18:02:34 2017

@author: jaycb
"""

import os

def diskspace(path):
    total=os.path.getsize(path)
    if os.path.isdir(path):
        for filen in os.listdir(path):
            child = os.path.join(path,filen)
            total += diskspace(child)
    print(path)
    return total

diskspace("C:/CS512/data/KBP16/")        