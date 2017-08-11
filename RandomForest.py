import os
import sys
import random
import math
random.seed(2016)

#cwd = os.getcwd()
#os.chdir("C:/Users/Jay/Desktop/CS 412/HW4") # setting working directory

#train_file="nursery.data.train"
#test_file="nursery.data.test"
#train_file="poker.train"
#test_file="poker.test"
#train_file="led.train.new"
#test_file="led.test.new"
#train_file="balance-scale.train"
#test_file="balance-scale.test"



##### main method
def main():
    # print command line arguments
    #print("main starts")
    train_file=sys.argv[1]
    test_file=sys.argv[2]
    ###print(train_file)
 

    #################################################
    ########   STEP-1   #############################
    #################################################
    #### fucntion to read data  
    def dataread (filename):
        with open(filename) as dFile:     
                data = dFile.read().splitlines()
        lines=[]  
        label=[] 
        recs=[] 
        #row_len=[]
        #for d in range(len(data)):
        #    row=data[d].split(' ')
        #    row_len.append(len(row))
        #max_len=max(row_len)    
    
        for k in range(len(data)):
            line=data[k].split(' ')
            lines.append(line)
            label.append(line[0])
            val=[]
            #val=['0']*(max_len)
            for i in range(len(line)-1): 
                  kv_pair=line[i+1].split(':')
            #      for m in range(max_len):
            #              if int(kv_pair[0])==m:
                  val.append(kv_pair[1]) 
            #vals=val[1:max_len]                                 
                                       
            recs.append([line[0],val])
        #if len(lines)==len(recs) :
          #  print("Data read correctly")
        return (recs)  
    
    
    ## reading all data files test and train    
    train=dataread(str(train_file)) 
    test=dataread(str(test_file)) 
    
    
    #######################################################
    ########### Step-2  Decision tree model  ##############
    #######################################################
    
    # remove missing data    
    for i in range(len(train)):
        if train[i][0]=='':
            train.remove(train[i])
    for i in range(len(test)):
        if test[i][0]=='':
            test.remove(test[i])        
            
            
    label_train=[]
    predictors_train=[]
    #data=dataread("balance-scale.train") 
    for i in range(len(train)):
        label_train.append(train[i][0])
        predictors_train.append(train[i][1])
    features_train=[]    
    for k in range(len(predictors_train[1])):
        con=[]
        for j in range(len(train)):
            con.append(predictors_train[j][k])
        features_train.append(con) 
        
    label_test=[]
    predictors_test=[]
    #data=dataread("balance-scale.train") 
    for i in range(len(test)):
        label_test.append(test[i][0])
        predictors_test.append(test[i][1])
    features_test=[]    
    for k in range(len(predictors_test[1])):
        con=[]
        for j in range(len(test)):
            con.append(predictors_test[j][k])
        features_test.append(con)         
        
        
        
        
    # train freq class    
    #tr_all_labels=list(set(label_tr))
    #tr_freq_values=[]   
        
        # Calculate the frequency of each of the values in labels
    #for l in range(len(tr_all_labels)) : 
    #    tr_freq_values.append(label_tr.count(tr_all_labels[l])) 
    #tr_max_freq=max(tr_freq_values)
    #for i in range(len(tr_freq_values)):
    #    if tr_freq_values[i]==tr_max_freq:
    #        tr_freq_class=tr_all_labels[i]  
        
        
    # fucntion to calculate gini index
    def gini(glabel):
        all_labels=list(set(glabel))
        g_freq_values=[]   
        sum_sqr_prob = 0.0
        # Calculate the frequency of each of the values in labels
        for l in range(len(all_labels)) : 
            g_freq_values.append(glabel.count(all_labels[l]))
        
        # Calculate the overall gini of the data for the labels
        for f in range(len (g_freq_values)):
            sum_sqr_prob += (g_freq_values[f]/len(glabel))**2
        
        gini=1-sum_sqr_prob    
        return gini
        
    
    # fucntion to calculate impurity of split by feature  
    #data=best_feat_subset
    #feature=new_features[0]
    #label=best_feat_subset_label  
    def impurity(ifeature, ilabel):
        
        feature_all_labels=list(set(ifeature))
        feature_freq_values=[]
        subset_gini=0.0
        # Calculate the frequency of each of the values in a feature
        for l in range(len(feature_all_labels)) : 
            feature_freq_values.append(ifeature.count(feature_all_labels[l]))
        
        # Calculate the sum of the gini for each subset of records 
        for f in range(len(feature_freq_values)) :
            prob    = feature_freq_values[f] / sum(feature_freq_values)
            subset_label=[]
            for k in range(len(ifeature)):
                if ifeature[k]==feature_all_labels[f]:
                    subset_label.append(ilabel[k])
            #print(len(data_subset)) 
            #print(len(subset_label))
            subset_gini += prob * gini(subset_label)
        # return impurity for the feature
        return (gini(ilabel) - subset_gini)    
    
    # Function to choose best feature at each split
    def best_feature(bfeatures, blabel):
        best = 0 # features[0]
        imp_all=[]
        for f in range(len(bfeatures)):
            imp_all.append(impurity(bfeatures[f],blabel))
        min_imp=min(imp_all) 
        for o in range(len(imp_all)):
            if imp_all[o]==min_imp:
                best= o #bfeatures[o]
        return best
        
    
    # constructing a tree
    def constructTree(predictors,features, label):        
        ## If the dataset is empty or the feature set is empty assign most frequent class
        all_labels=list(set(label))
        freq_values=[]   
        # Calculate the frequency of each of the values in labels
        for l in range(len(all_labels)) : 
            freq_values.append(label.count(all_labels[l]))
        max_freq=max(freq_values)
        for i in range(len(freq_values)):
            if freq_values[i]==max_freq:
                freq_class=all_labels[i]  
                
        if not predictors or len(features) <=0 :
                    return freq_class
        # If all observations in the dataset has same class then node is pure no furthur splitting (stop criterion)
        elif len(all_labels)==1:
            return all_labels[0]
        else:
            
            best = best_feature(features,label)
            tree = {best:{}}
        
            # Create a new sub tree for best feature with the values in the best feature
            best_feature_values=list(set(features[best]))
            best_feature_col=features[best]
        
            for z in range(len(best_feature_values)) :
                # Create a subtree for the current value under the "best" field
                bfs=[]
                best_feat_subset_label=[]
                for l in range(len(best_feature_col)):
                    if best_feature_col[l]==best_feature_values[z]:
                        bfs.append(predictors[l])
                        best_feat_subset_label.append(label[l])
                
                best_feat_subset=[]                
                for b in range (len(bfs)):
                    #best_feat_subset[b].remove(best_feat_subset[b][best])
                    #print(b)
                    tempb=bfs[b][:]
                    tempb.pop(best)
                    best_feat_subset.append(tempb)
                    
                new_features=[]
                
                for k in range(len(best_feat_subset[0])):
                    con=[]
                    for j in range(len(best_feat_subset)):
                        con.append(best_feat_subset[j][k])
                    new_features.append(con) 

                subtree = constructTree(best_feat_subset,new_features, best_feat_subset_label)
                z_val=best_feature_values[z]
                tree[best][z_val] = subtree
        
        return tree
        
    
    ################################################
    ########### random forest model ################
    def RandomForest(predictors_tr,features_tr,label_tr,predictors_te,features_te,label_te,ntrees,maxfeatures):
        feat_list=[]
        rf_predictions=[]
        for ft in range(len(features_tr)):
            feat_list.append(ft)
        
        # # train freq class    
        tr_all_labels=list(set(label_tr))
        tr_freq_values=[]   
        
        # Calculate the frequency of each of the values in labels
        for l in range(len(tr_all_labels)) : 
            tr_freq_values.append(label_tr.count(tr_all_labels[l])) 
            tr_max_freq=max(tr_freq_values)
            for i in range(len(tr_freq_values)):
                if tr_freq_values[i]==tr_max_freq:
                    tr_freq_class=tr_all_labels[i] 
            
       
        #rf_te_pred=[list(i) for i in zip(*rf_te_feat)]
            
        for nt in range(ntrees):
            #print("ntree" ,nt)
            rf_tr_feat=[]
            rf_te_feat=[]
            rf_tr_pred=[]
        #rf_te_pred=[]
            ran_array=random.sample(feat_list, int(maxfeatures))
            for h in range(len(ran_array)):
                rf_tr_feat.append(features_tr[ran_array[h]])
                rf_te_feat.append(features_te[ran_array[h]])
            rf_tr_pred=[list(i) for i in zip(*rf_tr_feat)]
            
            
            # 0.632 bootstrap of total samples
            rf_tr_pred_boot=[]
            label_tr_boot=[]
            for s in (range(int(len(rf_tr_pred)))):#range(int(0.5*len(rf_tr_pred))):
                ind=random.choice(range(int(0.632*len(rf_tr_pred))))#,1)[0]
                #print(ind)
                rf_tr_pred_boot.append(rf_tr_pred[ind])
                label_tr_boot.append(label_tr[ind])
                
            rf_tr_feat_boot=[list(i) for i in zip(*rf_tr_pred_boot)]   
            
            predictors=rf_tr_pred_boot[:]
            features=rf_tr_feat_boot[:]
            label=label_tr_boot[:]
                
        
            weak_tree=constructTree(predictors,features,label) 
            attr_te=[list(i) for i in zip(*rf_te_feat)]
            # making predictions on testing data.
            pred=[]
            for e in range(len(rf_te_feat[0])):
                tempDict = weak_tree.copy()
                result = []
                while isinstance(tempDict, dict):
                    root = MakeTree(list(tempDict.keys())[0], tempDict[list(tempDict.keys())[0]])
                    tempDict = tempDict[list(tempDict.keys())[0]]
                    index = root.value
                    value = attr_te[e][index]
                    if(value in list(tempDict.keys())):
                        del attr_te[e][index]
                        #attr_te[e].remove(attr_te[e][index])
                        result = tempDict[value]
                        tempDict = tempDict[value]
                    else:
                            break
                        #SAVE prediction in a list
                pred.append(result) 
    
    # dealing with tree rules that don't exist.
            for r in range(len(pred)):
                if len(pred[r-1])!=1 or type(pred[r-1])==dict:
                    #print(r)
                    pred[r-1]=tr_freq_class
    
            
            rf_predictions.append(pred)
            #print("treelabel:",list(set(rf_predicted_labels_te)))
            
        return rf_predictions
        
    predictors_tr=predictors_train[:]
    features_tr=features_train[:]
    label_tr=label_train[:]
    predictors_te=predictors_test[:]
    features_te=features_test[:]
    label_te=label_test[:]
    rf_preds=RandomForest(predictors_tr,features_tr,label_tr,predictors_te,features_te,label_te,9,int(math.sqrt(len(features_tr)))+1)
    
    rf_en_te_pred=[list(i) for i in zip(*rf_preds)] 
    rf_voted_pred=[]                                
    for rf in range(len(rf_en_te_pred)):
        row_lab=list(set(rf_en_te_pred[rf]))
        row_lab_counts=[]
        for l in range(len(row_lab)) : 
            row_lab_counts.append(label_tr.count(row_lab[l])) 
        tr_max_freq_rf=max(row_lab_counts)
        for i in range(len(row_lab_counts)):
                if row_lab_counts[i]==tr_max_freq_rf:
                    rf_voted_pred.append(row_lab[i]) 
    expected=[]
    predicted=[]        
    for i in range(len(label_te)):
        expected.append(int(label_test[i]))
        predicted.append(int(rf_voted_pred[i]))
            
    #expected=[1,2,3,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3]  
    #predicted=[1,2,3,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3]     
            
    def conf_matrix(expected, predicted, n_cls):
        m = [[0] * n_cls for i in range(n_cls)]
        for pred, exp in zip(predicted, expected):
            m[pred-1][exp-1] += 1
        return m
    confusion_matrix=conf_matrix(predicted, expected,len(list(set(label_test))))
    return (confusion_matrix)
    
    
    
if __name__ == "__main__":
    
    class MakeTree:
        value = ""
        subtree = []
        def __init__(self, val, tree):
            self.setValue(val)
            self.generateSub(tree)        
        def __str__(self):
            return str(self.value)        
        def setValue(self, val):
            self.value = val            
        def generateSub(self, tree):
            if(isinstance(tree, dict)):
                self.subtree = tree.keys()
    con_mat= main()
   #con_mat=[[0, 0, 3], [16, 71, 37], [6, 31, 61]]
    for c in range(len(con_mat)):
       print(" ".join(str(x) for x in con_mat[c])) 