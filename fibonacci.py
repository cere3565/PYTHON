# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:41:54 2018

@author: Wan Jung
"""
#arr=input('arr：')
#print(nextFibonacci(arr))

def fibonacci(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

for i in range(0, 3):
    print(fibonacci(i), end=' ')

#def nextFibonacci(arr):
    ##return [ fibonacci(n) for n in arr, n + 1)
    