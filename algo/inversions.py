import os
import sys

inversions = 0

def merge(left, right):
    global inversions
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            inversions += len(left[i:]) 
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(lst):
    if len(lst) <= 1:
        return lst
    middle = int(len(lst) / 2)
    left = mergesort(lst[:middle])
    right = mergesort(lst[middle:])
    return merge(left, right)





if __name__ == "__main__":

    
    array = [int(x) for x in open("IntegerArray.txt").readlines()]
    #array = [line.strip() for line in open('test.txt')]
    mergesort(array)
    print inversions