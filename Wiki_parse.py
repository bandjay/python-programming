# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 02:34:13 2016

@author: Jay
"""

import pandas as pd
import numpy as np
import re
from itertools import chain
import os
import math
import itertools
from nltk.corpus import stopwords

cwd = os.getcwd()

def Content_process( sentence ):
    
    while True:
                start = sentence.find("[")
                middle = sentence.find("|")
                end = sentence.find("]")
                if start == -1 or middle == -1 or end == -1:
                    break
                if end <= start:
                    sentence = sentence[:end] + sentence[end+1:]
                    continue
                sentence = sentence[:start] + sentence[start+1: middle] + sentence[end+1:]
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z0-9_]", " ", sentence) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words )) 
    
    
##############################################################################################
##############  generating 200 profession files from wiki sentences ##########################
##############################################################################################
    
## delimiter new line is used ,it causes error bcz some lines have two \n so those lines are considered bad and removed 
## tab delimiter doesn't has this issue but lines are not well seperated.
#### frequent patterns with length 2,3,4 may have the n-gram person,profession combination
## this profession files may even furthur diveded based on person
os.chdir("/shared/data/mangipu2/triple-scoring")    
df=pd.read_csv("wiki-sentences",sep='\n',header=None,encoding='utf-8',error_bad_lines=False)   # remove nrows to run on the whole wikisentences file
df.columns=['Sentence']  
pro_df=pd.read_csv("professions",sep='\n',header=None,encoding='utf-8')
pro_df.columns=['Profession'] 
os.chdir("/shared/data/mangipu2/triple-scoring/Profession_sentences")   
for i in range(pro_df.shape[0]):
    sentences_pro=[]
    profession=pro_df['Profession'][i]
    for j in range(df.shape[0]):
        sentence=df['Sentence'][j]  #.replace("_"," ")
        sentence_processed=Content_process(sentence)
        if sentence.find(profession)!=-1:
            sentences_pro.append(sentence_processed)
    print(len(sentences_pro))  
    sentences_df=pd.DataFrame(sentences_pro)
    sentences_df.to_csv(str(profession)+"_"+str("sentences.txt"),index_label=False,header=None,index=False)
    
    
    
#################################################################################################
############### generating 100 nation files from wiki sentences #################################
################################################################################################# 
os.chdir("/shared/data/mangipu2/triple-scoring")    
Nation_df=pd.read_csv("nationalities",sep='\n',header=None,encoding='utf-8')
Nation_df.columns=['Nationality'] 
os.chdir("/shared/data/mangipu2/triple-scoring/Nationality_sentences") 
for i in range(Nation_df.shape[0]):
    sentences_nation=[]
    nation=Nation_df['Nationality'][i]
    for j in range(df.shape[0]):
        sentence=df['Sentence'][j]  #.replace("_"," ")
        sentence_processed=Content_process(sentence)
        if sentence.find(nation)!=-1:
            sentences_nation.append(sentence_processed)
    print(len(sentences_nation))  
    sentences_df=pd.DataFrame(sentences_nation)
    sentences_df.to_csv(str(nation)+"_"+str("sentences.txt"),index_label=False,header=None,index=False)

os.chdir("/shared/data/mangipu2/triple-scoring") 