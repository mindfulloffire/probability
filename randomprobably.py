import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
%matplotlib inline
def di():
    n=[1,2,3,4,5,6]
    return random.choice(n)

di()
di()
di()
di()
di()
series = np.array([di() for x in range(5)])
series

def dice():
    return di() + di ()
dice()
dice()
dice()
dice()
dice()
dice()
dice()
dice()


series2=np.array([dice() for x in range(5)])
series2
plt.figure(figsize=(20,10))
plt.hist(series2,bins=11,align='mid')
print(len([x for x in series2 if x<=3])/float(len(series2)))
pairs=[[0,1],[1,0],[-1,0],[0,-1]]











def wai():
    n=[0,1,2]
    return random.choice(n)

seriesy=np.array([wai() for x in range(10000)])

plt.hist(seriesy)


np.mean(seriesy)
np.var(seriesy)

def bee():
    n=[0,2]
    return random.choice(n)

seriesb=np.array([bee() for x in range(10000)])

plt.hist(seriesb)


np.mean(seriesb)
np.var(seriesb)




A=[0,1]
B=[0,0,0,1]
bag=[B,B,B,A]
C=[0,0,0,1,1,1,1]
flips=[]
def compose2(f, g):
    return lambda x: f(g(x))


def choose():
    for x in range():
        return random.choice(bag)


def flip(coin):
    for x in range(1):
        return random.choice(coin)


flip(C)
seriesx=np.array([flip(C) for x in range(100)])
seriesx



n=2**7
n


def flipnchoose():
    x=random.choice(bag)
    return(flip(x))

flipnchoose()

seriez = np.array([flipnchoose() for x in range(10)])

seriez

num=7*6*5*4
num
num/24


A
B



Bseries_list=[]
def px1():
    for x in range(100):
        series_list.append(np.array([di() for x in range(5)]).tolist())

px1()

len(series_list)

twos_threes=[]

for x in series_list:
    if 2 | 3 in x:
        twos_threes.append(x)

len(twos_threes)
for x in twos_threes:
    if 2 & 3 in x:
        twos_threes.pop(twos_threes.index(x))

len(twos_threes)
for x in twos_threes:
    if 2 & 2 in x:
        twos_threes.pop(twos _threes.index(x))
for x in twos_threes:
    if 3 & 3 in x:
        twos_threes.pop(twos_threes.index(x))


len(twos_threes)/len(series_list)

print(len([x for x in series if x==2 | x==3])/float(len(series)))

print(len([x for x in series if x==2 | x==3])/float(len(series)))


def dice():
    return di() + di ()
dice()
dice()
dice()
dice()
dice()
dice()
dice()
dice()
series2=np.array([dice() for x in range(5)])
series2
plt.figure(figsize=(20,10))
plt.hist(series2,bins=11,align='mid')
print(len([x for x in series2 if x<=3])/float(len(series2)))

d=[1,2,3,4]

def d4():
    return random.choice(d)

def d4product():
    return d4()*d4()

d_series=np.array([d4product() for x in range(10000)])
d_series
pw4=len([x for x in d_series if x==4])/float(len(d_series))
pw4

pw5=len([x for x in d_series if x==5])/float(len(d_series))
pw5


coin=[0,1]

def flip():
    return random.choice(coin)

flip()
nflips=np.array([flip() for x in range(100)])
nflips
sum(nflips)

plt.hist(nflips,bins=100)

z=np.random.geometric(p=1/3, size=100)
z

from scipy.stats import bernoulli
fig, ax= plt.subplots(1,1)
p=.75
mean, var, skew, kurt = bernoulli.stats(p, moments='msvsk')

x = np.arange(bernoulli.ppf(.01, p),bernoulli.ppf(.99, p))
mean
var
skew
kurt

ax.plot(x, bernoulli.pmf(x, p), 'bo', ms=8, label='bernoulli')
ax.vlines(x, 0, bernoulli.pmf(x, p), colors='b', lw=5, alpha=.5)
plt.show()
fig

r=bernoulli.rvs(p, size=100)
r


p=.9
n=1-(p+p*(1-p)+(p*(1-p)**2)+(p*(1-p)**3)+(p*(1-p)**4)+(p*(1-p)**5)+(p*(1-p)**6)+(p*(1-p)**7)+(p*(1-p)**8)+(p*(1-p)**9))

n


x=np.array([-1,2])
y=np.array([-2,3])
x-y


A=
