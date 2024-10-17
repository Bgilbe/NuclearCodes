# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:32:40 2024

@author: gilbe
"""
### 1. Climbing stairs

## (a) Top-Down Approach w/ Memoization
# Define Recursive function, i.e. top-down
def T_Dstairs(n,T_Dmemo={}):
    # prevent negative number error, 
    # also going down stairs would be same as going up
    n = abs(n)
    ## base cases
    # provide return point for n=0,1,or 2
    # provide recursion exit point for 4-1 and 4-2
    if n <= 3:
        return n
    # check memo for previous entry before computation
    if n in T_Dmemo:
        return T_Dmemo[n]
    # compute recursivly until n=3 or memo-ed values reached
    else:
        T_Dmemo[n] = T_Dstairs(n-1,T_Dmemo) + T_Dstairs(n-2,T_Dmemo)
        return T_Dmemo[n]

## (b) Bottom-Up Approach
# Define dynamic program
def B_Ustairs(n):
    n = abs(n)
    # base values
    if n <= 3:
        return n
    # Build empty array and init values
    climb = [0]*(n+1)
    climb[1] = 1
    climb[2] = 2
    # Create Tabulation Array
    i = 3
    while i <= n:
        climb[i] = climb[i-1] + climb[i-2]
        i+=1
    return(climb[n])  

    
def ClimbStairs():
    print("Choose determination method: (1)Top-Down (2)Bottom-Up")
    method = int(input("Choose 1 or 2: "))
    if method != 1 and method != 2:
        print("invalid choice")
        return
    # convert user string imput to int for index assesment/subtraction
    # also prevent fractional stairs error & wasted memory
    n = int(input("Enter number of stairs: "))
    how = 'climb'
    if n < 0:
        how = 'descend'
    if method == 1:
        steps = T_Dstairs(n)
    if method == 2:
        steps = B_Ustairs(n)
    print("\nTaking stairs one or two at a time...")
    print("There are",steps,"ways to",how,"the stairs")

ClimbStairs()