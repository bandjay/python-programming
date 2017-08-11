# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 05:50:34 2017

@author: Jay
"""

### Anagram example
def ana(str1,str2):
    s1=list(str1)
    s2=list(str2)
    s1.sort()
    s2.sort()
    flag=True
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            flag=False
    return flag        
    
print (ana("ABD","ADB"))    

### ANagram linear example

def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok
print(anagram_solution4('apple','pleap'))


#### timer module
import datetime
def timer():
    pre=datetime.datetime.now()
    for i in range(10^8):
        a=0
    end=datetime.datetime.now()  
    return (end.second-pre.second)
print (timer()) 

### k th smallest 
def small_k(arr,k):
    f=arr[0]
    i=1
    while len(arr)>i and k!=0:
        if arr[i]<f:
            del(arr[i])
            k=k-1
        i=i+1    
    return f
    
print (small_k([1,2,3],2))   


## hour glass 

arr=[[1,1,1,2,2,2],[2,3,4,5,6,7],[3,4,5,0,9,3],[3,2,1,6,7,4],[1,1,1,1,1,1],[2,3,4,6,7,8]] 
hr_sum=[]    
for i in range(1,5):
    for j in range (1,5):
        sum=arr[i-1][j-1]+arr[i][j]+arr[i-1][j+1]+arr[i][j+1]+arr[i][j-1]
        hr_sum.append(sum)
print(max(hr_sum))      
    
## array rotation

arr=[1,2,3,5,6]
print(arr)
times=2
while times!=0:
     length=len(arr)
     ini=arr[0]
     for i in range(length-1):
         arr[i]=arr[i+1] 
     arr[length-1]=ini 
     times=times-1
print(arr)   


### algo crush

def crush(N,M,ops):
    N_arr=[0]*N
    for o in range(M):
        ind1=ops[o][0] 
        ind2=ops[o][1]
        val=ops[o][2]           
        for n in range(ind1,ind2):
            N_arr[n]=N_arr[n]+val
    return max(N_arr)
    
crush(5,3,[[1,2,100],[2,5,100],[3,4,100]])    

### STACK algo

class stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)   

s = stack()
print(s.is_empty())
s.push(4)
s.push('dog') 
print (s.pop())
print (s.size())       


#string reverse    
def str_rev(my_str):
    str1=list(my_str)
    str2=[]
    st=stack()
    length=len(str1)
    for i in range(length):
        st.push(str1[i])
    for j in range(length):    
        str2.append(st.pop())
        
    return ''.join(str2) 
    
print(str_rev('SIN'))    



## paranthesis checker

def par_checker(sym_str):
    st=stack()
    ind=0
    length=len(sym_str)
    bal=True
    while ind<length:
        if sym_str[ind] in "([{":
            st.push(sym_str[ind])
        else :
            if st.is_empty():
                bal=False
            else :
                top=st.pop()
                if not matches(top,sym_str[ind]):
                    bal=False
        ind=ind+1
    if bal and st.is_empty():
        return True
    else :
        return False
def matches(op,cls):
    opens="({["
    closes=")}]"
    return opens.index(op)==closes.index(cls)   
print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))   


## Base converter

def base_con(num,base):
    dig="0123456789ABCDEF"
    st=stack() 
    rep_str=[]
    while num>0:
        st.push(num%base) 
        num= num// base
    for i in range(st.size()):
        rep_str.append(dig[st.pop()])
    return ''.join(rep_str) 
    
print(base_con(1000,16))   


# Equation cal using postfix

def postfix_eval(postfix_expr):
    operand_stack = stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()
def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
print(postfix_eval('7 8 + 3 2 + /'))


## queue
class Queue:
    def __init__(self):
          self.items=[]
    def is_empty(self):
        return self.item==[]
    def enque(self,item):
        self.items.insert(0,item)
    def deque(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
q1=Queue()
q1.enque("23")
q1.enque("MAX")
print(q1.deque()) 


## round potato

def pot(kids,num):
    qu=Queue()
    #length=len(kids)
    for k in kids:
        qu.enque(k)
    while qu.size() > 1:
        for n in range(num):
            qu.enque(qu.deque())
        qu.deque()
    return qu.deque()   
    
print (pot(['A','B','C','D','E'],5))    

### double ended queue

class Deque:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def add_front(self,item):
        self.items.append(item)
    def add_rear(self,item):
        self.items.insert(0,item)
    def remove_rear(self):
        return self.items.pop(0)
    def remove_front(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
        
 ## palindrom example
def pal(mystr):
     #str1=mystr.split()
     dq=Deque()
     flag=True
     for s in mystr:
         dq.add_rear(s)
     while dq.size() > 1 and flag:
         c1=dq.remove_rear()
         c2=dq.remove_front()
         if c1!=c2:
             flag = False
     return flag

print(pal("STS"))   


# unordered list using data and next 

class Node:
    def __init__(self,init_data):
        self.data=init_data
        self.next=None
    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def set_data(self,item):
        self.data=item
    def set_next(self,new_next):
        self.next=new_next
        
class unorder:
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.set_next(self.head)
        self.head=temp
    def is_empty(self):
        return self.head==None
    def search(self,item):
        flag=False
        current=self.head
        while current!=None and not flag:
            if current.get_data()==item:
                flag=True
            else :
                current=current.get_next()
        return flag 
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count
        
    def remove(self,item):
        current=self.head
        found=False
        
        previous=None
        while not found:
            if current.get_data()==item:
                found=True
            else:
                previous=current
                current=current.get_next()
        if previous==None:
            self.head=current.get_next()
        else:
            previous.set_next(current.get_next())
        
mylist=unorder()
mylist.add(12)
mylist.add(13)
mylist.add(34) 
mylist.remove(23)
mylist.remove(12)
print(mylist.size())   


## sum using recursion

def sum(list):
    if len(list)==1:
        return list[0]
    else :
        return list[0]+sum(list[1:])
        
print(sum([1,2,3,4,5]))

## factorial

def fact(n):
    if n==0:
        return 1
    elif n>=1 :
        return n*fact(n-1)
        
print(fact(4))        