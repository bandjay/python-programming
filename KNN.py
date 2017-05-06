# -*- coding: utf-8 -*-
"""
Created on Fri May 05 23:56:54 2017

@author: jaycb
"""

"""
Nearest Negihbours Simple program both for Classification and Regression
"""
class KNN:
    def __init__(self,data,target,k):
        self.data=data
        self.target=target
        self.k=k
           
    def __eucludian__(self,v1,v2):
        if len(v1)==len(v2):
            return sum([(x1-x2)**2 for x1,x2 in zip(v1,v2)])
    
    def train(self):
        tr_labels=[]        
        for p1 in self.data:
            dist_vec=[]
            for p2 in self.data:
                dist_vec.append(self.__eucludian__(p1,p2))
            index_k=sorted(range(len(dist_vec)), key=lambda v: dist_vec[v])[0:self.k+2]
            label_k=[self.target[i] for i in index_k]
            if type(label_k[0])==str:
                tr_labels.append(max(set(label_k), key=label_k.count))
            else :
                tr_labels.append(sum(label_k)/len(label_k))
        return tr_labels
    
    def test(self,test_data):
        te_labels=[]
        for p1 in test_data:
            dist_vec=[]
            for p2 in self.data:
                dist_vec.append(self.__eucludian__(p1,p2))
            index_k=sorted(range(len(dist_vec)), key=lambda v: dist_vec[v])[0:self.k+2]
            label_k=[self.target[i] for i in index_k]
            if type(label_k[0])==str:
                te_labels.append(max(set(label_k), key=label_k.count))
            else :
                te_labels.append(sum(label_k)/len(label_k))
        return te_labels

            
data=[[1,2,3,4,5,6],[2,3,4,6,7,8],[2,3,4,5,7,6],[1,2,3,5,6,7],[4,5,6,2,3,4],[2,3,4,5,8,9],[4,5,6,1,3,4]]
target=['1','2','2','1','3','2','3']
target1=[1.2,2.3,2.5,1.0,3.2,4.2,3.4]
k=3
test_data=[[4,5,6,3,4,4],[1,2,2,4,5,6]]
print("trained KNN Classification:",KNN(data,target,k).train())      
print("trained KNN Regression:",KNN(data,target1,k).train()) 
print("test labels Classification:",KNN(data,target,k).test(test_data))  
print("test labels Regression:",KNN(data,target1,k).test(test_data))       