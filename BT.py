# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 14:30:26 2017

@author: M179100
"""
""" Tree Node """
class Node:
    def __init__(self,val):
        self.l=None
        self.r=None
        self.v=val

class BT:  
    
    def __init__(self):
        self.root=None
    
    def getroot(self):
        return self.root
    
    def add(self,val):
        if self.root==None:
            self.root= Node(val)
        else:
            self._add(val,self.root)
    
    def _add(self,val,node):
        if val<node.v :
            if node.l!=None:
                self._add(val,node.l)
            else:
                node.l=Node(val)
        else :
            if node.r!=None:
                self._add(val,node.r)
            else:
                node.r=Node(val)
                
    def find(self,val):        
        if self.root!=None :
            self._find(val,self.root)
        else:
            return None
    
    def _find(self,val,node):
        if val==node.v:
            return node.v
        elif  val<node.v and node.l!=None:
            self._find(val,node.l)
        elif  val>node.v and node.r!=None:
            self._find(val,node.r)
    
    def deltree(self):
        self.root=None
        
    def printtree(self):
        if self.root!=None:
            self._printtree(self.root)
        else:
            print "tree is empty"
    def _printtree(self,node):
        if node!=None:
            self._printtree(node.l)
            print str(node.v)+ "   "
            self._printtree(node.r)
            
    def depth(self,node):
        current_depth = 0
        if node.l!=None:
            current_depth = max(current_depth, self.depth(node.l))
        if node.r!=None:
            current_depth = max(current_depth, self.depth(node.r))
        return current_depth + 1
    
    def leftmost(self,node):
        if node.l!=None:
            self.leftmost(node.l)
        else :
            print node.v  
            
    def rightmost(self,node):
        if node.r!=None:
            self.rightmost(node.r)
        else :
            print node.v 

    
    
bt=BT()
bt.add(2)
bt.add(3)
bt.add(1)
bt.add(6)
bt.add(10)
bt.add(0)
bt.add(-5)
bt.add(12) 
bt.printtree()   
print bt.getroot().v  
bt.depth(bt.getroot())
bt.leftmost(bt.getroot())
bt.rightmost(bt.getroot())
