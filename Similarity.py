import pandas as pd
import numpy as np
import os
import math
import heapq
os.chdir('C:/Users/jaycb/Desktop/CS 512/dblp_data/data')
PA=pd.read_csv('PA.txt',sep='\t',header=None,index_col=False)
PA.columns=['pid','aid','c'] 
PA=PA[['pid','aid']]

PC=pd.read_csv('PC.txt',sep='\t',header=None,index_col=False)
PC.columns=['pid','cid','c'] 
PC=PC[['pid','cid']]

PT=pd.read_csv('PT.txt',sep='\t',header=None,index_col=False)
PT.columns=['pid','tid','c'] 
PT=PT[['pid','tid']]

PAC= PA.merge(PC,on='pid')
PAT= PA.merge(PT,on='pid')


#############################################################
##############  PATH SIM ####################################
#############################################################

##  author-paper-venue-paper-author meta path
Aggr_PAC= pd.DataFrame({'count' : PAC.groupby( [ "aid", "cid"] ).size()}).reset_index()


def vectorize(ID):
    SearchRec=Aggr_PAC[Aggr_PAC.aid==ID]
    cidlist=np.array(SearchRec['cid'])
    cidall=np.array(pd.unique(Aggr_PAC['cid']))
    search_counts=np.array(SearchRec['count'])
    search_vector=[0]*len(cidall)
    for i in range(len(cidall)):
        for j in range(len(cidlist)):
            if cidall[i]==cidlist[j]:
                search_vector[i]=search_counts[j]
    return search_vector

def distance(v1,v2):
    prod_sum=0
    v1_sum=0
    v2_sum=0
    for p in range(len(v1)):
        v1_sum=v1_sum+math.pow(v1[p],2)
        v2_sum=v2_sum+math.pow(v2[p],2)
        prod_sum=prod_sum+(2*v1[p]*v2[p])
    return (prod_sum/(v1_sum+v2_sum))    
    

aidall=np.array(pd.unique(Aggr_PAC['aid']))
dist_all=[0]*len(aidall)
#aid_all=[0]*len(aidall)
searchID=7696
search_vec=vectorize(searchID)
for k in range(len(aidall)):
    comp_vec=vectorize(aidall[k])
    dist_all[k]=distance(search_vec,comp_vec)
    #aid_all[k]=k
    
first_five=heapq.nlargest(6, range(len(dist_all)), dist_all.__getitem__)  
print("Top 5 similar Authors to ",searchID,"based on APVPA meta path are:" )
for i in range(1,6):
    print(first_five[i]+1)



##  author-paper-venue-paper-author meta path
Aggr_PAT= pd.DataFrame({'count' : PAT.groupby( [ "aid", "tid"] ).size()}).reset_index()


def vectorize(ID):
    SearchRec=Aggr_PAT[Aggr_PAT.aid==ID]
    tidlist=np.array(SearchRec['tid'])
    tidall=np.array(pd.unique(Aggr_PAT['tid']))
    search_counts=np.array(SearchRec['count'])
    search_vector=[0]*len(tidall)
    for i in range(len(tidall)):
        for j in range(len(tidlist)):
            if tidall[i]==tidlist[j]:
                search_vector[i]=search_counts[j]
    return search_vector

def distance(v1,v2):
    prod_sum=0
    v1_sum=0
    v2_sum=0
    for p in range(len(v1)):
        v1_sum=v1_sum+math.pow(v1[p],2)
        v2_sum=v2_sum+math.pow(v2[p],2)
        prod_sum=prod_sum+(2*v1[p]*v2[p])
    return (prod_sum/(v1_sum+v2_sum))    
    

aidall=np.array(pd.unique(Aggr_PAT['aid']))
dist_all=[0]*len(aidall)
#aid_all=[0]*len(aidall)
searchID=7696
search_vec=vectorize(searchID)
for k in range(len(aidall)):
    comp_vec=vectorize(aidall[k])
    dist_all[k]=distance(search_vec,comp_vec)
    #aid_all[k]=k
    
first_five=heapq.nlargest(6, range(len(dist_all)), dist_all.__getitem__)  
print("Top 5 similar Authors to ",searchID,"based on APTPA meta path are:" )
for i in range(1,6):
    print(first_five[i]+1)
   
    
    
