# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 10:10:11 2016

@author: bandlmd2
"""
import pandas as pd
import numpy as np
from itertools import chain
import os
import math
import itertools
cwd = os.getcwd()
os.chdir("C:/Users/Jay/Desktop/CS 412/HW3")
with open("C:/Users/Jay/Desktop/CS 412/HW3/paper.txt") as dFile:     # reading topic file
        data = dFile.read().splitlines()
terms=[] 
words=[]       
for k in range(len(data)):
    terms.append(data[k].split('\t')[1])  

count_array=list([])

### Generating the dictionary
for x in range(len(terms)):
    words.append(terms[x].split(' '))
    for j in terms[x].split(" "):
          words.append(j)
vocab=list(chain.from_iterable(words))  
vocab=sorted(list(set(vocab)))
vocab=vocab[1:]   ## remove first non empty row

len(vocab)



### writing Vocab list to vocab.txt file

with open("vocab.txt", "w") as wFile:
    for i in range(len(vocab)):
        wFile.write(str(vocab[i])+ "\n") 
        

### Tokenize plain text by dictionary

for i in range (len(terms)) :
    tokens=list([])    
    #count=0
    strip_words=terms[i].split(" ")
    for j in range(len(strip_words)):
        for k in range(len(vocab)):    
            if strip_words[j]==vocab[k]:
                tokens.append([k])
    count_array.append(tokens)
           
len(count_array)
#count_array[0]

### sparse tokenized docs to title.txt
with open("title.txt", "w") as wFile:
    for i in range(len(count_array)):
        wordarr=np.array(count_array[i],dtype=str)
        arr=np.array(count_array[i],dtype=str)
        arr=np.unique(arr,return_counts=True)
        wordarr=' '.join([str(a) +':'+ str(b) for a,b in zip(arr[0],arr[1])])
        wFile.write(str(len(arr[0]))+" "+str(wordarr)+"\n")


### reading word-assignments.dat file 
with open("C:/Users/Jay/Desktop/CS 412/HW3/result/word-assignments.dat") as dataFile:
    data = dataFile.read().splitlines()

topic_0_np=list([])
topic_1_np=list([])
topic_2_np=list([])
topic_3_np=list([])
topic_4_np=list([])

for num in range(len(data)):
    line = data[num].split(" ")
    topic_0=list([])
    topic_1=list([])
    topic_2=list([])
    topic_3=list([])
    topic_4=list([])
    for i in range(len(line)-1):
        word=line[i+1].split(":")
        if word[1]=='00':
            topic_0.append(vocab[int(word[0])])
        elif word[1]=='01':
            topic_1.append(vocab[int(word[0])])
        elif word[1]=='02':
            topic_2.append(vocab[int(word[0])])
        elif word[1]=='03':
            topic_3.append(vocab[int(word[0])])
        elif word[1]=='04':
            topic_4.append(vocab[int(word[0])])
    topic_0_np.append(topic_0) 
    topic_1_np.append(topic_1)
    topic_2_np.append(topic_2)
    topic_3_np.append(topic_3)
    topic_4_np.append(topic_4)

os.chdir("C:/Users/Jay/Desktop/CS 412/HW3/bandlmd2_assign3")
### generating topic-i-txt files.    
with open("topic-0.txt", "w") as wFile:
    for i in range(len(topic_0_np)):
        if len(topic_0_np[i])>0:
            wFile.write(str(' '.join(topic_0_np[i]))+"\n") 
with open("topic-1.txt", "w") as wFile:
    for i in range(len(topic_1_np)):
        if len(topic_1_np[i])>0:
            wFile.write(str(' '.join(topic_1_np[i]))+"\n")            
with open("topic-2.txt", "w") as wFile:
    for i in range(len(topic_2_np)):
        if len(topic_2_np[i])>0:
            wFile.write(str(' '.join(topic_2_np[i]))+"\n")            
with open("topic-3.txt", "w") as wFile:
    for i in range(len(topic_3_np)):
        if len(topic_3_np[i])>0:
            wFile.write(str(' '.join(topic_3_np[i]))+"\n")
with open("topic-4.txt", "w") as wFile:
    for i in range(len(topic_4_np)):
        if len(topic_4_np[i])>0:
            wFile.write(str(' '.join(topic_4_np[i]))+"\n")
  