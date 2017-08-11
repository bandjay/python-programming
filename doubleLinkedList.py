# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 11:07:09 2017

@author: Jay
"""



""" double linked list using sentinal nodes at the ends"""

class doubleLinkedList:
    
        """ Node class"""
        class _Node:
            __solts__= '_element','_prev','_next'
            def __init__(self,element,prev,next):
                self._element=element
                self._prev=prev
                self._next=next 
                
                
        def __init__(self):
             self._header=self._Node(None,None,None)
             self._trailer=self._Node(None,None,None)
             self._header._next=self._trailer
             self._trailer._prev=self._header
             self._size=0
             
        def __len__(self):
            return self._size
        
        def __isEmpty__(self):
            return self._size==0
        
        def __add_in__(self,e,predecessor,successor):
            new=self._Node(e,predecessor,successor)
            predecessor._next=new
            successor._prev=new
            self._size+=1
            return new
        def __del__(self,n):
            pre=n._prev
            suc=n._next
            pre._next=suc
            suc._prev=pre
            self._size-=1
            ele=n._element
            n._prev=n._next=n._element=None
            return ele
        
dll=doubleLinkedList()
dll.__len__()
dll.__isEmpty__()
