# -*- coding: utf-8 -*-
"""
Created on Fri Jun 02 12:31:01 2017

@author: M179100
"""

class linkedstack:
    
    """" Node class """
    class _Node:
        
        __slots__= '_element','_next'
        
        def __init__(self,element,next):
            self._element=element
            self._next=next
            
    """ stack functions """        
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def __isempty__(self):
        return self._size==0
    def __push__(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1
    def __pop__(self):
        
        if self.__isempty__():
            print "Stack is empty"
        else:
            popped=self._head._element
            self._head=self._head._next  
            self._size-=1
            return popped
        
        
""" Testing """
S=linkedstack()   
S.__isempty__()
S.__push__(5)
S.__len__()
S.__push__("A")
S.__push__(20.7)
S.__pop__()
S.__len__()
      