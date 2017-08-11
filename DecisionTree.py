
import os
import sys
import random
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
            
            
    label_tr=[]
    predictors_tr=[]
    #data=dataread("balance-scale.train") 
    for i in range(len(train)):
        label_tr.append(train[i][0])
        predictors_tr.append(train[i][1])
    features_tr=[]    
    for k in range(len(predictors_tr[1])):
        con=[]
        for j in range(len(train)):
            con.append(predictors_tr[j][k])
        features_tr.append(con) 
        
    label_te=[]
    predictors_te=[]
    #data=dataread("balance-scale.train") 
    for i in range(len(test)):
        label_te.append(test[i][0])
        predictors_te.append(test[i][1])
    features_te=[]    
    for k in range(len(predictors_te[1])):
        con=[]
        for j in range(len(test)):
            con.append(predictors_te[j][k])
        features_te.append(con)         
        
        
        
        
    # train freq class    
    tr_all_labels=list(set(label_tr))
    tr_freq_values=[]   
        
        # Calculate the frequency of each of the values in labels
    for l in range(len(tr_all_labels)) : 
        tr_freq_values.append(label_tr.count(tr_all_labels[l])) 
    tr_max_freq=max(tr_freq_values)
    for i in range(len(tr_freq_values)):
        if tr_freq_values[i]==tr_max_freq:
            tr_freq_class=tr_all_labels[i]  
        
        
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
                
        if len(predictors)<0 or len(features) <=0:
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
                best_feat_subset=[]
                best_feat_subset_label=[]
                for l in range(len(best_feature_col)):
                    if best_feature_col[l]==best_feature_values[z]:
                        best_feat_subset.append(predictors[l])
                        best_feat_subset_label.append(label[l])
                        
                for b in range (len(best_feat_subset)):
                    #best_feat_subset[b].remove(best_feat_subset[b][best])
                    del best_feat_subset[b][best]
                    
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
        
        
    # constructing tree on training data
    my_tree_tr= constructTree(predictors_tr,features_tr, label_tr) 
    attr_te=[list(i) for i in zip(*features_te)]
    # making predictions on testing data.
    pred=[]
    for e in range(len(features_te[0])):
        tempDict = my_tree_tr.copy()
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
        if len(pred[r])!=1 or type(pred[r])==dict:
            #print(r)
            pred[r]=tr_freq_class
    expected=[]
    predicted=[]        
    for i in range(len(label_te)):
        expected.append(int(label_te[i]))
        predicted.append(int(pred[i][0]))
            
    #expected=[1,2,3,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3]  
    #predicted=[1,2,3,3,2,1,1,1,3,2,1,3,2,2,2,1,1,1,3]                 
    def conf_matrix(expected, predicted, n_cls):
        m = [[0] * n_cls for i in range(n_cls)]
        for pre, exp in zip(predicted, expected):
            m[pre-1][exp-1] += 1
        return m
    confusion_matrix=conf_matrix(predicted, expected,len(list(set(label_te))))
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
        


