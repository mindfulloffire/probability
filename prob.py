import random
random.choice(['clubs','diamonds','spades','hearts'])
random.choice(['clubs','diamonds','spades','hearts'])
suits=['clubs','diamonds','spades','hearts']
cards=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deckofcards=dict(zip(suits,cards))
squares=[]
for i in range(1000):
    squares.append(i**2)

divthreequares=[]
for num in squares:
    if num%3 == 0:
        divthreequares.append(num)

print(len(divthreequares)/len(squares))
from itertools import combinations
from itertools import permutations


samp=['h','h','h','h','t','t','t']
len(samp)
type(samp)
samperm=list(permutations(samp, 7))
samperm
import itertools
from numpy import array
sampermlists=[]

for tuple in samperm:
    sampermlists.append(list(tuple))


import numpy as np
import pandas as pd

samparray=np.array([np.array(xi) for xi in sampermlists])

myList=[]

[val for val in x if y[x.index(val)]]
for each in samparray:

len(myList)


for a in samparray:
    if a[1]


len(myList)




type(sampermlists[0])
len(sampermlists)
sampermlists[0][1]


secondheadslist=[]




coin=[0,1]
tosses


comb = combinations('abcdefghi',2)
comblist=[]
for i in list(comb):
        comblist.append(i)
pprint(comblist)
len(comblist)
pp=pprint.PrettyPrinter(indent=4)
pp.pprint(comblist)
anb=(.05*.99)
anb
acnb=.95*.1
acnb
b=acnb+anb
b
agivb=(.05*.99)/b
agivb
216/36
1296/36
list=[]
for i in range(100):
    list.append((2**-i)*(3**-i))
list
sum(list)
falsepos=.999*.05
falsepos
accpos=.001*.95
accpos
probpos=falsepos+accpos
probpos
accpos/probpos
cards=52
aces=4
aces_prob=aces/cards
print(round(aces_prob,4))
import random
random_number=random.random()
print(random_number)
from random import SystemRandom
crypto=SystemRandom()
print(crypto.random())
import numpy as np
x=np.random.sample((3,4))
print(x)
import os
os.listdir("/")
