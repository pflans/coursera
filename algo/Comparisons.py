import os
import sys
from array import *
from random import *

comparisons = 0

def swap(array,a,b):
    array[a],array[b] = array[b],array[a]

def partition(array,start,end):
    global comparisons
    comparisons += len(array[start:end]) - 1
    left = start + 1
    pivot = array[end-1]
    for right in range(start+1,end):
        if pivot < array[left]:
            swap(array,left,pivot)
            left = left + 1
    swap(array,start,left-1) 
    return left-1

def quickSortHelper(array,start,end):
    if start < end:
    	#swap(array,array[start],array[end-1])
        splitPoint = partition(array,start,end)
        quickSortHelper(array,start,splitPoint)
        quickSortHelper(array,splitPoint+1,end)
        
def quickSort(array):
    quickSortHelper(array,0,len(array))
    return array


if __name__ == "__main__":

    
    array = [int(x) for x in open("test.txt").readlines()]
    options = sorted([array[0], array[(len(array)-1)/2], array[len(array)-1]])
    quickSort(array)   
    print array
    print options
    print comparisons
    
