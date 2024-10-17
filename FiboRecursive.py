# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 12:32:34 2024

@author: gilbe
"""

def FIBO(n):
    #ensure n is whole number in int format
    n = int(n)
    #Entry validation
    if n < 0:
        print("Must be positive number.")
        return
    if n > 50:
        print("Number too large. n<=50")
        return
    ## base cases
    if n <= 1:
        return n
    # compute recursivly to base case
    else:
        Fn = FIBO(n-1) + FIBO(n-2)
        return Fn
    
FIBO(33)