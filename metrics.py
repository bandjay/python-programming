# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:53:24 2016

@author: Jay
"""

#con_mat=[[7,0,1,0,0],[1,7,0,0,0],[0,0,7,1,0],[0,0,0,7,1],[0,0,0,1,7]]
def Accuracy(confusion_matrix):
    diag_sum=0
    mat_sum=0
    for i in range(len(confusion_matrix)):
        diag_sum=diag_sum+confusion_matrix[i][i]
        for j in range(len(confusion_matrix)):
            mat_sum=mat_sum+confusion_matrix[i][j]
    return (diag_sum/mat_sum)        

Accuracy(confusion_matrix) 

#expected=[1,2,3,3,2,1,2,3,3,2,1,3,1,1,2,1,1,1,3,1,1,2]  
#predicted=[1,1,1,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3,3,2,1] 
n_cls=list(set(expected))                
def conf_matrix(expected, predicted, n_cls):
    m = [[0] * n_cls for i in range(n_cls)]
    for pred, exp in zip(predicted, expected):
        m[pred-1][exp-1] += 1
    return m


def class_mat(expected,predicted,class_lab):
    exp=expected
    pre=predicted
    for i in range(len(expected)):
        if expected[i]==class_lab:
            exp[i]=1
        else :
            exp[i]=0
        if predicted[i]==class_lab:    
           pre[i]=1
        else :
            pre[i]=0
    return conf_matrix(exp,pre,2)        
            
for c in range(len(n_cls)):
    class_lab=n_cls[3]
    #expected=[1,2,3,3,2,1,2,3,3,2,1,3,1,1,2,1,1,1,3,1,1,2]  
    #predicted=[1,1,1,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3,3,2,1] 
    mat=class_mat(expected,predicted,class_lab)
    TP=mat[0][0]
    FP=mat[1][0]
    FN=mat[0][1]
    TN=mat[1][1]
    print("class label",class_lab,"sensitivity",(TP/(TP+FN)))
    print("class label",class_lab,"specificity",(TN/(TN+FP)))
    print("class label",class_lab,"precision",(TP/(TP+FP)))
    print("class label",class_lab,"recall",(TP/(TP+FN)))
    P=TP/(TP+FP)
    R=TP/(TP+FN)
    print("class label",class_lab,"F1 score",((2*P*R)/(P+R)))
    print("class label",class_lab,"F0.5 score",((1.25*P*R)/((0.25*P)+R)))
    print("class label",class_lab,"F2 score",((5*P*R)/((4*P)+R)))
    