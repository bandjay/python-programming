# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:50:20 2016

@author: Jay
"""

import pandas as pd
import numpy as np
from itertools import chain
import os
import math
import itertools
cwd = os.getcwd()
os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3")

########################################
###### Apriori algorithm ###############
########################################
vocab=[]
with open("C:/Users/Jay/Desktop/CS 412/HW3/vocab.txt") as dataFile:
         data = dataFile.read().splitlines() 
for i in range(len(data)):
    vocab.append(data[i])

## Run this step five times to generate freq_patt patterns for 5 topic files  

for ab in range(5):
    print(ab)          

    with open(str("topic-"+str(ab)+".txt")) as dFile:     # reading topic file
        data = dFile.read().splitlines()

    min = len(data)*0.01                  # defining min support for patterns

# generating 1-itemset freq_pattuent patterns.
    word_dic = {}
    vocabData = []
    for line in data:
        vocabLine = []
        line = line.strip().split(" ")
        for z in line:
            z = z.strip()
            vocabLine.append(z)
            if z in word_dic:
                word_dic[z] += 1
            else:
                word_dic[z] = 1
                vocabData.append(vocabLine)
                    
    vocab_topic=list(chain.from_iterable(vocabData))    
    vocab_topic=sorted(list(set(vocab_topic)))  
    len(vocab_topic)        
    word_dic = {k:v for k, v in word_dic.items() if v >= min}
                    
    # obtaining 1 itemset with support
    freq_patt=[]                          # defining freq_patt pattern array
    
    l=list(itertools.combinations(word_dic.keys(),1))
    l1 = []
    l1_sup=[]

    for x in l:
        count=0
        for line in data:
            line = line.strip().split(" ")
            if all((w in line for w in x)):
                count=count+1
        if count>min:
            l1.append(sorted(x))
            l1_sup.append((count,sorted(x)))
    freq_patt=freq_patt+l1_sup
    present=l1
    k=2
    while(present):
        comb_self=np.union1d(present,present)
        l2=[]
        l2_sup=[]
        #for c3 in c2:
        l = list(itertools.combinations(comb_self,k ))
        for x in l:
            count = 0
            for line in data:
                line = line.strip().split(" ")
                if all((w in line for w in x)):
                    count = count + 1
            if count > min:
                l2.append(sorted(x))
                l2_sup.append((count,sorted(x)))
        present=l2
        freq_patt=freq_patt+l2_sup
        k=k+1


    pattern_df=pd.DataFrame.from_records(freq_patt)
    pattern_df.columns=['count','pattern']
    pattern_df = pattern_df.sort_values(by='count', ascending=0)
    terms=np.array(pattern_df['pattern'])
    counts=np.array(pattern_df['count'])

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
    os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/patterns")
# wiriting to pattern-i.txt file
    with open(str("pattern-"+str(ab)+".txt.phrase"), "w") as wFile:
        for i in range(len(terms)):
            wordarr=np.array(terms[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n")
    with open(str("pattern-"+str(ab)+".txt"), "w") as wFile:
        for i in range(len(topic_array)):
            wordarr=np.array(topic_array[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n")
        
    pattern_df=pd.DataFrame.from_records(freq_patt)
    pattern_df.columns=['count','pattern']
    pattern_df = pattern_df.sort_values(by='count', ascending=0)
    terms=np.asarray(pattern_df['pattern'])
    counts=np.asarray(pattern_df['count'])
    
    
##########################################################
# finding max and closed patterns  #######################
##########################################################

    

    close_patt = []
    max_patt = []

    for i in range(len(terms)):
        isClosed = True
        isMax = True
        for j in range(len(terms)):
            if i != j:
                if set(terms[i]).issubset(set(terms[j])) and counts[j] >= counts[i]:
                    isClosed = False
                    break
        for j in range(len(freq_patt)):
            if i != j:
                if set(terms[i]).issubset(set(terms[j])):
                    isMax = False
        if isClosed:
            close_patt.append([counts[i], terms[i]])
        if isMax:
            max_patt.append([counts[i], terms[i]])

    close_patt = [list(i) for i in close_patt]
    max_patt = [list(i) for i in max_patt]


    # wiritng to closed-i.txt file

    topic_array=[]
    counts=[]
    for i in range (len(close_patt)) :
        tokens=[] 
        counts.append(close_patt[i][0])
    #count=0
        strip_words=close_patt[i][1]
        for j in range(len(strip_words)):
            for k in range(len(vocab)):    
                if strip_words[j]==vocab[k]:
                    tokens.append(k)
        topic_array.append(tokens)
    
           
    len(topic_array)
    #len(counts)
    pattern_df=pd.DataFrame.from_records(close_patt)
    pattern_df.columns=['count','pattern']
    pattern_df = pattern_df.sort_values(by='count', ascending=0)
    terms=np.asarray(pattern_df['pattern'])
    counts=np.asarray(pattern_df['count'])
    os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/closed")
    with open(str("closed-"+str(ab)+".txt.phrase"), "w") as wFile:
        for i in range(len(terms)):
            wordarr=np.array(terms[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n")
    with open(str("closed-"+str(ab)+".txt"), "w") as wFile:
        for i in range(len(topic_array)):
            wordarr=np.array(topic_array[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n")    
        
    # writing to max-i.txt file        
        
    topic_array=[]
    counts=[]
    for i in range (len(max_patt)) :
        tokens=[] 
        counts.append(max_patt[i][0])
        #count=0
        strip_words=max_patt[i][1]
        for j in range(len(strip_words)):
            for k in range(len(vocab_topic)):    
                if strip_words[j]==vocab_topic[k]:
                    tokens.append(k)
        topic_array.append(tokens)
    
           
   #len(counts)
    pattern_df=pd.DataFrame.from_records(max_patt)
    pattern_df.columns=['count','pattern']
    pattern_df = pattern_df.sort_values(by='count', ascending=0)
    terms=np.asarray(pattern_df['pattern'])
    counts=np.asarray(pattern_df['count'])
    os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3/max")
# wiriting to pattern-i.txt file
    with open(str("max-"+str(ab)+".txt.phrase"), "w") as wFile:
        for i in range(len(terms)):
            wordarr=np.array(terms[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n")
    with open(str("max-"+str(ab)+".txt"), "w") as wFile:
        for i in range(len(topic_array)):
            wordarr=np.array(topic_array[i],dtype=str)
            wordarr=str(' '.join(wordarr))
            wFile.write(str(counts[i]/len(data))+" "+"["+str(wordarr)+"]"+"\n") 
    os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3")
