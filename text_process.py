# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:39:20 2017

@author: M179100
"""

""" 
program to process text 
it does the following by default
1. Special char removal
2. Case conversion
3. number of lines
4. POS tagging
"""

import re

class textprocess:
    
    def __init__(self,filename):
        self.fileip=filename
        self.numlines=0
        
    def clean_text(self):
        opfile=open(self.fileip)
        file_to_read=opfile.readlines()
        self.numlines=len(file_to_read)
        self.clean_lines=[]
        self.all_words=[]
        self.counts=[]
        for line in file_to_read:
            words=line.split(" ")
            clean_words=[]
            for w in words:
                cl_word=re.sub(r'[^a-zA-Z0-9. ]',"",w)
                clean_words.append(cl_word)
                self.all_words.append(cl_word)
            self.clean_lines.append(' '.join(clean_words))
        self.write_to_file()
    
    def write_to_file(self):
        with open(self.fileip+str("clean"),'w') as wfile:
            for cl in self.clean_lines:
                wfile.write(cl+"\n")
                
    def wc_print(self):
        uniq_word=list(set(self.all_words))
        print "word \t","count"
        for u in uniq_word:            
            print u,"\t",self.all_words.count(u)
    
        
                
tp=textprocess("text.txt")
tp.clean_text()
tp.wc_print()
            
    
        
      