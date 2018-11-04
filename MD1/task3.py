#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sys


sys.setrecursionlimit(1000000)

def extended_euclid_algorithm(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_euclid_algorithm(b % a, a)
        return (g, y - (b // a) * x, x)

def chinese_remainder_theorem(m_list, a_list):
    n_factor = np.prod(m_list)

    s_list = []
 
    for m_i in m_list:
        s_list.append(extended_euclid_algorithm(m_i, n_factor/m_i)[2])
    
    x = 0
    
    for m_i, a_i, s_i in zip(m_list, a_list, s_list):
        x += a_i * s_i * n_factor / m_i
    
    return x % n_factor


data = pd.read_csv('ieeja.txt', header=None)
data.columns = ['m']
m_list = data['m'].values.tolist()
a_list = [1,2,6]

print(m_list)
print(a_list)
print(int(chinese_remainder_theorem(m_list, a_list)))

