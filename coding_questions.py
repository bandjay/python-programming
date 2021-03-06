''' Confusion matrix '''
y_actual=[1,1,1,0,1,1,0,0,1,1,1,1]
y_pred=[1,1,0,0,1,1,0,0,1,1,1,1]

mat=[[0,0],[0,0]]

for i,j in zip(y_actual,y_pred):
        mat[i][j]+=1
       

print(mat)

''' Call by obj or obj ref '''
a=[0,1,2,3]
b=a[:]
print (b,a)
a.pop()
print (b,a)


v1=25
def f1():
    print(v2)

def f2():
    global v2
    v2=10
    f1()

f2()


listA = [23,24]
listB = listA
listB
print (listA)


listA = [23,24]
listB = listA[:]
listB[0]=25
print (listA,listB)


''' Two sorted lists '''
l1=[i for i in range(100000000)]
l2=[i for i in range(100000000)]
for k in l2:
    l1.append(k)

l1.extend(l2)


a=[1,3,5,7,9,13,17]
b=[2,4,6,8,12,14,15,18,22,26]

i,j=0,0
s=[]
while (i<len(a) and j<len(b)) :
    if a[i]<b[j]:
        s.append(a[i])
        i+=1
    else:
        s.append(b[j])
        j+=1
if i<len(a):
    s.extend(a[i:])
if j<len(b):
    s.extend(b[j+1:])

             
def checkBST(n, min=0, max=10000):
    if not n:
        return True
    if n.data <= min or n.data >= max:
        return False
    return checkBST(n.left, min, n.data) and checkBST(n.right, n.data, max)   

'''Running median '''
l=[1,2,3,4,5,6,7,8,9,-3]
from heapq import heappush as push, heappushpop as pushpop
min_h,max_h=[],[]

for val in l:
    val=pushpop(max_h,val)
    val=-pushpop(min_h,-val)
    if len(max_h)<=len(min_h):
        push(max_h,val)
    else:
        push(min_h,-val)
if len(max_h)>len(min_h):
    print(max_h[0])
else:
    print((max_h[0]-min_h[0])/2.0)    
                            
''' insertion sort '''
def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1
            
''' merge sort '''
import sys

def merge(l1,l2):
    l=[]
    i,j=0,0
    while i<len(l1) and j<len(l2):
        if l1[i]<l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
            inv+=1
    if i<len(l1):
        l.extend(l1[i:])
    if j<len(l2):
        l.extend(l2[j:])
    return l

def mergesort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergesort(L[:middle])
        right = mergesort(L[middle:])
        return merge(left, right)
result= mergesort([2,1,3,1,2])
print(result)   

''' Two sum '''
a=[2,3,5,1,3,6]
t=8
dict_={}
for i in a:
    d=t-i
    if d in dict_.keys():
        print(i,d)
    else:
        dict_[i]=i
        print(i,"added")

''' fibnocci '''        
def fib(n):
    if n<=2:
        return 1
    else:
        return(fib(n-1)+fib(n-2))
                
fib(6)

''' gcd '''

def gcd(x,y):
    while y!=0:
        x,y=y,x%y
    print(x)
gcd(10,15) 
   
''' Staircase '''
s = int(input().strip())
def paths(n):
    s0, s1, s2 = 1, 1, 2
    for _ in range(n):
        s0, s1, s2 = s1, s2, s0 + s1 + s2
    return s0
for a0 in range(s):
    n = int(input().strip())
    print(paths(n))
    
'''Towers of hanoi 
Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

Move a tower of height-1 to an intermediate pole, using the final pole.
Move the remaining disk to the final pole.
Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
'''
def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

moveTower(3,"A","B","C")    
    
''' Comibations '''

def perms01(li):
    if len(li)<2:
         yield li
    else:
        for perm in perms01(li[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + li[0:1] + perm[i:]
 
for p in perms01(['a','b','c','d']):
    print (p)
    
    
''' list of files in a directory '''
import os
path="C:\insight"

def print_file(pa):
    for p in os.listdir(pa):
        new_p=os.path.join(pa,p)
        if os.path.isdir(new_p):
            print_file(new_p)
        else:
            print(new_p)
            
print_file(path)

'''Inheritance'''
class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    def __display__(self):
        print("MODEL:",self.model)

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.battery_type=battery_type
        super(ElectricCar, self).__init__(model, color, mpg)
        
car = ElectricCar('battery', 'ford', 'golden', 10)
car.__display__()

'''BFS 
Check the starting node and add its neighbours to the queue.
Mark the starting node as explored.
Get the first node from the queue / remove it from the queue
Check if node has already been visited.
If not, go through the neighbours of the node.
Add the neighbour nodes to the queue.
Mark the node as explored.
Loop through steps 3 to 7 until the queue is empty.

for dfs use stack
'''
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

def bfs(graph,start):
    explored=[]
    q=[start]
    while q:
        node=q.pop(0)
        if node not in explored:
            explored.append(node)
            connected=graph[node]
            for c in connected:
                q.append(c)
    return explored        

bfs(graph,'A')

