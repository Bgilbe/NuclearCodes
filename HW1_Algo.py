# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 13:07:54 2024

@author: gilbe
"""
#Homework 1 - Algorithms

### 1. Finding the Maximum Element in an Array

def find_max(arr):
    if len(arr)> 0:                     #checks for empty set, prevent error
        max = arr[0]                    #starts with index zero
        for n in range(1,len(arr)):     #compares from index 1 to length non-inclusive
            if arr[n] > max:            #finds larger
                max = arr[n]            #assigns if larger
        return(max)                     #at end of loop
    else: 
        print(end="Empty array. ")
        
####Code Tests####   
arr = [1, 5, 3, 9, 2]
print(find_max(arr))

#Check empty set
arr = []
print(find_max(arr))

#Check last position
arr = [1, 5, 3, 9, 2, 12]
print(find_max(arr))

#Check first position
arr = [12, 5, 3, 9, 2]
print(find_max(arr))

#Check float mix
arr = [1, 5, 3, 9.5, 2]
print(find_max(arr))

#%% 2. Binary Search Function

def binarySearch(target, arr):
    n = round((len(arr)/2))             #n=index being chacked
    i = n                               #i=increment of change
    while i>=1:
        i = round(i/2)                  #halves inc every loop
        if arr[n] == target:            #check current index for target
            return(n)
        elif arr[n] > target:           #if target is before n
            n-=i                        #dec index by i
            if i == 0:                  #corrects low end behavior around 1 & 0
                if arr[0] == target:
                    return(0)
        else:                           #target can only be after n
            n+=i                        #inc index by i
            if i == 0:                  #corrects high end behavior, checks last
                if arr[-1] == target:
                    return(n+1)
    return(-1)

####Code Tests####
#Given checks lower half max iteration
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
print(binarySearch(target, arr))

#Check same for list with even length
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 4
print(binarySearch(target, arr))

#Check for index 0 even/odd
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 1
print(binarySearch(target, arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 1
print(binarySearch(target, arr))

#Check last even/odd
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 9
print(binarySearch(target, arr))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
print(binarySearch(target, arr))

#Check upper half max iterations
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
print(binarySearch(target, arr))

#Check same for list with even length
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 9
print(binarySearch(target, arr))