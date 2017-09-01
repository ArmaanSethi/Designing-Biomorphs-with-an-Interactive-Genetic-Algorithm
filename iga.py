# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random
NUM_GENES = 12#number of genes per bug
NUM_BUGS = 12#number of bugs
a = []
b = []

def init_population():
    t = np.arange(0,8*np.pi, 0.001)
    for j in range(NUM_BUGS):
        ai = []
        bi = []
        x = 0
        y = 0
        for i in range(NUM_GENES):
            ai.append(random.randint(-5,5))
            bi.append(random.randint(-5,5))
        a.append(ai)
        b.append(bi)
        for i in range(NUM_GENES):
            x += ai[i]*np.cos((i+1)*t)
            y += bi[i]*np.sin((i+1)*t)
        newSubPlot = plt.subplot(3,4,j+1)
        newSubPlot.set_title(j)
        plt.plot(x,y)
        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(12,9, forward = True)
    plt.show()
    print a
    print b

def user_select():
    c = []
    i = 0
    while i >= 0:
        while True:
            try:
                i = int(raw_input("What looks like a bug? (enter -1 to end):  "))
                c.append(i)
            except:
                print "Bad Input"
                continue
            else:
                print "Good input"
                break
    c.sort()
    c = c[1:]
    print "THESE LOOK LIKE BUGS:   ", c
    return c

def breed_mutate(c):
    global a
    global b
    print "PreMutationA: ", a
    print "PreMutationB: ", b
    if len(c) == 0:
        print "DEAD"
    else:
        new_a = []
        new_b = []
        for i in range(NUM_BUGS):
            cross_point = random.randint(0,NUM_GENES)
            mom = c[random.randint(0,len(c)-1)]
            dad = c[random.randint(0,len(c)-1)]
            if(mom == dad):
                dad = c[random.randint(0,len(c)-1)]
                if(mom == dad):
                    dad = c[random.randint(0,len(c)-1)]
            new_a.append(a[mom][0:cross_point] + a[dad][cross_point:NUM_GENES])
            new_b.append(b[dad][0:cross_point] + b[dad][cross_point:NUM_GENES])
            for j in range(2*NUM_GENES):
                mutation = random.randint(0,1000)
                if mutation == 0:
                    print mutation,"MUTATION",j
                    if j < NUM_GENES:
                        #mutate new_a
                        new_a[len(new_a)-1][j] = random.randint(-5,5)
                    else:
                        #mutate new_b
                        new_b[len(new_b)-1][j-NUM_GENES] = random.randint(-5,5)
    a = new_a
    b = new_b
    print "Breeding Complete"

def gen_population():
    global a
    global b
    print "New PopulationA: ", a
    print "New PopulationB: ", b
    t = np.arange(0,8*np.pi, 0.001)
    for j in range(NUM_BUGS):
        x = 0
        y = 0
        for i in range(NUM_GENES):
            x += a[j][i]*np.cos((i+1)*t)
            y += b[j][i]*np.sin((i+1)*t)
        newSubPlot = plt.subplot(3,4,j+1)
        newSubPlot.set_title(j)
        plt.plot(x,y)
        plt.axis('off')
        fig = plt.gcf()
        fig.set_size_inches(12,9, forward = True)
    plt.show()



def main():
    answer = ""
    init_population()#intial population
    while answer != "nah":
        breed_mutate(user_select())#breed and mutate
        gen_population()#new population
        answer = raw_input("continue or nah?")#User decides when the bugs have converged

main()
