#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

def gcd(a:int, b:int) -> int: 
    """
    Calculates greatest common divisor of 2 numbers
    """
    
    if (a == 0): 
        return b 
    return gcd(b % a, a) 

def calculate_jacobi_symbol(m:int, n:int) -> int:
    """
    Calculates Jacobi symbol for 2 given numbers
    """
    if n < 0 or not n % 2:
        raise ValueError("n should be an odd positive integer")
    if m < 0 or m > n:
        m = m % n
    if not m:
        return int(n == 1)
    if n == 1 or m == 1:
        return 1
    if gcd(m, n) != 1:
        return 0

    j = 1
    if m < 0:
        m = -m
        if n % 4 == 3:
            j = -j
    while m != 0:
        while m % 2 == 0 and m > 0:
            m >>= 1
            if n % 8 in [3, 5]:
                j = -j
        m, n = n, m
        if m % 4 == 3 and n % 4 == 3:
            j = -j
        m %= n
    if n != 1:
        j = 0
    return j

data = pd.read_csv('ieeja.txt', header=None)
data.columns = ['m']
prime_list = data['m'].values.tolist()
a = None

for b in prime_list:
    if not a:
        a = b
        continue
    
    jacobi_symbol = calculate_jacobi_symbol(a, b)
    print("Jakobi symbol for numbers {a} and {b} is: {jacobi_symbol}".format(a=a, b=b, jacobi_symbol=jacobi_symbol))
    a = b

