#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwaps = 0
for j in range(len(a)-1):
    for i in range(len(a)-1):
        if a[i] > a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            numSwaps +=1
print('Array is sorted in',numSwaps,'swaps.')
print('First Element:',a[0],'\nLast Element:',a[-1])
