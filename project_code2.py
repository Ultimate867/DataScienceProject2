# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:06:08 2017

@author: Jack
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
dict = {}
number = 0

with open('vgsales2.csv','r') as f:
    reader = csv.reader(f, delimiter = ',')
    next(reader)
    
    for row in reader:
        x.append(row[4])
        y.append(float(row[6]))
        number += 1   
        if(number == 20):
            break
        
     
print(x)
print(y)
print()

x2 = np.arange(len(x))    
plt.bar(x2,y)
plt.xticks(x2, x, rotation= 'vertical')
plt.show()