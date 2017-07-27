# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:34:54 2017

@author: M179100
"""

class TTT:
    def __init__(self):
        self._grid=[["-"]*3 for i in range(3)]
            
    def __disp__(self):
        for l in range(3):
            print ' '.join(self._grid[l])
    
    def __isEmpty__(self,pos):
        if self._grid[pos[0]][pos[1]]=='-':
            return True
        else:
            return False
    def __isover__(self):
        if self._grid[0][0]==self._grid[1][1]==self._grid[2][2] and self._grid[0][0]!='-':
            return True
        else :
            return False
    def __play__(self,sym,pos):
        
        if sym=='X':
            print "X started game"
        else:
            print"O started game"
        if self.__isEmpty__(pos):    
            self._grid[pos[0]][pos[1]]=sym
            self.__disp__() 
        else :
            print "cell is not empty, choose another"
        if self.__isover__():
            print "Game over",sym,"wins"

g=TTT()  
print "Game Begins"
print " Choose Symbols X/O and enter the pos in 3*3 grid"
print " follow this format : ['X' ,[0,1]]"          
for i in range(9):
    ip=input() 
    g.__play__(ip[0],ip[1]) 
    if g.__isover__():
        break
                 
        
        
        
    
        