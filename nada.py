import random

#bob and his coins

coin_a=[0,1]


coin_b=[0,1,1,1,1,1,1,1,1,1]
len(coin_b)
len(coin_a)


bag=[coin_a,coin_b]

def flip(coin):
    return random.choice(coin)

def choose():
    return random.choice(bag)


flip(coin_a)
flip(coin_b)


choose()

flip(choose())


n=5
list=[]

bunch=[]


def run5():
    for i in range(n):
        x=flip(choose())
        list.append(x)

run5()


list
run5()
list
run5()
list
len(list)
run5()
list
len(list)
sum(list)
run5()
list
len(list)
sum(list)
sum(list)/5
run5()
list
len(list)
sum(list)
sum(list)/7
run5()
run5()
run5()
len(list)
sum(list)/10
run5()
run5()
run5()
len(list)
run5()
len(list)
sum(list)/14
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
len(list)
sum(list)/34
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
run5()
len(list)
len(list)/5
sum(list)/56
for i in range(100000):
    run5()
len(list)/5
sum(list)/(len(list)/5)
u
