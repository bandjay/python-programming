# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 11:54:05 2016

@author: Jay
"""
import pandas as pd
import numpy as np
from itertools import chain
import os
import math
import itertools
cwd = os.getcwd()
os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/patterns")


vocab=[]
with open("C:/Users/Jay/Desktop/CS 412/HW3/vocab.txt") as dataFile:
         data = dataFile.read().splitlines() 
for i in range(len(data)):
    vocab.append(data[i])

###############################################################################
############ purity calculation and re-ranking    #############################
###############################################################################

for ab in range(5):
    with open("C:/Users/Jay/Desktop/CS 412/HW3/result/word-assignments.dat") as dataFile:
        data = dataFile.read().splitlines()

    topic_0_np_w=list([])
    topic_1_np_w=list([])
    topic_2_np_w=list([])
    topic_3_np_w=list([])
    #topic_4_np=list([])
    fl=['00','01','02','03','04']
    fl=np.delete(fl,str("0"+str(ab)))
    print(fl)
    for num in range(len(data)):
        line = data[num].split(" ")
        topic_0_w=list([])
        topic_1_w=list([])
        topic_2_w=list([])
        topic_3_w=list([])
        #topic_4=list([])
        for i in range(len(line)-1):
            word=line[i+1].split(":")
            if word[1]==str("0"+str(ab)) or word[1]==fl[0]:
                topic_0_w.append(vocab[int(word[0])])
            if word[1]==str("0"+str(ab)) or word[1]==fl[1]:
                topic_1_w.append(vocab[int(word[0])])
            if word[1]==str("0"+str(ab)) or word[1]==fl[2]:
                topic_2_w.append(vocab[int(word[0])])
            if word[1]==str("0"+str(ab)) or word[1]==fl[3]:
                topic_3_w.append(vocab[int(word[0])])
        #elif word[1]=='04':
        #    topic_4.append(vocab[int(word[0])])
        topic_0_np_w.append(topic_0_w) 
        topic_1_np_w.append(topic_1_w)
        topic_2_np_w.append(topic_2_w)
        topic_3_np_w.append(topic_3_w)
        #topic_4_np.append(topic_4)
    topic_c1=np.unique(topic_0_np_w)
    topic_c2=np.unique(topic_1_np_w)
    topic_c3=np.unique(topic_2_np_w)
    topic_c4=np.unique(topic_3_np_w)
    with open(str("pattern-"+str(ab)+".txt.phrase")) as dataFile:
        data = dataFile.read().splitlines()
    
        sup_t=[] 
        sup_tr=[]
        tran_t=[] 
        for num in range(len(data)):
            line = data[num].replace ("[", "").replace("]","").split(" ")
            sup_t.append(line[0])
            tran_t.append(line[1:len(line)])
        for x in tran_t:
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            for line in topic_c1:
                #line = line.split(" ")
                if all((w in line for w in x)):
                    count1 = count1 + 1
            sup1=count1/len(topic_c1)    
            for line in topic_c2:
                #line = line.strip().split(" ")
                if all((w in line for w in x)):
                    count2 = count2 + 1
            sup2=count2/len(topic_c2)
            for line in topic_c3:
                #line = line.strip().split(" ")
                if all((w in line for w in x)):
                    count3 = count3 + 1
            sup3=count3/len(topic_c3)        
            for line in topic_c4:
                #line = line.strip().split(" ")
                if all((w in line for w in x)):
                    count4 = count4 + 1  
            sup4=count4/len(topic_c4)
            sup_tr.append(max(sup1,sup2,sup3,sup4))
        
        purity=[]
        for i in range(len(sup_t)):    
            purity.append(math.log(float(sup_t[i]),2)-math.log(float(sup_tr[i]),2)) 
        pur_sup=[]  
        supt=np.array(sup_t,dtype=float)
        for p in range(len(sup_t)):
            norm_p=(purity[p]-np.amin(purity))/(np.amax(purity)-np.amin(purity))
            norm_s=(supt[p]-np.amin(supt))/(np.amax(supt)-np.amin(supt))
            pur_sup.append((norm_p+norm_s)/2)
            
           
        #pattern_df=pd.DataFrame.from_records(freq)
        pattern_df=pd.DataFrame(columns=('pur_sup','pattern'))
        pattern_df['pur_sup']=pur_sup
        pattern_df['pattern']=tran_t
        pattern_df = pattern_df.sort_values(by='pur_sup', ascending=0)
        terms=np.array(pattern_df['pattern'])
        pur_sup=np.array(pattern_df['pur_sup'])
        
        topic_array=[]
        for i in range (pattern_df.shape[0]) :
            tokens=[]    
            #count=0
            strip_words=terms[i]
            for j in range(len(strip_words)):
                for k in range(len(vocab)):    
                    if strip_words[j]==vocab[k]:
                        tokens.append(k)
            topic_array.append(tokens)
           
        len(topic_array)
        os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/purity")
        with open(str("purity-"+str(ab)+".txt.phrase"), "w") as wFile:
            for i in range(len(terms)):
                wordarr=np.array(terms[i],dtype=str)
                wordarr=str(' '.join(wordarr))
                wFile.write(str(pur_sup[i])+" "+"["+str(wordarr)+"]"+"\n")
        with open(str("purity-"+str(ab)+".txt"), "w") as wFile:
            for i in range(len(topic_array)):
                wordarr=np.array(topic_array[i],dtype=str)
                wordarr=str(' '.join(wordarr))
                wFile.write(str(pur_sup[i])+" "+"["+str(wordarr)+"]"+"\n")
        os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/patterns")
