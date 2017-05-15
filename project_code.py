# -*- coding: utf-8 -*-
"""
Created on Sat May 13 20:59:08 2017

@author: Jack
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []


def graphA(x,y):
    x2 = np.arange(len(x))    
    plt.bar(x2,y)
    plt.xticks(x2, x, rotation= 'vertical')
    plt.xticks(x2, x)
    

def graphB(x,y):
    x2 = np.arange(len(x))  
    plt.scatter(x2,y)
    plt.xticks(x2, x, rotation = 'vertical')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Genre breakdown of video game sales in the United States in 2016')
    plt.legend()
    
with open('statistic_2015.csv','r') as f:
    reader = csv.reader(f, delimiter = ',')
    next(reader)
    next(reader)
    
    for row in reader:
        x.append(row[0])
        y.append(float(row[1]))
   
print(x)
print(y)

#graphA(x,y)
print()
graphB(x,y)
plt.show()

"""
x2 = np.arange(len(x))    
plt.bar(x2,y)
plt.xticks(x2, x)
plt.show()
"""