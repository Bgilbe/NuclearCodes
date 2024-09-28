# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:09:47 2024

@author: gilbe
"""

###Merge sorted arrays

#Define function
def merge_sorted_arrays(A,B):
    C = []
    
    # go through both lists competely
    while A and B: #while values exist in both inputs
        if A[0] < B[0]:
            C.append(A.pop(0))
        
        else: #B consumed first in event of duplicate value
            C.append(B.pop(0))
    
    #If A longer, remainder sorted
    while A:
        C.append(A.pop(0))
    
    #If B longer
    while B:
        C.append(B.pop(0))
           
    return(C)
            
# Test code

#even alternating lists
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1,arr2))

#arr2 longer than arr1
arr1 = [1, 3, 5]
arr2 = [2, 4, 6, 7]
print(merge_sorted_arrays(arr1,arr2))

#arr1 longer than arr2
arr1 = [1, 3, 5, 9]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1,arr2))

#duplicate values
arr1 = [1, 4, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1,arr2))