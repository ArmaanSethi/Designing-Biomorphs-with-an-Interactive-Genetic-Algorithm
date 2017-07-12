# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
import random
N = 12#number of genes per bug
M = 12#number of bugs
a =[]
b = []

def chicken():
    ai = []
    bi = []
    t = np.arange(0,8*np.pi, 0.001)
    x = 0
    y = 0

    for j in range(M):
        for i in range(N):
            #ai.append(random.random()*2)
            #bi.append(random.random()*2)
            ai.append(random.randint(-5,5))
            bi.append(random.randint(-5,5))
            
        a.append(ai)
        b.append(bi)
        for i in range(N):
            x += ai[i]*np.cos((i+1)*t)
            y += bi[i]*np.sin((i+1)*t)
            print j
            plt.plot(x,y)
            
            fig = plt.gcf()
            fig.set_size_inches(2,2, forward = True)
            plt.show()
        #x = 0
        #y = 0
        ai = []
        bi = []
    print a
    print b
    
def chicken2():
    c = []
    i = 0
    while i >= 0:
        while True:
            try:
                i = int(raw_input("What looks like a bug?Pick 6 ( enter -1 to end):  "))
                c.append(i)
            except:
                print "You done messed up"
                continue
            else:
                print "Good input"
                break
    c.sort()
    c = c[1:]
    print "C:   ", c
    return c
    
def chicken3(c):
    global a
    global b
    print "Chicken3:a: ", a
    print "Chicken3:b: ", b

    new_a = []
    new_b = []
    for i in range(M):
        cross_point = random.randint(0,N)
        mom = random.randint(0,len(c))
        dad = random.randint(0,len(c))
        if(mom == dad):
            dad = random.randint(0,len(c))
            if(mom == dad):
                dad = random.randint(0,len(c))
        new_a.append(a[mom][0:cross_point] + a[dad][cross_point:N])
        new_b.append(b[dad][0:cross_point] + b[dad][cross_point:N])

    a = new_a
    b = new_b
        
        
        
    
    print "im breeding"

def chicken4():
    global a
    global b
    print "Chicken4:a: ", a
    print "Chicken4:b: ", b
    t = np.arange(0,8*np.pi, 0.001)
    x = 0
    y = 0

    for j in range(M):
        for i in range(N):
            x += a[j][i]*np.cos((i+1)*t)
            y += b[j][i]*np.sin((i+1)*t)
            print j
            plt.plot(x,y)
            fig = plt.gcf()
            fig.set_size_inches(2,2, forward = True)
            plt.show()
        #x = 0
        #y = 0


def main():
    answer = ""
    chicken()#intial      
    while answer != "nah":
        #chicken2()#select
        chicken3(chicken2())#breed
        chicken4()
        answer = raw_input("continue or nah?")
        
    
    #breed
    #mutate
        
    
main()
#==============================================================================
# t = np.arange(0,2*np.pi, 0.1)
# x = 16*np.sin(t)**3
# y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
# plt.plot(x,y)
# plt.show()
# 
#==============================================================================
